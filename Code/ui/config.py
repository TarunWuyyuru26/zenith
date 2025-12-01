"""
UI Configuration module.
Manages UI settings and options from configuration file.
"""
from configparser import ConfigParser
import os

class Config:
    """
    Configuration manager for Streamlit UI settings.
    
    Attributes:
        config: ConfigParser instance containing settings
    """
    
    def __init__(self, config_file=None):
        """
        Initialize configuration.
        
        Args:
            config_file: Path to configuration INI file (optional)
        """
        self.config = ConfigParser()
        if config_file is None:
            config_file = os.path.join(os.path.dirname(__file__), "config.ini")
        self.config.read(config_file)

    def get_llm_options(self):
        """Get available LLM provider options."""
        return self.config["DEFAULT"].get("LLM_OPTIONS", "Groq").split(", ")
    
    def get_usecase_options(self):
        """Get available use case options."""
        return self.config["DEFAULT"].get(
            "USECASE_OPTIONS", 
            "Basic Chatbot, Chatbot with Tool"
        ).split(", ")

    def get_groq_model_options(self):
        """Get available Groq model options."""
        return self.config["DEFAULT"].get(
            "GROQ_MODEL_OPTIONS",
            "mixtral-8x7b-32768, llama-3.1-70b-versatile, llama-3.3-70b-versatile"
        ).split(", ")

    def get_page_title(self):
        """Get application page title."""
        return self.config["DEFAULT"].get("PAGE_TITLE", "Zenith AI Assistant")
