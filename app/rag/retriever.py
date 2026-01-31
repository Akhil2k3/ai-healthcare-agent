def retrieve(query_embedding, vector_store, top_k=3):
    results = vector_store.collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    return results["documents"][0]