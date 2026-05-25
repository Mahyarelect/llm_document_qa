import os
import re

from langchain_openai import ChatOpenAI
from rank_bm25 import BM25Okapi

from .models import DocumentChunk


def _get_llm():
    """Create LLM client lazily and print safe debug info."""
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    openrouter_model = os.getenv("OPENROUTER_MODEL")


    if not openrouter_model or not openrouter_api_key:
        return None

    try:
        client = ChatOpenAI(
            model=openrouter_model,
            api_key=openrouter_api_key,
            base_url="https://openrouter.ai/api/v1",
        )

        return client
    except Exception as e:
        return None


def tokenize(text):
    """Convert text into lowercase tokens used by BM25 retrieval."""
    return re.findall(r"\b\w+\b", text.lower())


def retrieve_relevant_chunks_simple(question, limit=3):
    chunks = DocumentChunk.objects.all()
    scored_chunks = []

    question_words = question.lower().split()

    for chunk in chunks:
        score = 0
        content_lower = chunk.content.lower()

        for word in question_words:
            if word in content_lower:
                score += 1

        if score > 0:
            scored_chunks.append((score, chunk))

    scored_chunks.sort(reverse=True, key=lambda x: x[0])
    return [chunk for score, chunk in scored_chunks[:limit]]


def retrieve_relevant_chunks_bm25(question, limit=3):
    chunks = list(DocumentChunk.objects.all())
    if not chunks:
        return []

    tokenized_chunks = [tokenize(c.content) for c in chunks]
    bm25 = BM25Okapi(tokenized_chunks)

    tokenized_question = tokenize(question)
    scores = bm25.get_scores(tokenized_question)

    scored_chunks = list(zip(scores, chunks))
    scored_chunks.sort(key=lambda x: x[0], reverse=True)

    return [chunk for score, chunk in scored_chunks[:limit]]


def retrieve_relevant_chunks(question, search_method="simple", limit=3):
    if search_method == "bm25":
        return retrieve_relevant_chunks_bm25(question=question, limit=limit)

    return retrieve_relevant_chunks_simple(question=question, limit=limit)


def generate_answer(question, search_method="simple"):
    relevant_chunks = retrieve_relevant_chunks(
        question=question,
        search_method=search_method,
        limit=3,
    )

    context = "\n\n".join([chunk.content for chunk in relevant_chunks])

    if not context:
        return {
            "answer": "I could not find relevant information in the uploaded documents.",
            "context": "",
            "search_method": search_method,
        }

    llm = _get_llm()
    if llm is None:
        return {
            "answer": "LLM service error: OPENROUTER_API_KEY and OPENROUTER_MODEL must be set.",
            "context": context,
            "search_method": search_method,
        }

    prompt = f"""
Answer the question using ONLY the provided context.

If the answer is not in the context, say:
"I could not find the answer in the uploaded documents."

Retrieval method:
{search_method}

Context:
{context}

Question:
{question}
"""

    try:
        response = llm.invoke(prompt)
        answer = response.content
    except Exception as e:
        answer = f"LLM service error: {str(e)}"

    return {
        "answer": answer,
        "context": context,
        "search_method": search_method,
    }