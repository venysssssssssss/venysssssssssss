<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&height=3&color=7C3AED" width="100%"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=13&duration=2800&pause=1200&color=7C3AED&center=true&vCenter=true&width=480&lines=clarity+%3E+cleverness;architecture+%3E+patchwork;systems+that+outlast+the+sprint" alt="Philosophy" />

<br/>

# Vinícius Reis

<p>
  <a href="https://www.linkedin.com/in/vinícius-gonçalves-reis-4544a921a">
    <img src="https://img.shields.io/badge/LinkedIn-0a0a0a?style=flat-square&logo=linkedin&logoColor=7C3AED"/>
  </a>
  &nbsp;
  <a href="https://github.com/venysssssssssss">
    <img src="https://img.shields.io/badge/GitHub-0a0a0a?style=flat-square&logo=github&logoColor=7C3AED"/>
  </a>
  &nbsp;
  <a href="mailto:viniciussport2004@gmail.com">
    <img src="https://img.shields.io/badge/Email-0a0a0a?style=flat-square&logo=gmail&logoColor=7C3AED"/>
  </a>
  &nbsp;
  <img src="https://komarev.com/ghpvc/?username=venysssssssssss&style=flat-square&color=7C3AED&labelColor=0a0a0a&label=profile+views"/>
</p>

</div>

<br/>

```
Backend · Data Systems · Automation · Applied AI
```

> I turn fragile manual workflows into **auditable, observable software**.  
> APIs with strict contracts. Pipelines with lineage. Automation with receipts.

<br/>

---

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

---

## Architecture Flow

How raw operations become decision-ready systems:

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#7C3AED', 'primaryTextColor': '#E2E8F0', 'primaryBorderColor': '#4C1D95', 'lineColor': '#475569', 'secondaryColor': '#1E293B', 'tertiaryColor': '#0F172A', 'background': '#0F172A', 'mainBkg': '#1E293B', 'nodeBorder': '#7C3AED', 'clusterBkg': '#1E293B', 'titleColor': '#A78BFA', 'edgeLabelBackground': '#1E293B', 'attributeBackgroundColorEven': '#1E293B', 'attributeBackgroundColorOdd': '#0F172A'}}}%%
graph LR
    classDef source  fill:#0F172A,stroke:#334155,stroke-width:1px,color:#94A3B8
    classDef layer   fill:#1E293B,stroke:#7C3AED,stroke-width:1px,color:#A78BFA
    classDef core    fill:#1E293B,stroke:#7C3AED,stroke-width:2px,color:#C4B5FD
    classDef output  fill:#4C1D95,stroke:#7C3AED,stroke-width:1px,color:#EDE9FE,font-weight:bold

    A[Raw Ops]:::source    -->|ETL / dbt|      B(Data Layer):::layer
    D[Documents]:::source  -->|Embeddings|     E(Vector Store):::layer
    B                      -->                 C{FastAPI Core}:::core
    E                      -->|RAG|            C
    C                      -->|Workers|        F[Batch Jobs]:::output
    C                      -->|REST / Events|  G[Decision Output]:::output
```

<br/>

---

## Stack

<table>
<tr>
<td valign="top" width="25%">

**Languages**
```
Python
Rust
SQL
Bash / PS
```

</td>
<td valign="top" width="25%">

**Data**
```
PostgreSQL
DuckDB
dbt
Qdrant
```

</td>
<td valign="top" width="25%">

**Backend**
```
FastAPI
Celery
Redis
Docker
```

</td>
<td valign="top" width="25%">

**Tooling**
```
SAP GUI
SFTP / FTP
Grafana
ClickUp API
```

</td>
</tr>
</table>

<br/>

---

## Stats

<div align="center">

<img height="160" src="https://github-readme-stats.vercel.app/api?username=venysssssssssss&show_icons=true&theme=transparent&hide_border=true&title_color=7C3AED&icon_color=7C3AED&text_color=94A3B8&bg_color=0D1117&ring_color=7C3AED&hide=stars" />
&nbsp;&nbsp;
<img height="160" src="https://github-readme-stats.vercel.app/api/top-langs/?username=venysssssssssss&layout=compact&theme=transparent&hide_border=true&title_color=7C3AED&text_color=94A3B8&bg_color=0D1117&langs_count=6" />

</div>

<br/>

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&height=3&color=7C3AED" width="100%"/>
<br/>
<sub><code>Build systems that outlast the engineer who wrote them.</code></sub>
</div>
