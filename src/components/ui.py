"""
Module for handling UI components and interactions.
"""

import streamlit as st
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler

def initialize_session_state():
    """
    Initialize Streamlit session state if needed.
    """
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role":"assistant", "content":"Hi, I'm here to help you with your math problems and search for information on the internet."}
        ]

def setup_ui():
    """
    Set up the base Streamlit UI components.
    
    Returns:
        str or None: User input if provided, None otherwise
    """
    # App configuration
    st.set_page_config(page_title="MathSolveX - Advanced Math Problem Solver", page_icon="🧮", layout="centered")
    st.title("MathSolveX - Advanced Math Problem Solver")
    
    # Get API key input
    groq_api_key = st.text_input(label="Enter your Groq API Key", type="password")
    
    if not groq_api_key:
        st.info("Please add your Groq API Key to continue")
        return None, None
    
    return groq_api_key

def display_chat_history():
    """
    Display the chat history from session state.
    """
    for msg in st.session_state["messages"]:
        role = msg["role"]
        with st.chat_message(role):
            st.markdown(f"<div class='chat-message {role}'>", unsafe_allow_html=True)
            st.write(msg["content"])
            st.markdown("</div>", unsafe_allow_html=True)

def get_user_input():
    """
    Get user input from the chat input.
    
    Returns:
        str or None: User input if provided, None otherwise
    """
    return st.chat_input("Enter your question here...")

def handle_response(agent, question):
    """
    Handle the user question and generate a response using the agent.
    
    Args:
        agent: LangChain agent to use for generating responses
        question (str): User's question
    """
    with st.spinner("Generating Response..."):
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(f"<div class='chat-message user'>", unsafe_allow_html=True)
            st.write(question)
            st.markdown("</div>", unsafe_allow_html=True)

        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=True)
        response = agent.run(st.session_state.messages, callbacks=[st_cb])

        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(f"<div class='chat-message assistant'>", unsafe_allow_html=True)
            st.write(response)
            st.markdown("</div>", unsafe_allow_html=True)
