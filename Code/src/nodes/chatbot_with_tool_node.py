"""
Chatbot node with tool integration.
Enhanced chatbot logic that can use external tools.
"""
from Code.src.state.state import State

class ChatbotWithToolNode:
    """
    Chatbot logic enhanced with tool integration.
    
    Attributes:
        llm: Language model instance with tool binding capabilities
    """
    
    def __init__(self, model):
        """
        Initialize chatbot with tool capabilities.
        
        Args:
            model: LLM model instance (e.g., ChatGroq)
        """
        self.llm = model

    def process(self, state: State) -> dict:
        """
        Processes the input state and generates a response with tool integration.
        
        Args:
            state: Current state containing messages
            
        Returns:
            dict: Updated state with new messages and tool responses
        """
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])

        # Simulate tool-specific logic
        tools_response = f"Tool integration for: '{user_input}'"

        return {"messages": [llm_response, tools_response]}

    def create_chatbot(self, tools):
        """
        Returns a chatbot node function with tools bound.
        
        Args:
            tools: List of tool instances to bind to the LLM
            
        Returns:
            function: Chatbot node function for graph integration
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            """
            Chatbot logic for processing the input state and returning a response.
            
            Args:
                state: Current state containing messages
                
            Returns:
                dict: Updated state with LLM response
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}

        return chatbot_node
