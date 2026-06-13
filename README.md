<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&height=4&color=7C3AED" width="100%"/>

<br><br>

# VINÍCIUS REIS
**`BACKEND`** &nbsp;•&nbsp; **`DATA SYSTEMS`** &nbsp;•&nbsp; **`AUTOMATION`** &nbsp;•&nbsp; **`APPLIED AI`**

<br>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-000000?style=flat-square&logo=linkedin&logoColor=7C3AED)](https://www.linkedin.com/in/vinícius-gonçalves-reis-4544a921a)
[![GitHub](https://img.shields.io/badge/GitHub-000000?style=flat-square&logo=github&logoColor=7C3AED)](https://github.com/venysssssssssss)
[![Email](https://img.shields.io/badge/Email-000000?style=flat-square&logo=gmail&logoColor=7C3AED)](mailto:viniciussport2004@gmail.com)
[![Signal](https://komarev.com/ghpvc/?username=venysssssssssss&style=flat-square&color=000000&labelColor=000000&label=signal&logo=activity&logoColor=7C3AED)](https://github.com/venysssssssssss)

<br>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=15&duration=3000&pause=1000&color=94A3B8&center=true&vCenter=true&width=600&lines=System+architecture+for+real+operations.;Turning+fragile+workflows+into+auditable+software.;Clarity+%3E+Cleverness.+Architecture+%3E+Patchwork." alt="Engineering Philosophy" />

<br><br>

</div>

## ⬢ Engineering Surface

Em vez de listas exaustivas, minha atuação é dividida em quatro pilares de infraestrutura, focados em estabilidade, rastreabilidade e escala.

> **`01` Backend Systems**
> Desenho e implementação de interfaces orientadas à produção. APIs resilientes, service layers, processamento assíncrono (runners), control planes e contratos estritos de validação utilizando **FastAPI** e **Rust**.

> **`02` Data Infrastructure**
> Engenharia de pipelines analíticos limpos. Modelagem SQL, orquestração com **dbt**, processamento escalável com **DuckDB** e **PostgreSQL**, além de validação rigorosa de schemas e regras de qualidade de dados.

> **`03` Applied AI & Search**
> Infraestrutura para inteligência artificial sem fricção. Arquiteturas **RAG**, processamento de documentos, busca vetorial avançada com **Qdrant** e orquestração de LLMs locais/serviços de knowledge-base.

> **`04` Operational Automation**
> Substituição de rotinas frágeis por software auditável. Motores de extração em **Python**, ingestão via SFTP, fluxos integrados (SAP, ClickUp, Grafana) e batch jobs via **Bash/PowerShell**.

<br>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&height=1&color=1E293B" width="60%"/>
</div>

<br>

## ⬢ Architecture DNA

O fluxo tático de como estruturo a transição de operações brutas para sistemas de decisão:

```mermaid
graph LR
    %% Minimalist Theme Configurations
    classDef core fill:transparent,stroke:#7C3AED,stroke-width:1px,color:#A78BFA
    classDef node fill:transparent,stroke:#334155,stroke-width:1px,color:#94A3B8
    classDef final fill:#7C3AED,stroke:none,color:#ffffff,font-weight:bold
    
    A[Raw Ops]:::node -->|ETL / dbt| B(Data Layer):::core
    D[Documents]:::node -->|Embeddings| E(Vector Store):::core
    
    B --> C{FastAPI Core}:::node
    E -->|RAG| C
    
    C -->|Automated Actions| F[Batch/Workers]:::node
    C -->|API/Insights| G[Decision Output]:::final
