"""
Module for styling the Streamlit app.
"""

import streamlit as st

def apply_styling():
    """
    Apply custom CSS styling to the Streamlit app.
    """
    st.markdown("""
    <style>
        .stApp {
            background-color: #2c3e50;
            font-family: 'Segoe UI', sans-serif;
            color: white;
        }
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        /* Make all text elements white */
        p, h1, h2, h3, h4, h5, h6, li, span, label {
            color: white !important;
        }
        /* Title and headers */
        .stTitleBlock {
            color: white !important;
        }
        h1, h2, h3 {
            color: white !important;
        }
        /* Input styling */
        .stTextInput > div > div > input {
            border-radius: 8px;
            border: 2px solid #af504c;
            padding: 12px;
            font-size: 16px;
            color: white !important;
            background-color: rgba(0, 0, 0, 0.2);
        }
        /* Button styling */
        .stButton > button {
            background-color: #af504c;
            color: white;
            border-radius: 8px;
            padding: 12px 24px;
            font-weight: 600;
            border: none;
            transition: background-color 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #45a049;
            border: none;
        }
        /* Chat message styling */
        .chat-message {
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 12px;
            max-width: 85%;
            font-size: 15px;
            line-height: 1.5;
        }
        .chat-message.user {
            background-color: #2196F3;
            color: white;
            margin-left: auto;
            border: 1px solid #1976D2;
        }
        .chat-message.assistant {
            background-color: rgba(0, 0, 0, 0.6);
            color: white;
            margin-right: auto;
            border: 1px solid #555555;
            box-shadow: 0 1px 3px rgba(0,0,0,0.3);
        }
        /* Streamlit default elements */
        .st-bv, .st-bw, .st-bx, .st-by {
            color: white !important;
        }
        /* Streamlit markdown */
        .st-ae, .st-af, .st-ag, .st-ah, .st-ai, .st-aj {
            color: white !important;
        }
        /* Other elements */
        div[data-testid="stMarkdownContainer"] > p {
            color: white !important;
        }
        /* Labels and small text */
        .css-1aehpvj, .css-1bdvguh {
            color: white !important;
        }
        /* Make sure text inputs and text areas have white text */
        textarea, input {
            color: white !important;
        }
        /* Chat input */
        .stChatInput {
            background-color: rgba(255, 255, 255, 0.15);
            color: white !important;
            border-radius: 12px !important;
            border: 2px solid #af504c !important;
            padding: 12px !important;
            font-size: 16px !important;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            margin-top: 20px !important;
            transition: all 0.3s ease;
        }
        
        .stChatInput:focus-within,
        .stChatInput:hover {
            background-color: rgba(255, 255, 255, 0.25);
            border-color: #ff6b66 !important;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.4);
            transform: translateY(-2px);
        }
        
        .stChatInput > div {
            width: 100% !important;
        }
        
        .stChatInput textarea {
            color: white !important;
            caret-color: white !important;
            font-size: 16px !important;
        }
        
        /* The chat input button */
        .stChatInput button {
            background-color: #af504c !important;
            border-color: #af504c !important;
            color: white !important;
            border-radius: 50% !important;
            width: 40px !important;
            height: 40px !important;
            transition: all 0.3s ease;
        }
        
        .stChatInput button:hover {
            background-color: #ff6b66 !important;
            transform: scale(1.1);
        }
    </style>
    """, unsafe_allow_html=True)
