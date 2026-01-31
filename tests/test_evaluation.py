import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.evaluation.report import evaluate

question = "What are the symptoms of type 2 diabetes?"
context = "Common symptoms include increased thirst, frequent urination, fatigue, blurred vision."
answer = "Symptoms include increased thirst, frequent urination, and fatigue."

metrics = evaluate(
    question=question,
    answer=answer,
    context=context,
    latency_ms=1200
)

print(metrics)