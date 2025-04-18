"""
MathSolveX - Advanced Math Problem Solver
Main application entry point
"""

import streamlit as st
import os
import sys

# Add the parent directory to the path to make imports work
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Page config must come first before any other Streamlit commands
st.set_page_config(page_title="MathSolveX - Advanced Math Problem Solver", page_icon="🧮", layout="centered")

# Import modules using absolute imports
from src.components.ui import initialize_session_state, display_chat_history, get_user_input, handle_response
from src.utils.styling import apply_styling
from src.utils.tools import setup_llm, setup_tools, setup_agent

def main():
    """
    Main application function.
    """
    # Apply custom styling
    apply_styling()
    
    # Create a container for the header that will always be visible
    header_container = st.container()
    
    # Display the app title and header in the dedicated container
    with header_container:
        st.title("MathSolveX - Advanced Math Problem Solver")
        st.markdown("---")
    
    # Initialize session state
    initialize_session_state()
    
    # Get API key input from UI
    groq_api_key = st.text_input(label="Enter your Groq API Key", type="password")
    
    if not groq_api_key:
        st.info("Please add your Groq API Key to continue")
        return
    
    # Create a container for the chat interface
    chat_container = st.container()
    
    # Set up the language model
    llm = setup_llm(groq_api_key)
    
    # Set up the tools
    wikipedia_tool, math_tool, reasoning_tool = setup_tools(llm)
    
    # Set up the agent
    agent = setup_agent(llm, [wikipedia_tool, math_tool, reasoning_tool])
    
    # Display chat history within the chat container
    with chat_container:
        display_chat_history()
        
        # Get user input
        question = get_user_input()
        
        # Process user input if provided
        if question:
            handle_response(agent, question)

if __name__ == "__main__":
    main()
