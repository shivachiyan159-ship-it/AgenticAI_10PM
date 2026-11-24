
from IPython.display import Image, display
from pydantic import BaseModel
from langgraph.graph import StateGraph, START, END


# State definition
class AgentState(BaseModel):
    message: str  # rajesh

# build Node


def greet_node(state: AgentState):
    """A node that generates a greeting message based on the input state."""
    state.message = "Hey" + state.message+"How are you doing ?"
    return state


# graph with state
graph = StateGraph(AgentState)

# node
graph.add_node("greeter", greet_node)


# edges
graph.add_edge(START, "greeter")
graph.add_edge("greeter", END)

# compile
app = graph.compile()

display(Image(app.get_graph().draw_mermaid_png()))
