"""
Main application module for Zenith AI Assistant.
Integrates LangGraph workflows with Streamlit UI.
"""
import streamlit as st
from Code.ui.load_ui import LoadStreamlitUI
from Code.src.llms.groq_client import GroqLLM
from Code.src.graph.graph_builder import GraphBuilder
from Code.ui.display_result import DisplayResultStreamlit


def load_zenith_app():
    """
    Main application function that loads and runs the Zenith AI Assistant.
    
    This function:
    1. Initializes the UI and collects user input
    2. Configures the LLM model based on user selection
    3. Sets up the appropriate graph workflow
    4. Displays the results in the UI
    """
    # Load UI and get user controls
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return

    # Text input for user message
    user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            # Configure LLM
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()
            
            if not model:
                st.error("Error: LLM model could not be initialized.")
                return

            # Get selected use case
            usecase = user_input.get('selected_usecase')
            if not usecase:
                st.error("Error: No use case selected.")
                return

            # Build and compile graph
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                
                # Display results
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
                
            except Exception as e:
                st.error(f"Error: Graph setup failed - {e}")
                return

        except Exception as e:
            st.error(f"Error Occurred: {e}")
            raise


if __name__ == "__main__":
    load_zenith_app()
