<div align="center">

<img src="./assets/terminal.svg" width="92%" alt="venys@tekhnai terminal session"/>

<br/>
<br/>

# Vinícius Reis

<p>
  <a href="https://github.com/Tekhnai">
    <img src="https://img.shields.io/badge/CEO_/_CTO-Tekhnai-0D1117?style=flat-square&labelColor=0D1117&color=7C3AED&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0iIzdDM0FFRCI+PHBhdGggZD0iTTEyIDJsOC42NiA1djEwTDEyIDIybC04LjY2LTVWN3oiLz48L3N2Zz4="/>
  </a>
  &nbsp;
  <a href="https://venys.vercel.app">
    <img src="https://img.shields.io/badge/Portfolio-0D1117?style=flat-square&logo=vercel&logoColor=22D3EE"/>
  </a>
  &nbsp;
  <a href="https://www.linkedin.com/in/vinícius-gonçalves-reis-4544a921a">
    <img src="https://img.shields.io/badge/LinkedIn-0D1117?style=flat-square&logo=linkedin&logoColor=7C3AED"/>
  </a>
  &nbsp;
  <a href="mailto:viniciussport2004@gmail.com">
    <img src="https://img.shields.io/badge/Email-0D1117?style=flat-square&logo=gmail&logoColor=22D3EE"/>
  </a>
  &nbsp;
  <img src="https://komarev.com/ghpvc/?username=venysssssssssss&style=flat-square&color=7C3AED&labelColor=0D1117&label=visitors"/>
</p>

<sub><i>clarity > cleverness &nbsp;·&nbsp; architecture > patchwork &nbsp;·&nbsp; systems that outlast the sprint</i></sub>

</div>

<br/>

> I turn fragile manual workflows into **auditable, observable software**.  
> APIs with strict contracts. Pipelines with lineage. Automation with receipts.

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=7C3AED" width="100%"/>

## Surface

Four load-bearing pillars — operational scopes where I take full-stack ownership.

**`Backend Systems`** — Production interfaces built for operators, not demos. Resilient APIs, async task runners, service-layer separation, strict validation contracts. **FastAPI**, **Rust**.

**`Data Infrastructure`** — Clean analytical pipelines from raw to decision-ready. SQL modeling, schema enforcement, incremental ingestion, quality gates. **dbt**, **DuckDB**, **PostgreSQL**.

**`Applied AI & Search`** — Friction-free AI infrastructure: **RAG** architectures, document pipelines, vector search with **Qdrant**, local LLM orchestration.

**`Operational Automation`** — Brittle routines replaced by auditable software. Extraction engines, SFTP ingestion, SAP/ClickUp/Grafana integrations, scheduled jobs via **Bash** and **PowerShell**.

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=22D3EE" width="100%"/>

## Architecture Flow

<div align="center">
<img src="./assets/pipeline.svg" width="100%" alt="data pipeline"/>
</div>

<details>
<summary><b>↳ precise topology</b> &nbsp;<sub>(click to expand the wiring)</sub></summary>
<br/>

```mermaid
%%{init: {'theme':'dark','themeVariables':{'fontFamily':'monospace','lineColor':'#475569','edgeLabelBackground':'#1E293B'}}}%%
graph LR
    A[Raw Ops] -->|ETL| B(Data Layer)
    D[Documents] -->|embeddings| E(Vector Store)
    B --> C{FastAPI Core}
    E -->|RAG| C
    C -->|workers| F[Batch Jobs]
    C -->|events| G[Decision Output]

    classDef source fill:#0F172A,stroke:#334155,color:#94A3B8
    classDef layer fill:#1E293B,stroke:#7C3AED,color:#C4B5FD
    classDef ai fill:#1E293B,stroke:#22D3EE,color:#67E8F9
    classDef core fill:#1E293B,stroke:#7C3AED,stroke-width:2px,color:#C4B5FD
    classDef output fill:#4C1D95,stroke:#7C3AED,color:#EDE9FE

    class A,D source
    class B layer
    class E ai
    class C core
    class F,G output
```

</details>

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=7C3AED" width="100%"/>

## Stack

<div align="center">
<img src="./assets/stack-monitor.svg" width="100%" alt="stack monitor"/>
</div>

<details>
<summary><b>↳ full toolchain</b> &nbsp;<sub>(every package, enumerated)</sub></summary>
<br/>
<div align="center">

<sub><b>L A N G U A G E S</b></sub>
<br/>
<img src="https://img.shields.io/badge/Python-0D1117?style=flat-square&logo=python&logoColor=7C3AED"/>
&nbsp;
<img src="https://img.shields.io/badge/Rust-0D1117?style=flat-square&logo=rust&logoColor=7C3AED"/>
&nbsp;
<img src="https://img.shields.io/badge/SQL-0D1117?style=flat-square&logo=postgresql&logoColor=7C3AED"/>
&nbsp;
<img src="https://img.shields.io/badge/Bash-0D1117?style=flat-square&logo=gnubash&logoColor=7C3AED"/>
&nbsp;
<img src="https://img.shields.io/badge/PowerShell-0D1117?style=flat-square&logo=powershell&logoColor=7C3AED"/>

<br/><br/>

<sub><b>D A T A</b></sub>
<br/>
<img src="https://img.shields.io/badge/PostgreSQL-0D1117?style=flat-square&logo=postgresql&logoColor=22D3EE"/>
&nbsp;
<img src="https://img.shields.io/badge/DuckDB-0D1117?style=flat-square&logo=duckdb&logoColor=22D3EE"/>
&nbsp;
<img src="https://img.shields.io/badge/dbt-0D1117?style=flat-square&logo=dbt&logoColor=22D3EE"/>
&nbsp;
<img src="https://img.shields.io/badge/Qdrant-0D1117?style=flat-square&logo=qdrant&logoColor=22D3EE"/>

<br/><br/>

<sub><b>B A C K E N D</b></sub>
<br/>
<img src="https://img.shields.io/badge/FastAPI-0D1117?style=flat-square&logo=fastapi&logoColor=7C3AED"/>
&nbsp;
<img src="https://img.shields.io/badge/Celery-0D1117?style=flat-square&logo=celery&logoColor=7C3AED"/>
&nbsp;
<img src="https://img.shields.io/badge/Redis-0D1117?style=flat-square&logo=redis&logoColor=7C3AED"/>
&nbsp;
<img src="https://img.shields.io/badge/Docker-0D1117?style=flat-square&logo=docker&logoColor=7C3AED"/>

<br/><br/>

<sub><b>T O O L I N G</b></sub>
<br/>
<img src="https://img.shields.io/badge/SAP_GUI-0D1117?style=flat-square&logo=sap&logoColor=22D3EE"/>
&nbsp;
<img src="https://img.shields.io/badge/SFTP_/_FTP-0D1117?style=flat-square&logoColor=22D3EE"/>
&nbsp;
<img src="https://img.shields.io/badge/Grafana-0D1117?style=flat-square&logo=grafana&logoColor=22D3EE"/>
&nbsp;
<img src="https://img.shields.io/badge/ClickUp-0D1117?style=flat-square&logo=clickup&logoColor=22D3EE"/>

</div>
</details>

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=22D3EE" width="100%"/>

## Stats

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=venysssssssssss&show_icons=true&include_all_commits=true&count_private=true&hide_border=true&hide=stars&title_color=7C3AED&icon_color=22D3EE&text_color=94A3B8&bg_color=0D1117&ring_color=7C3AED" alt="stats"/>
&nbsp;
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=venysssssssssss&layout=compact&hide_border=true&langs_count=8&title_color=22D3EE&text_color=94A3B8&bg_color=0D1117" alt="top languages"/>

</div>

<br/>

<details>
<summary><b>$ neofetch</b> &nbsp;<sub>(system specs)</sub></summary>

```
        ⬡ ⬡ ⬡           venys@tekhnai
      ⬡       ⬡         ──────────────────────────────────────
     ⬡  ▟█▙   ⬡         role    ▸  CEO / CTO · backend & data systems
     ⬡  ▜█▛   ⬡         os      ▸  Kali Linux · WSL2 · Windows
      ⬡       ⬡         shell   ▸  zsh · tmux · nvim
        ⬡ ⬡ ⬡           lang    ▸  Python · Rust · SQL
                        stack   ▸  FastAPI · dbt · DuckDB · Qdrant
                        infra   ▸  Docker · Redis · Celery · Grafana
                        focus   ▸  raw ops ─→ decision systems
                        uptime  ▸  shipping since 2021
                        ───────────────────────────────────────
                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  violet · cyan
```

</details>

<br/>

<div align="center">
<sub><code>Build systems that outlast the engineer who wrote them.</code></sub>
</div>
