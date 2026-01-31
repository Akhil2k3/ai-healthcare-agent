from app.rag.embeddings import EmbeddingModel
from app.rag.vector_store import VectorStore

embedder = EmbeddingModel()
vector_store = VectorStore()

def retrieve_context(query: str):
    """
    Tool: Retrieve relevant healthcare context using RAG
    """
    query_embedding = embedder.embed([query])[0]
    results = vector_store.collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    return results["documents"][0]