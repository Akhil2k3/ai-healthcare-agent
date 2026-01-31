import time

from app.evaluation.relevance import relevance_score
from app.evaluation.faithfulness import faithfulness_score
from app.evaluation.confidence import confidence_score


def evaluate(question, answer, context, latency_ms):
    return {
        "relevance": relevance_score(question, context),
        "faithfulness": faithfulness_score(answer, context),
        "confidence": confidence_score(answer, context),
        "latency_ms": latency_ms
    }