from transformers import pipeline
from app.agents.tools import retrieve_context

# Stable causal model (works with text-generation)
generator = pipeline(
    "text-generation",
    model="distilgpt2",
    max_new_tokens=150
)

def healthcare_agent(state: dict):
    question = state["question"]

    # Retrieve RAG context
    context_docs = retrieve_context(question)
    context = "\n".join(context_docs)

    prompt = f"""
You are a healthcare assistant.
Use ONLY the information below to answer.
If the answer is not present, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""

    result = generator(prompt)
    answer = result[0]["generated_text"]

    return {
        "answer": answer,
        "sources": context_docs
    }
