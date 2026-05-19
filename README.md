# LLM Document QA System

A Retrieval-Augmented Generation (RAG) backend system built with Django, Django REST Framework, LangChain, and OpenRouter.

The system allows users to upload DOCX documents, extract text, retrieve relevant document chunks, and ask AI-powered questions about uploaded content.

---

# Features

- Upload DOCX documents
- Automatic text extraction
- Automatic document chunking
- Retrieval-based question answering
- LLM integration using OpenRouter
- Question history storage
- REST API endpoints
- Dockerized deployment
- Django Admin interface

---

# Tech Stack

## Backend

- Django
- Django REST Framework

## AI / LLM

- LangChain
- OpenRouter

## Retrieval

- Custom keyword-based retrieval
- Planned BM25 upgrade

## Database

- SQLite

## Containerization

- Docker
- Docker Compose

---

# Project Architecture

```text
User
  ↓
Django REST API
  ↓
Retrieval Layer
  ↓
Prompt Construction
  ↓
LangChain
  ↓
OpenRouter LLM
  ↓
Generated Answer
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Mahyarelect/llm_document_qa.git
cd llm_document_qa
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env`

```env
OPENROUTER_API_KEY=your_api_key
OPENROUTER_MODEL=openrouter/free
```

---

# Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# Create Superuser

```bash
python manage.py createsuperuser
```

---

# Run Development Server

```bash
python manage.py runserver
```

Server URL:

```text
http://127.0.0.1:8000/
```

---

# Docker Setup

## Build Docker Image

```bash
docker compose build --no-cache
```

## Run Container

```bash
docker compose up
```

## Run Migrations Inside Docker

```bash
docker compose exec web python manage.py migrate
```

## Create Superuser Inside Docker

```bash
docker compose exec web python manage.py createsuperuser
```

---

# API Endpoints

## Ask Question

```text
POST /api/ask/
```

### Request

```json
{
  "question": "What programming languages does Mahyar know?"
}
```

### Response

```json
{
  "question": "What programming languages does Mahyar know?",
  "answer": "Java, Python, C, SQL",
  "context": "...",
  "history_id": 1
}
```

---

## Question History

```text
GET /api/history/
```

---

# Retrieval Pipeline

1. User submits question
2. Question is tokenized
3. Relevant chunks are scored
4. Top chunks selected
5. Prompt generated
6. LLM produces answer
7. History stored

---

# Current Limitations

- DOCX only
- SQLite only
- Basic keyword retrieval
- No embeddings
- No vector database
- No frontend
- No authentication

---

# Future Improvements

- BM25 retrieval
- Inverted index
- Embedding search
- ChromaDB / FAISS
- PostgreSQL
- PDF support
- React frontend
- JWT authentication

---

# Security Notes

Never upload:

- `.env`
- API keys
- `venv/`
- `db.sqlite3`

---

# Author

Mahyar Rezaeepoor

GitHub:

```text
https://github.com/Mahyarelect
```