from langgraph.graph import StateGraph

from app.agents.healthcare_agent import healthcare_agent

def build_agent_graph():
    graph = StateGraph(dict)

    graph.add_node("healthcare_agent", healthcare_agent)

    graph.set_entry_point("healthcare_agent")
    graph.set_finish_point("healthcare_agent")

    return graph.compile()