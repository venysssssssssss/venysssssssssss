#!/usr/bin/env python3
"""
generate_status.py — renders assets/status.svg from live GitHub data.

Self-built profile telemetry: aggregates the primary language across all
public repos, repo count, and most-recent push, then renders an animated
terminal-style SVG. Pure stdlib (no pip deps). Runs in CI via GITHUB_TOKEN.

Usage:
    GITHUB_USER=venysssssssssss GITHUB_TOKEN=*** python scripts/generate_status.py
    python scripts/generate_status.py --demo   # render with sample data
"""
import os, sys, json, html, collections, datetime, urllib.request, urllib.error

USER  = os.environ.get("GITHUB_USER", "venysssssssssss")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT   = os.environ.get("STATUS_OUT", "assets/status.svg")

# two-tone palette, alternated per language row
VIOLET, CYAN = "#A78BFA", "#67E8F9"
TRACK = "#161E2E"


def api(url):
    headers = {"User-Agent": "venys-status", "Accept": "application/vnd.github+json"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fetch():
    repos = []
    for page in range(1, 6):  # up to 500 repos
        batch = api(f"https://api.github.com/users/{USER}/repos"
                    f"?per_page=100&page={page}&sort=pushed&type=owner")
        repos += batch
        if len(batch) < 100:
            break
    langs = collections.Counter()
    recent_at, recent_name = "", ""
    for r in repos:
        if r.get("fork"):
            continue
        if r.get("language"):
            langs[r["language"]] += 1
        p = r.get("pushed_at") or ""
        if p > recent_at:
            recent_at, recent_name = p, r.get("name", "")
    return {
        "repos": len([r for r in repos if not r.get("fork")]),
        "langs": langs.most_common(5),
        "lang_total": sum(langs.values()) or 1,
        "last_push": recent_at[:10],
        "last_repo": recent_name,
    }


def demo():
    return {
        "repos": 103,
        "langs": [("Python", 46), ("Jupyter Notebook", 14), ("TypeScript", 12),
                  ("Rust", 9), ("Shell", 8)],
        "lang_total": 89,
        "last_push": datetime.date.today().isoformat(),
        "last_repo": "elt-sftp-enel",
    }


def esc(s):
    return html.escape(str(s), quote=True)


def render(d):
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    rows = []
    clips = []
    y = 150
    BAR_X, BAR_W = 250, 300
    for i, (name, count) in enumerate(d["langs"]):
        pct = round(100 * count / d["lang_total"])
        col = VIOLET if i % 2 == 0 else CYAN
        fill_w = max(4, round(BAR_W * count / d["lang_total"]))
        cid = f"bar{i}"
        clips.append(
            f'<clipPath id="{cid}"><rect x="{BAR_X}" y="{y-12}" width="0" height="14">'
            f'<animate attributeName="width" from="0" to="{fill_w}" '
            f'begin="{0.5 + i*0.18:.2f}s" dur="0.9s" fill="freeze"/></rect></clipPath>'
        )
        rows.append(f'''
    <text x="70" y="{y}" font-size="13" fill="#475569">│</text>
    <text x="92" y="{y}" font-size="13" fill="#94A3B8">{esc(name.lower())[:16]}</text>
    <rect x="{BAR_X}" y="{y-12}" width="{BAR_W}" height="14" rx="3" fill="{TRACK}"/>
    <g clip-path="url(#{cid})"><rect x="{BAR_X}" y="{y-12}" width="{BAR_W}" height="14" rx="3" fill="{col}"/></g>
    <text x="{BAR_X+BAR_W+16}" y="{y}" font-size="12" fill="{col}">{pct}%</text>''')
        y += 30

    height = y + 70
    bars = "".join(rows)
    clipdefs = "".join(clips)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 {height}" role="img" aria-label="Live profile status">
  <defs>{clipdefs}</defs>
  <rect x="1" y="1" width="758" height="{height-2}" rx="12" fill="#0D1117" stroke="#1E293B"/>
  <rect x="1" y="1" width="758" height="34" rx="12" fill="#0F172A"/>
  <rect x="1" y="22" width="758" height="13" fill="#0F172A"/>
  <circle cx="26" cy="18" r="5.5" fill="#7C3AED"/>
  <circle cx="46" cy="18" r="5.5" fill="#22D3EE"/>
  <circle cx="66" cy="18" r="5.5" fill="#334155"/>
  <text x="380" y="22" text-anchor="middle" font-family="ui-monospace, SFMono-Regular, monospace" font-size="12" fill="#475569">profile.service — telemetry</text>

  <g font-family="ui-monospace, SFMono-Regular, Menlo, monospace">
    <text x="28" y="68" font-size="14"><tspan fill="#A78BFA">venys@tekhnai</tspan><tspan fill="#475569">:</tspan><tspan fill="#22D3EE">~</tspan><tspan fill="#475569">$ </tspan><tspan fill="#E2E8F0">systemctl status profile</tspan></text>

    <circle cx="34" cy="96" r="5" fill="#22D3EE"><animate attributeName="opacity" values="1;0.25;1" dur="1.6s" repeatCount="indefinite"/></circle>
    <text x="48" y="101" font-size="14"><tspan fill="#C4B5FD">profile.service</tspan><tspan fill="#64748B"> — </tspan><tspan fill="#67E8F9">active (running)</tspan></text>

    <text x="70" y="130" font-size="13"><tspan fill="#475569">├─ </tspan><tspan fill="#94A3B8">repos     </tspan><tspan fill="#475569">▸ </tspan><tspan fill="#E2E8F0">{d["repos"]} public</tspan></text>
    <text x="70" y="{150-12-6}" font-size="13" opacity="0"> </text>
{bars}
    <text x="70" y="{y}" font-size="13"><tspan fill="#475569">├─ </tspan><tspan fill="#94A3B8">last push </tspan><tspan fill="#475569">▸ </tspan><tspan fill="#67E8F9">{esc(d["last_push"])}</tspan><tspan fill="#475569"> · </tspan><tspan fill="#94A3B8">{esc(d["last_repo"])[:28]}</tspan></text>
    <text x="70" y="{y+26}" font-size="13"><tspan fill="#475569">└─ </tspan><tspan fill="#94A3B8">synced    </tspan><tspan fill="#475569">▸ </tspan><tspan fill="#64748B">{now} · self-generated via github actions</tspan></text>
  </g>
</svg>
'''


def main():
    if "--demo" in sys.argv:
        data = demo()
    else:
        try:
            data = fetch()
        except urllib.error.HTTPError as e:
            print(f"API error {e.code}: falling back to demo", file=sys.stderr)
            data = demo()
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(render(data))
    print(f"wrote {OUT}  ({data['repos']} repos, {len(data['langs'])} langs)")


if __name__ == "__main__":
    main()
