#!/usr/bin/env python3
"""
generate_pipeline_art.py — renders assets/pipeline-art.svg from live GitHub data.

Generative pipeline art: my most active repos become source nodes feeding a
raw → trusted → decisions pipeline. Animated pulses flow along the edges —
their count and speed come from real commit activity over the last 30 days,
their color from each repo's primary language. Layout is seeded by the day +
the data, so the render changes daily but is fully reproducible; the seed and
inputs are embedded in the SVG as a receipt.

Pure stdlib (no pip deps). Runs in CI via GITHUB_TOKEN.

Usage:
    GITHUB_USER=venysssssssssss GITHUB_TOKEN=*** python scripts/generate_pipeline_art.py
    python scripts/generate_pipeline_art.py --demo   # render with sample data
"""
import os, sys, json, html, random, hashlib, datetime, urllib.request, urllib.error

USER  = os.environ.get("GITHUB_USER", "venysssssssssss")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT   = os.environ.get("ART_OUT", "assets/pipeline-art.svg")

MAX_SOURCES = 7
WINDOW_DAYS = 30

# brand ramp — stable color per language, all within the violet/cyan family
LANG_COLORS = {
    "Python": "#A78BFA", "TypeScript": "#67E8F9", "Rust": "#C4B5FD",
    "JavaScript": "#7DD3FC", "Java": "#5EEAD4", "Dart": "#8B5CF6",
    "HTML": "#7DD3FC", "Shell": "#5EEAD4", "Jupyter Notebook": "#A78BFA",
}
RAMP = ["#A78BFA", "#67E8F9", "#C4B5FD", "#5EEAD4", "#7DD3FC", "#8B5CF6"]
GRAY = "#64748B"


def api(url):
    headers = {"User-Agent": "venys-pipeline-art", "Accept": "application/vnd.github+json"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fetch():
    """Top repos by 30-day activity (public events), padded by recent pushes."""
    cutoff = (datetime.datetime.now(datetime.timezone.utc)
              - datetime.timedelta(days=WINDOW_DAYS)).isoformat()

    commits = {}   # repo name -> commit count from PushEvents
    for page in range(1, 4):  # events API caps at ~300 recent events
        batch = api(f"https://api.github.com/users/{USER}/events/public"
                    f"?per_page=100&page={page}")
        for ev in batch:
            if ev.get("created_at", "") < cutoff:
                break
            name = ev.get("repo", {}).get("name", "").split("/")[-1]
            if name == USER:
                continue  # profile repo commits are mostly this pipeline's own bot
            if ev.get("type") == "PushEvent":
                commits[name] = commits.get(name, 0) + ev["payload"].get("size", 1)
        if len(batch) < 100:
            break

    repos = []
    for page in range(1, 6):
        batch = api(f"https://api.github.com/users/{USER}/repos"
                    f"?per_page=100&page={page}&sort=pushed&type=owner")
        repos += [r for r in batch if not r.get("fork") and r["name"] != USER]
        if len(batch) < 100:
            break
    by_name = {r["name"]: r for r in repos}

    # active repos first (by commits), then pad with most recently pushed
    names = sorted(commits, key=commits.get, reverse=True)
    names = [n for n in names if n in by_name]
    for r in repos:
        if len(names) >= MAX_SOURCES:
            break
        if r["name"] not in names:
            names.append(r["name"])

    sources = [{
        "name": n,
        "commits": commits.get(n, 0),
        "lang": by_name[n].get("language") or "",
    } for n in names[:MAX_SOURCES]]

    if not sources:
        print("no source repos found", file=sys.stderr)
        sys.exit(1)
    return sources


def demo():
    return [
        {"name": "schema-guard", "commits": 14, "lang": "Python"},
        {"name": "raw-to-trusted-pncp", "commits": 9, "lang": "TypeScript"},
        {"name": "data-intake-selic-bc", "commits": 6, "lang": "Python"},
        {"name": "mini-software-house", "commits": 4, "lang": "Python"},
        {"name": "synapse-like", "commits": 2, "lang": "Python"},
        {"name": "rusting-things-baby", "commits": 1, "lang": "Rust"},
    ]


def esc(s):
    return html.escape(str(s), quote=True)


def lang_color(lang):
    if not lang:
        return GRAY
    if lang in LANG_COLORS:
        return LANG_COLORS[lang]
    return RAMP[int(hashlib.sha256(lang.encode()).hexdigest(), 16) % len(RAMP)]


def render(sources, demo_mode=False):
    today = datetime.date.today().isoformat()
    inputs = {s["name"]: s["commits"] for s in sources}
    seed = hashlib.sha256(
        f"{today}|{json.dumps(inputs, sort_keys=True)}".encode()).hexdigest()[:12]
    rng = random.Random(seed)

    n = len(sources)
    total = sum(s["commits"] for s in sources)
    W = 920
    top, row_h, footer = 96, 44, 74
    H = max(320, top + n * row_h + footer)
    area_y0, area_y1 = top, H - footer
    hub_cy = (area_y0 + area_y1) / 2

    SRC_X, RAW_X, TRU_X, OUT_X = 216, 452, 622, 806

    defs, body, particles = [], [], []

    def edge(pid, x1, y1, x2, y2, bend):
        c1x = x1 + 70 + rng.uniform(-12, 12)
        c2x = x2 - 80 + rng.uniform(-12, 12)
        c2y = y2 + bend
        d = f"M {x1:.1f} {y1:.1f} C {c1x:.1f} {y1:.1f}, {c2x:.1f} {c2y:.1f}, {x2:.1f} {y2:.1f}"
        defs.append(f'<path id="{pid}" d="{d}" fill="none"/>')
        body.append(f'<use href="#{pid}" stroke="#1E293B" stroke-width="1.2"/>')
        return d

    def pulses(pid, color, count, dur, r=2.6, opacity=0.9):
        for k in range(count):
            begin = -rng.uniform(0, dur)
            particles.append(
                f'<circle r="{r}" fill="{color}" opacity="{opacity}">'
                f'<animateMotion dur="{dur:.2f}s" begin="{begin:.2f}s" repeatCount="indefinite">'
                f'<mpath xlink:href="#{pid}"/></animateMotion></circle>')

    # ── source nodes → raw hub ──────────────────────────────────────────
    max_c = max((s["commits"] for s in sources), default=0) or 1
    for i, s in enumerate(sources):
        cy = area_y0 + row_h * (i + 0.5) + rng.uniform(-6, 6)
        col = lang_color(s["lang"])
        act = s["commits"]
        r_node = 4.5 + 4.0 * (act / max_c)
        pid = f"e{i}"
        edge(pid, SRC_X + r_node + 2, cy, RAW_X - 14, hub_cy, rng.uniform(-18, 18))
        # pulse density and speed follow real activity
        pulses(pid, col, 1 + min(3, act // 3), 7.0 - 4.0 * (act / max_c) + rng.uniform(-0.4, 0.4))
        glow_dur = 2.6 - 1.2 * (act / max_c)
        body.append(
            f'<circle cx="{SRC_X}" cy="{cy:.1f}" r="{r_node:.1f}" fill="{col}">'
            f'<animate attributeName="opacity" values="1;0.45;1" dur="{glow_dur:.2f}s" repeatCount="indefinite"/></circle>')
        label = esc(s["name"][:20])
        suffix = f'<tspan fill="#475569"> ·{act}c</tspan>' if act else ""
        body.append(
            f'<text x="{SRC_X - 14}" y="{cy + 4:.1f}" text-anchor="end" font-size="12" fill="#94A3B8">{label}{suffix}</text>')

    # ── hub → hub → output ──────────────────────────────────────────────
    agg = max(3, min(8, 2 + total // 4))
    edge("h1", RAW_X + 14, hub_cy, TRU_X - 14, hub_cy, rng.uniform(-26, 26))
    pulses("h1", "#A78BFA", agg, 3.4, r=2.2, opacity=0.8)
    edge("h2", TRU_X + 14, hub_cy, OUT_X - 18, hub_cy, rng.uniform(-26, 26))
    pulses("h2", "#67E8F9", agg, 3.4, r=2.2, opacity=0.8)

    def hub(cx, label, color, r=11):
        body.append(
            f'<circle cx="{cx}" cy="{hub_cy:.1f}" r="{r + 6}" fill="none" stroke="{color}" '
            f'stroke-width="1" stroke-dasharray="4 5" opacity="0.55">'
            f'<animateTransform attributeName="transform" type="rotate" '
            f'from="0 {cx} {hub_cy:.1f}" to="360 {cx} {hub_cy:.1f}" dur="14s" repeatCount="indefinite"/></circle>')
        body.append(f'<circle cx="{cx}" cy="{hub_cy:.1f}" r="{r}" fill="#0F172A" stroke="{color}" stroke-width="1.6"/>')
        body.append(
            f'<text x="{cx}" y="{hub_cy + 34:.1f}" text-anchor="middle" '
            f'font-size="11" fill="{color}" letter-spacing="2">{label}</text>')

    hub(RAW_X, "RAW", "#A78BFA")
    hub(TRU_X, "TRUSTED", "#22D3EE")
    body.append(
        f'<circle cx="{OUT_X}" cy="{hub_cy:.1f}" r="15" fill="#4C1D95" stroke="#A78BFA" stroke-width="1.8">'
        f'<animate attributeName="stroke-width" values="1.8;3.2;1.8" dur="2.4s" repeatCount="indefinite"/></circle>')
    body.append(
        f'<text x="{OUT_X}" y="{hub_cy + 40:.1f}" text-anchor="middle" font-size="11" '
        f'fill="#C4B5FD" letter-spacing="2">DECISIONS</text>')

    # ── chrome: prompt + footer ─────────────────────────────────────────
    if demo_mode:
        mode = "demo data"
    elif total:
        mode = f"{total} commits/{WINDOW_DAYS}d"
    else:
        mode = "standby — idling until next push"
    prompt = (f'<text x="28" y="66" font-size="14">'
              f'<tspan fill="#A78BFA">visitor@venys</tspan><tspan fill="#475569">:</tspan>'
              f'<tspan fill="#22D3EE">~</tspan><tspan fill="#475569">$ </tspan>'
              f'<tspan fill="#E2E8F0">watch -n 86400 ./render_pipeline --live</tspan></text>')
    foot = (f'<text x="28" y="{H - 26}" font-size="12">'
            f'<tspan fill="#475569">└─ inputs ▸ </tspan>'
            f'<tspan fill="#94A3B8">{n} repos · {mode}</tspan>'
            f'<tspan fill="#475569"> · seed </tspan><tspan fill="#67E8F9">{seed}</tspan>'
            f'<tspan fill="#475569"> · {today} · deterministic — same day + same data = same art</tspan></text>')

    receipt = json.dumps({"date": today, "seed": seed, "user": USER,
                          "window_days": WINDOW_DAYS, "inputs": inputs,
                          "generator": "scripts/generate_pipeline_art.py"}, sort_keys=True)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" role="img" aria-label="Generative pipeline art rendered daily from live commit activity">
<!-- receipt: {esc(receipt)} -->
  <defs>{"".join(defs)}</defs>
  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="12" fill="#0D1117" stroke="#1E293B"/>
  <rect x="1" y="1" width="{W - 2}" height="34" rx="12" fill="#0F172A"/>
  <rect x="1" y="22" width="{W - 2}" height="13" fill="#0F172A"/>
  <circle cx="26" cy="18" r="5.5" fill="#7C3AED"/>
  <circle cx="46" cy="18" r="5.5" fill="#22D3EE"/>
  <circle cx="66" cy="18" r="5.5" fill="#334155"/>
  <text x="{W // 2}" y="22" text-anchor="middle" font-family="ui-monospace, SFMono-Regular, monospace" font-size="12" fill="#475569">pipeline.live — generative · self-rendered</text>
  <g font-family="ui-monospace, SFMono-Regular, Menlo, monospace">
    {prompt}
    {"".join(body)}
    {"".join(particles)}
    {foot}
  </g>
</svg>
'''


def main():
    demo_mode = "--demo" in sys.argv
    sources = demo() if demo_mode else fetch()
    svg = render(sources, demo_mode)

    # self-check: well-formed XML, animation present
    import xml.etree.ElementTree as ET
    root = ET.fromstring(svg)
    motions = root.iter("{http://www.w3.org/2000/svg}animateMotion")
    assert sum(1 for _ in motions) >= len(sources), "missing pulse animations"

    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote {OUT}  ({len(sources)} sources, "
          f"{sum(s['commits'] for s in sources)} commits/{WINDOW_DAYS}d)")


if __name__ == "__main__":
    main()
