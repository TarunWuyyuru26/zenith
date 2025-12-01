"""
Groq LLM client implementation.
Provides interface to Groq's language models.
"""
import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    """
    Wrapper for Groq LLM integration.
    
    Attributes:
        user_controls_input: Dictionary containing API key and model selection
    """
    
    def __init__(self, user_controls_input: dict):
        """
        Initialize Groq LLM client.
        
        Args:
            user_controls_input: Dictionary with 'GROQ_API_KEY' and 'selected_groq_model'
        """
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        """
        Get configured Groq LLM model instance.
        
        Returns:
            ChatGroq: Configured Groq chat model
            
        Raises:
            ValueError: If API key is missing or configuration fails
        """
        try:
            groq_api_key = self.user_controls_input.get('GROQ_API_KEY', '')
            selected_groq_model = self.user_controls_input.get('selected_groq_model', 'mixtral-8x7b-32768')
            
            # Check for API key in input or environment
            if not groq_api_key and not os.environ.get("GROQ_API_KEY"):
                st.error("Please Enter the Groq API KEY")
                return None

            llm = ChatGroq(
                api_key=groq_api_key or os.environ.get("GROQ_API_KEY"),
                model=selected_groq_model
            )

        except Exception as e:
            raise ValueError(f"Error Occurred with Exception: {e}")
        
        return llm
