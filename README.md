
# Enterprise Knowledge Assistant

An AI-powered Enterprise Knowledge Assistant built using **LangGraph**, **LangChain**, **Ollama**, **ChromaDB**, **FastAPI**, and **Streamlit**. The application enables users to query enterprise documents using natural language and provides accurate, context-aware responses with source citations through a Retrieval-Augmented Generation (RAG) pipeline.

---

## Features

- Intelligent document question answering
- Multi-agent architecture using LangGraph
- Retrieval-Augmented Generation (RAG)
- Metadata-aware document retrieval
- Source citations for every response
- Supports multiple document formats:
  - PDF
  - DOCX
  - PPTX
  - Excel (XLSX)
- FastAPI backend
- Streamlit web interface
- Local LLM inference using Ollama
- ChromaDB vector database

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | LangGraph |
| LLM Framework | LangChain |
| Large Language Model | Ollama (Llama 3.2) |
| Embedding Model | nomic-embed-text |
| Vector Database | ChromaDB |
| Backend API | FastAPI |
| Frontend | Streamlit |
| Programming Language | Python |

---

# Project Architecture

```text
                   +------------------------------------------------------+
|                      End User                        |
+-------------------------+----------------------------+
                          |
                          v
+------------------------------------------------------+
|                 Streamlit Dashboard                  |
|  - Chat Interface                                    |
|  - Source Viewer                                     |
|  - Query History                                     |
|  - Feedback (👍 / 👎)                                |
+-------------------------+----------------------------+
                          |
                          v
+------------------------------------------------------+
|                     FastAPI Layer                    |
|  - Authentication                                    |
|  - Request Validation                                |
|  - Rate Limiting                                     |
+-------------------------+----------------------------+
                          |
                          v
+------------------------------------------------------+
|               LangGraph Orchestrator                 |
+-------------------------+----------------------------+
                          |
         -------------------------------------------------------
         |            |            |            |              |
         v            v            v            v              v

 +---------------+ +-------------+ +------------+ +-----------+ +-------------+
 | Query         | | Retriever   | | Reasoning  | | Citation  | | Response    |
 | Analyzer      | | Agent       | | Agent      | | Agent     | | Formatter   |
 +-------+-------+ +------+------+ +------+-----+ +-----+-----+ +------+------+
         |                |                |             |              |
         |                v                |             |              |
         |      +--------------------+     |             |              |
         |      |  ChromaDB / FAISS  |     |             |              |
         |      | Vector Database    |     |             |              |
         |      +---------+----------+     |             |              |
         |                |                |             |              |
         |                v                |             |              |
         |      +--------------------+     |             |              |
         |      | Enterprise Docs    |     |             |              |
         |      | PDF / DOCX / KB    |     |             |              |
         |      +--------------------+     |             |              |
         |                                |             |              |
         --------------------------------------------------------------
                                          |
                                          v

                         +--------------------------------+
                         |      LLM (Azure OpenAI)        |
                         |    GPT-4o / GPT-5 / Claude     |
                         +---------------+----------------+
                                         |
                                         v

                         +--------------------------------+
                         |    Conversation Memory         |
                         |    Session Context Store       |
                         +---------------+----------------+
                                         |
                                         v

                         +--------------------------------+
                         |     Audit & Monitoring         |
                         |     Logs / Metrics / Cost      |
                         +---------------+----------------+
                                         |
                                         v

                         +--------------------------------+
                         | Final Answer + Citations       |
                         +--------------------------------+
                                        v
                              Final Response with Citations
```

---

# Multi-Agent Workflow

### Planner Agent

- Understands the user's question
- Identifies the query intent
- Determines the relevant document type
- Passes retrieval instructions to the Retriever Agent

### Retriever Agent

- Performs metadata-aware semantic search
- Retrieves relevant document chunks from ChromaDB
- Filters by document type when applicable

### Reasoning Agent

- Uses the retrieved context
- Generates accurate natural language responses
- Avoids hallucinations by relying on retrieved documents

### Citation Agent

- Adds source references
- Includes filename, page number, slide number, or row metadata when available

### Logger Agent

- Logs user queries
- Records retrieved sources
- Captures execution information for debugging

---

# Supported Documents

| Format | Retrieval Strategy |
|---------|--------------------|
| PDF | Page-based chunking |
| DOCX | Heading-based chunking |
| PPTX | Slide-wise retrieval |
| Excel | Row-wise retrieval with metadata |

---

# Project Structure

```
enterprise-knowledge-assistant/
│
├── agents/
│   ├── planner.py
│   ├── retriever.py
│   ├── reasoning.py
│   ├── citation.py
│   └── logger.py
│
├── ingestion/
│   ├── loader.py
│   └── build_index.py
│
├── database/
│   └── chroma_db/
│
├── documents/
│
├── frontend/
│
├── api.py
├── app.py
├── requirements.txt
└── README.md
```

---

# Retrieval Pipeline

```
User Question
      │
      ▼
Query Analyzer Agent
(Intent Detection,
Keyword Extraction)
      │
      ▼
Planner Agent
(Task Planning &
Routing Decision)
      │
      ▼
Retriever Agent
      │
      ▼
ChromaDB Vector Store
      │
      ▼
Relevant Documents
      │
      ▼
Context Validator Agent
(Relevance Filtering)
      │
      ▼
Reasoning Agent
(LLM Processing)
      │
      ▼
Response Formatter Agent
(Formatting & Cleanup)
      │
      ▼
Citation Agent
(Source Attribution)
      │
      ▼
Audit / Logger Agent
(Query Tracking)
      │
      ▼
Final Response
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/harshamalkar/enterprise-knowledge-assistant.git

cd enterprise-knowledge-assistant-ai
```

---

## Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env` file.

Example:

```env
OLLAMA_BASE_URL=your llm (I used OLLAMA)
LLM_MODEL=llama3.2:latest
EMBEDDING_MODEL=nomic-embed-text:latest
```

---

## Build the Vector Database

```bash
python ingestion/build_index.py
```

---

## Run FastAPI

```bash
uvicorn api:app --reload
```

---

## Run Streamlit

Open another terminal.

```bash
streamlit run app.py
```

---

# Example Queries

- Summarize the client presentation.
- Explain the Marketing Mart architecture.
- What is the Customer ID mapping?
- Which slide discusses system architecture?
- List the key findings from the report.
- Explain the business process described in the document.

---

# Future Enhancements

- Hybrid Search (Keyword + Semantic)
- Query Expansion
- Reranking Models
- Conversation Memory
- User Authentication
- Role-Based Access Control
- Document Upload from UI
- Cloud Deployment
- Multi-user Support
- Support for SharePoint and Google Drive

---


---



-----


 # Document
 
[Enterprise_Knowledge_Assistant_Capstone_Report.docx](https://github.com/user-attachments/files/30429792/Enterprise_Knowledge_Assistant_Capstone_Report.docx)

-----

# Author

Harsha M

GitHub:

https://github.com/harshamalkar

---

# License

This project is licensed under the MIT License.
