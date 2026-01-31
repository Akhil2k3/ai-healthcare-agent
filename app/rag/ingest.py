import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.rag.loader import load_documents
from app.rag.chunker import chunk_text
from app.rag.embeddings import EmbeddingModel
from app.rag.vector_store import VectorStore


def ingest():
    docs = load_documents("data/raw")

    embedder = EmbeddingModel()
    store = VectorStore()

    for doc in docs:
        chunks = chunk_text(doc["text"])
        embeddings = embedder.embed(chunks)

        store.add(
            texts=chunks,
            embeddings=embeddings,
            metadatas=[{"source": doc["source"]}] * len(chunks)
        )

    print("RAG ingestion completed and stored ✅")


if __name__ == "__main__":
    ingest()
