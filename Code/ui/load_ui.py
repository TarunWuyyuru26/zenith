"""
Streamlit UI loader module.
Manages UI components, user controls, and configuration.
"""
import streamlit as st
import os
from Code.ui.config import Config


class LoadStreamlitUI:
    """
    Manages Streamlit UI loading and user control collection.
    
    Attributes:
        config: Configuration instance
        user_controls: Dictionary storing user input values
    """
    
    def __init__(self):
        """Initialize UI loader with configuration."""
        self.config = Config()
        self.user_controls = {}

    def initialize_session(self):
        """
        Initialize session state variables.
        
        Returns:
            dict: Default session state values
        """
        return {
            "messages": [],
            "current_mode": "chat"
        }

    def load_streamlit_ui(self):
        """
        Load and configure the Streamlit UI.
        
        Returns:
            dict: User control values (API keys, model selection, etc.)
        """
        st.set_page_config(
            page_title="🤖 " + self.config.get_page_title(),
            layout="wide"
        )
        st.header("🤖 " + self.config.get_page_title())

        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                # Model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox(
                    "Select Model", 
                    model_options
                )
                
                # API key input
                self.user_controls["GROQ_API_KEY"] = st.text_input(
                    "Groq API Key",
                    type="password",
                    help="Get your API key from https://console.groq.com/keys"
                )
                
                # Validate API key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed.")
            
            st.markdown("---")
            
            # Use case selection
            self.user_controls["selected_usecase"] = st.selectbox(
                "Select Use Case", 
                usecase_options
            )

            # Show TAVILY API key input for tool-based chatbot
            if self.user_controls["selected_usecase"] == "Chatbot with Tool":
                st.markdown("---")
                self.user_controls["TAVILY_API_KEY"] = st.text_input(
                    "Tavily API Key",
                    type="password",
                    help="Get your API key from https://app.tavily.com/home"
                )
                
                # Set environment variable for Tavily
                if self.user_controls["TAVILY_API_KEY"]:
                    os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"]
                
                # Validate API key
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("⚠️ Please enter your TAVILY API key to use tools.")
            
            st.markdown("---")
            st.caption("Built with LangGraph & Streamlit")
        
        # Initialize session state
        if "state" not in st.session_state:
            st.session_state.state = self.initialize_session()

        return self.user_controls
