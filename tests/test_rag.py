import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.rag.loader import load_documents
from app.rag.chunker import chunk_text
from app.rag.embeddings import EmbeddingModel
from app.rag.vector_store import VectorStore

docs = load_documents("data/raw")
chunks = chunk_text(docs[0]["text"])

embedder = EmbeddingModel()
embeddings = embedder.embed(chunks)

store = VectorStore()
store.add(
    texts=chunks,
    embeddings=embeddings,
    metadatas=[{"source": docs[0]["source"]}] * len(chunks)
)

print("RAG ingestion successful ✅")