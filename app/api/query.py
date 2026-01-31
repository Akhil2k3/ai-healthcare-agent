import time
from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.graph import build_agent_graph
from app.evaluation.report import evaluate

router = APIRouter()

graph = build_agent_graph()


class QueryRequest(BaseModel):
    question: str


@router.post("/query")
def query_agent(request: QueryRequest):
    start_time = time.time()

    result = graph.invoke({
        "question": request.question
    })

    latency_ms = int((time.time() - start_time) * 1000)

    context = " ".join(result.get("sources", []))
    answer = result.get("answer", "")

    metrics = evaluate(
        question=request.question,
        answer=answer,
        context=context,
        latency_ms=latency_ms
    )

    return {
        "question": request.question,
        "answer": answer,
        "sources": result.get("sources", []),
        "metrics": metrics
    }