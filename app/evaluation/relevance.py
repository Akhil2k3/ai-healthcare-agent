from sklearn.metrics.pairwise import cosine_similarity
from app.rag.embeddings import EmbeddingModel


def relevance_score(question: str, context: str) -> float:
    embedder = EmbeddingModel()
    embeddings = embedder.embed([question, context])

    score = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return round(float(score), 2)