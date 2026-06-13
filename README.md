<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=waving&height=240&color=0:020617,45:111827,100:7C3AED&text=Vin%C3%ADcius%20Reis&fontColor=F8FAFC&fontSize=56&fontAlignY=38&desc=Backend%20Engineering%20%7C%20Data%20Systems%20%7C%20Automation%20%7C%20AI%20Infrastructure&descSize=16&descAlignY=58&animation=fadeIn"
    alt="Vinícius Reis"
  />
</p>

<p align="center">
  <img
    src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=21&duration=2600&pause=900&color=A78BFA&center=true&vCenter=true&width=860&lines=I+design+backend+systems+for+real+operations.;I+turn+fragile+workflows+into+auditable+software.;I+build+data%2C+automation+and+AI+infrastructure."
    alt="Engineering Focus"
  />
</p>

<p align="center">
  <a href="mailto:viniciussport2004@gmail.com">
    <img src="https://img.shields.io/badge/email-020617?style=for-the-badge&logo=gmail&logoColor=EA4335" alt="Email"/>
  </a>
  <a href="https://www.linkedin.com/in/vin%C3%ADcius-gon%C3%A7alves-reis-4544a921a">
    <img src="https://img.shields.io/badge/linkedin-020617?style=for-the-badge&logo=linkedin&logoColor=0A66C2" alt="LinkedIn"/>
  </a>
  <a href="https://github.com/venysssssssssss">
    <img src="https://img.shields.io/badge/github-020617?style=for-the-badge&logo=github&logoColor=FFFFFF" alt="GitHub"/>
  </a>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=venysssssssssss&style=flat-square&color=7C3AED&label=profile+signal" alt="Profile views"/>
</p>

---

## ⚙️ Engineering Surface

<table>
  <tr>
    <td width="50%">
      <h3>Backend Systems</h3>
      <p>API-first services, FastAPI applications, service layers, async runners, control planes, validation contracts, and production-oriented interfaces.</p>
    </td>
    <td width="50%">
      <h3>Data Infrastructure</h3>
      <p>DuckDB pipelines, SQL modeling, dbt workflows, analytical datasets, schema validation, data quality rules, and materialized outputs.</p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>Automation</h3>
      <p>Python engines, SFTP ingestion, SAP-related flows, batch jobs, PowerShell/Bash tooling, and operational process replacement.</p>
    </td>
    <td width="50%">
      <h3>AI Systems</h3>
      <p>RAG architectures, Qdrant vector search, document processing, local LLM services, and knowledge-base engineering.</p>
    </td>
  </tr>
</table>

---

## 🧬 System Architecture DNA

```mermaid
flowchart LR
    subgraph Operations & Data
        A[Raw Sources] -->|Extraction| B[ETL/ELT Engine]
        B -->|Validation| C[(Analytical DB)]
        C --> D[dbt Models]
    end

    subgraph Intelligence & AI
        E[Documents] -->|Chunking| F[Embeddings]
        F --> G[(Vector DB)]
        G -->|RAG| H[LLM Node]
    end

    subgraph Service Layer
        D --> I[FastAPI Core]
        H --> I
        I -->|Automation| J[Batch Jobs]
        I -->|Endpoints| K[Decision Support]
    end
    
    style I fill:#020617,stroke:#7C3AED,stroke-width:2px,color:#fff
