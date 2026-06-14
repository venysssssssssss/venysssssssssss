<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=7C3AED" width="100%"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=14&duration=2800&pause=1100&color=7C3AED&center=true&vCenter=true&width=520&lines=clarity+%3E+cleverness;architecture+%3E+patchwork;systems+that+outlast+the+sprint;APIs+with+contracts.+pipelines+with+lineage." alt="Philosophy" />

<br/>
<br/>

# Vinícius Reis

<p>
  <a href="https://www.linkedin.com/in/vinícius-gonçalves-reis-4544a921a">
    <img src="https://img.shields.io/badge/LinkedIn-0D1117?style=flat-square&logo=linkedin&logoColor=7C3AED"/>
  </a>
  &nbsp;
  <a href="https://github.com/venysssssssssss">
    <img src="https://img.shields.io/badge/GitHub-0D1117?style=flat-square&logo=github&logoColor=22D3EE"/>
  </a>
  &nbsp;
  <a href="mailto:viniciussport2004@gmail.com">
    <img src="https://img.shields.io/badge/Email-0D1117?style=flat-square&logo=gmail&logoColor=7C3AED"/>
  </a>
  &nbsp;
  <img src="https://komarev.com/ghpvc/?username=venysssssssssss&style=flat-square&color=7C3AED&labelColor=0D1117&label=profile+views"/>
</p>

<sub><code>Backend</code> &nbsp;·&nbsp; <code>Data Systems</code> &nbsp;·&nbsp; <code>Automation</code> &nbsp;·&nbsp; <code>Applied AI</code></sub>

</div>

<br/>

> I turn fragile manual workflows into **auditable, observable software**.  
> APIs with strict contracts. Pipelines with lineage. Automation with receipts.

<br/>

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=22D3EE" width="100%"/>

## Surface

My work is organized around four load-bearing pillars — not feature lists, but operational scopes where I take full-stack ownership.

<br/>

**`Backend Systems`**
Production-grade interfaces built for operators, not demos. Resilient APIs, async task runners, service-layer separation, and strict validation contracts. Primary stack: **FastAPI**, **Rust**.

**`Data Infrastructure`**
Clean analytical pipelines from raw to decision-ready. SQL modeling, schema enforcement, incremental ingestion, and quality gates — built on **dbt**, **DuckDB**, **PostgreSQL**.

**`Applied AI & Search`**
Friction-free AI infrastructure: **RAG** architectures, document processing pipelines, advanced vector search with **Qdrant**, and orchestration of local LLMs and knowledge-base services.

**`Operational Automation`**
Replace brittle routines with auditable software. Python extraction engines, SFTP ingestion, SAP/ClickUp/Grafana integrations, scheduled batch jobs via **Bash** and **PowerShell**.

<br/>

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=7C3AED" width="100%"/>

## Architecture Flow

How raw operations become decision-ready systems:

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'fontFamily': 'JetBrains Mono, monospace', 'lineColor': '#475569', 'edgeLabelBackground': '#0F172A' }}}%%
graph LR
    classDef source  fill:#0F172A,stroke:#334155,stroke-width:1px,color:#94A3B8
    classDef layer   fill:#1E293B,stroke:#7C3AED,stroke-width:1px,color:#C4B5FD
    classDef ai      fill:#1E293B,stroke:#22D3EE,stroke-width:1px,color:#67E8F9
    classDef core    fill:#1E293B,stroke:#7C3AED,stroke-width:2px,color:#C4B5FD
    classDef output  fill:#4C1D95,stroke:#7C3AED,stroke-width:1px,color:#EDE9FE

    A[Raw Ops]:::source    -->|ETL / dbt|      B(Data Layer):::layer
    D[Documents]:::source  -->|Embeddings|     E(Vector Store):::ai
    B                      -->                 C{FastAPI Core}:::core
    E                      -->|RAG|            C
    C                      -->|Workers|        F[Batch Jobs]:::output
    C                      -->|REST / Events|  G[Decision Output]:::output
```

<br/>

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=22D3EE" width="100%"/>

## Stack

<div align="center">
<br/>

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

<br/>
<br/>

<sub><b>D A T A</b></sub>
<br/>
<img src="https://img.shields.io/badge/PostgreSQL-0D1117?style=flat-square&logo=postgresql&logoColor=22D3EE"/>
&nbsp;
<img src="https://img.shields.io/badge/DuckDB-0D1117?style=flat-square&logo=duckdb&logoColor=22D3EE"/>
&nbsp;
<img src="https://img.shields.io/badge/dbt-0D1117?style=flat-square&logo=dbt&logoColor=22D3EE"/>
&nbsp;
<img src="https://img.shields.io/badge/Qdrant-0D1117?style=flat-square&logo=qdrant&logoColor=22D3EE"/>

<br/>
<br/>

<sub><b>B A C K E N D</b></sub>
<br/>
<img src="https://img.shields.io/badge/FastAPI-0D1117?style=flat-square&logo=fastapi&logoColor=7C3AED"/>
&nbsp;
<img src="https://img.shields.io/badge/Celery-0D1117?style=flat-square&logo=celery&logoColor=7C3AED"/>
&nbsp;
<img src="https://img.shields.io/badge/Redis-0D1117?style=flat-square&logo=redis&logoColor=7C3AED"/>
&nbsp;
<img src="https://img.shields.io/badge/Docker-0D1117?style=flat-square&logo=docker&logoColor=7C3AED"/>

<br/>
<br/>

<sub><b>T O O L I N G</b></sub>
<br/>
<img src="https://img.shields.io/badge/SAP_GUI-0D1117?style=flat-square&logo=sap&logoColor=22D3EE"/>
&nbsp;
<img src="https://img.shields.io/badge/SFTP_/_FTP-0D1117?style=flat-square&logo=files&logoColor=22D3EE"/>
&nbsp;
<img src="https://img.shields.io/badge/Grafana-0D1117?style=flat-square&logo=grafana&logoColor=22D3EE"/>
&nbsp;
<img src="https://img.shields.io/badge/ClickUp-0D1117?style=flat-square&logo=clickup&logoColor=22D3EE"/>

<br/>
</div>

<br/>

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=7C3AED" width="100%"/>

## Stats

<div align="center">

<img height="170" src="https://github-readme-stats.vercel.app/api?username=venysssssssssss&show_icons=true&include_all_commits=true&count_private=true&hide_border=true&hide=stars&title_color=7C3AED&icon_color=22D3EE&text_color=94A3B8&bg_color=0D1117&ring_color=7C3AED" />
&nbsp;
<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=venysssssssssss&layout=compact&hide_border=true&langs_count=8&title_color=22D3EE&text_color=94A3B8&bg_color=0D1117" />

<br/>
<br/>

<img height="170" src="https://streak-stats.demolab.com?user=venysssssssssss&hide_border=true&background=0D1117&stroke=1E293B&ring=7C3AED&fire=22D3EE&currStreakLabel=A78BFA&currStreakNum=E2E8F0&sideNums=E2E8F0&sideLabels=94A3B8&dates=64748B" />

<br/>
<br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=venysssssssssss&bg_color=0D1117&color=A78BFA&line=7C3AED&point=22D3EE&area=true&area_color=7C3AED&hide_border=true&custom_title=Contribution%20Signal" width="98%" />

</div>

<br/>

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=22D3EE" width="100%"/>

<div align="center">
<br/>
<sub><code>Build systems that outlast the engineer who wrote them.</code></sub>
<br/>
<br/>
<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=7C3AED" width="100%"/>
</div>
