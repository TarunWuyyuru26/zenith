"""
Basic chatbot node implementation.
Simple chatbot logic without tool integration.
"""
from Code.src.state.state import State

class BasicChatbotNode:
    """
    Basic chatbot logic implementation.
    
    Attributes:
        llm: Language model instance for generating responses
    """
    
    def __init__(self, model):
        """
        Initialize basic chatbot node.
        
        Args:
            model: LLM model instance (e.g., ChatGroq)
        """
        self.llm = model

    def process(self, state: State) -> dict:
        """
        Processes the input state and generates a chatbot response.
        
        Args:
            state: Current state containing messages
            
        Returns:
            dict: Updated state with new message
        """
        return {"messages": self.llm.invoke(state['messages'])}
