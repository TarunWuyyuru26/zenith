"""
State definition for LangGraph workflows.
Defines the structure of state passed between nodes in the graph.
"""
from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages

class State(TypedDict):
    """
    Represents the structure of the state used in the graph.
    
    Attributes:
        messages: List of messages with automatic message aggregation
    """
    messages: Annotated[list, add_messages]
