import chromadb
from chromadb.config import Settings


class VectorStore:
    def __init__(self):
        # ✅ Correct way in new Chroma versions
        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="healthcare_docs"
        )

    def add(self, texts, embeddings, metadatas):
        ids = [str(i) for i in range(len(texts))]
        self.collection.add(
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )