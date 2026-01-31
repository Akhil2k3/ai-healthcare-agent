import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.agents.graph import build_agent_graph

graph = build_agent_graph()

response = graph.invoke({
    "question": "What are the symptoms of type 2 diabetes?"
})

print(response)