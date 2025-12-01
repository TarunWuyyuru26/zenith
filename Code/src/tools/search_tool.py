"""
Search tool implementation using Tavily.
Provides web search capabilities for the chatbot.
"""
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Return the list of tools to be used in the chatbot.
    
    Returns:
        list: List of tool instances (currently TavilySearchResults)
    """
    tools = [TavilySearchResults(max_results=2)]
    return tools

def create_tool_node(tools):
    """
    Creates and returns a tool node for the graph.
    
    Args:
        tools: List of tool instances
        
    Returns:
        ToolNode: LangGraph tool node for executing tools
    """
    return ToolNode(tools=tools)
