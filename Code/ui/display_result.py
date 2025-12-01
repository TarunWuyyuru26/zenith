"""
Display result module for Streamlit UI.
Handles rendering of graph execution results.
"""
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage


class DisplayResultStreamlit:
    """
    Manages display of graph execution results in Streamlit UI.
    
    Attributes:
        usecase: Selected use case name
        graph: Compiled LangGraph workflow
        user_message: User input message
    """
    
    def __init__(self, usecase, graph, user_message):
        """
        Initialize display handler.
        
        Args:
            usecase: Name of the selected use case
            graph: Compiled LangGraph workflow
            user_message: User input message string
        """
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        """
        Display graph execution results based on use case.
        """
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        if usecase == "Basic Chatbot":
            # Stream basic chatbot responses
            for event in graph.stream({'messages': ("user", user_message)}):
                for value in event.values():
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        st.write(value["messages"].content)

        elif usecase == "Chatbot with Tool":
            # Invoke graph with tool support
            initial_state = {"messages": [user_message]}
            res = graph.invoke(initial_state)
            
            for message in res['messages']:
                if type(message) == HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message) == ToolMessage:
                    with st.chat_message("ai"):
                        st.write("🔧 Tool Call Start")
                        st.write(message.content)
                        st.write("🔧 Tool Call End")
                elif type(message) == AIMessage and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)
