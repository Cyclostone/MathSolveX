"""
MathSolveX - Advanced Math Problem Solver
Main application launcher
"""

# Import necessary modules
import sys
import os
import streamlit as st

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the main function from src.main
from src.main import main

if __name__ == "__main__":
    # Load environment variables from .env file if it exists
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass
    
    # Run the main application
    main()
