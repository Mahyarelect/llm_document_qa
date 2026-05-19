import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from .models import DocumentChunk


load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL")


llm = ChatOpenAI(
    model=OPENROUTER_MODEL,
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)


def retrieve_relevant_chunks(question, limit=3):
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


def generate_answer(question):
    relevant_chunks = retrieve_relevant_chunks(question)

    context = "\n\n".join(
        [chunk.content for chunk in relevant_chunks]
    )

    prompt = f"""
Answer the question using ONLY the provided context.

If the answer is not in the context, say:
"I could not find the answer in the uploaded documents."

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
    }