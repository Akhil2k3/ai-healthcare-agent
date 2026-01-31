from fastapi import FastAPI
from app.api.query import router as query_router

app = FastAPI(
    title="AI Healthcare Agent System",
    description="RAG-based Healthcare AI Agent with Evaluation Framework",
    version="1.0.0"
)

app.include_router(query_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}