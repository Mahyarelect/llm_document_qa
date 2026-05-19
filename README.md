\# LLM Document QA System



A Retrieval-Augmented Generation (RAG) backend system built with Django, Django REST Framework, LangChain, and OpenRouter.



The system allows users to upload DOCX documents, extract text, retrieve relevant document chunks, and ask AI-powered questions about uploaded content.



\---



\## Features



\* Upload DOCX documents

\* Automatic text extraction

\* Automatic document chunking

\* Retrieval-based question answering

\* LLM integration using OpenRouter

\* Question history storage

\* REST API endpoints

\* Dockerized deployment

\* Django Admin interface



\---



\## Tech Stack



\### Backend



\* Django

\* Django REST Framework



\### AI / LLM



\* LangChain

\* OpenRouter



\### Retrieval



\* Custom keyword-based retrieval

\* Planned BM25 upgrade



\### Database



\* SQLite



\### Containerization



\* Docker

\* Docker Compose



\---



\## Project Architecture



```text

User

&#x20; ↓

Django REST API

&#x20; ↓

Retrieval Layer

&#x20; ↓

Prompt Construction

&#x20; ↓

LangChain

&#x20; ↓

OpenRouter LLM

&#x20; ↓

Generated Answer

&#x20; ↓

Question History Storage

```



\---



\## Project Structure



```text

llm\_document\_qa/

│

├── config/

├── documents/

├── screenshots/

├── sample\_data/

├── Dockerfile

├── docker-compose.yml

├── requirements.txt

├── README.md

├── API\_DOCUMENTATION.md

├── .gitignore

├── .dockerignore

├── manage.py

└── .env.example

```



\---



\## Installation



\### 1. Clone Repository



```bash

git clone https://github.com/Mahyarelect/llm\_document\_qa.git

cd llm\_document\_qa

```



\---



\### 2. Create Virtual Environment



```bash

python -m venv venv

```



Activate:



\#### Windows



```bash

venv\\Scripts\\activate

```



\#### Linux / Mac



```bash

source venv/bin/activate

```



\---



\### 3. Install Dependencies



```bash

pip install -r requirements.txt

```



\---



\## Environment Variables



Create `.env`:



```env

OPENROUTER\_API\_KEY=your\_api\_key\_here

OPENROUTER\_MODEL=openrouter/free

```



You can also copy from `.env.example`.



\---



\## Run Migrations



```bash

python manage.py makemigrations

python manage.py migrate

```



\---



\## Create Admin User



```bash

python manage.py createsuperuser

```



\---



\## Run Server



```bash

python manage.py runserver

```



Server:



```text

http://127.0.0.1:8000/

```



\---



\## Docker Setup



\### Build Docker Image



```bash

docker compose build --no-cache

```



\### Run Container



```bash

docker compose up

```



\### Run Migrations Inside Docker



```bash

docker compose exec web python manage.py migrate

```



\### Create Superuser Inside Docker



```bash

docker compose exec web python manage.py createsuperuser

```



\---



\## Admin Panel



Open:



```text

http://127.0.0.1:8000/admin/

```



Admin capabilities:



\* Upload documents

\* Inspect extracted text

\* Inspect chunks

\* View question history



\---



\## API Endpoints



\### Ask Question



Endpoint:



```text

POST /api/ask/

```



Request example:



```json

{

&#x20; "question": "What programming languages does Mahyar know?"

}

```



Response example:



```json

{

&#x20; "question": "What programming languages does Mahyar know?",

&#x20; "answer": "Java, Python, C, SQL",

&#x20; "context": "...",

&#x20; "history\_id": 1

}

```



\---



\### Question History



Endpoint:



```text

GET /api/history/

```



Returns all previous question-answer interactions.



\---



\## Retrieval Pipeline



Current retrieval process:



1\. User submits a question

2\. Question words are tokenized

3\. Document chunks are scored

4\. Top relevant chunks are selected

5\. Context is sent to the LLM

6\. LLM generates the final answer



\---



\## AI Pipeline



```text

Question

&#x20; ↓

Chunk Retrieval

&#x20; ↓

Prompt Construction

&#x20; ↓

LangChain

&#x20; ↓

OpenRouter API

&#x20; ↓

LLM Response

&#x20; ↓

JSON Response

```



\---



\## Document Processing Flow



```text

Upload DOCX

&#x20;   ↓

Extract Text

&#x20;   ↓

Save Full Text

&#x20;   ↓

Create Chunks

&#x20;   ↓

Store Chunks

&#x20;   ↓

Ready for QA

```



\---



\## Current Limitations



\* DOCX only

\* SQLite only

\* Basic keyword retrieval

\* No embeddings yet

\* No vector database yet

\* No authentication yet

\* No frontend UI



\---



\## Planned Improvements



\* BM25 retrieval

\* Inverted index

\* Semantic embeddings

\* Vector databases

\* PDF support

\* PostgreSQL

\* React frontend

\* Authentication

\* Swagger/OpenAPI docs



\---



\## Security Notes



Never upload:



\* `.env`

\* API keys

\* `venv/`

\* `db.sqlite3`



\---



\## Screenshots



Place screenshots inside:



```text

screenshots/

```



Recommended screenshots:



\* Admin login

\* Document upload

\* Chunk display

\* `/api/ask/`

\* `/api/history/`

\* Docker container running



\---



\## Sample Test Data



Place sample documents inside:



```text

sample\_data/

```



\---



\## Author



Mahyar Rezaeepoor



GitHub:



```text

https://github.com/Mahyarelect

```



