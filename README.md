# 🧮 MathSolveX: Advanced Math Problem Solver

<div align="center">

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/langchain-0.1.0+-green.svg)](https://python.langchain.com/)
[![GROQ](https://img.shields.io/badge/groq-API-purple.svg)](https://groq.com/)
[![Made with ❤️](https://img.shields.io/badge/made%20with-%E2%9D%A4%EF%B8%8F-ff69b4.svg)](https://github.com/yourusername/mathsolvex)

<img src="https://i.imgur.com/example.png" alt="MathSolveX Logo" width="250"/>

**An elegant, AI-powered mathematics assistant that makes problem-solving a breeze.**

[Features](#-key-features) • [Demo](#-live-demo) • [Installation](#-installation) • [Usage](#-usage) • [Architecture](#-system-architecture) • [Contributing](#-contributing) • [License](#-license)

</div>

---

## 🌟 Introduction

MathSolveX is an intelligent, AI-powered mathematical problem-solving assistant built with Streamlit and LangChain. Designed for students, educators, and math enthusiasts, it provides detailed, step-by-step solutions to a wide range of mathematical problems - from basic arithmetic to complex calculus and beyond.

With its intuitive chat interface and sophisticated reasoning capabilities, MathSolveX brings the power of advanced AI to mathematical problem-solving, making it accessible to everyone.

## ✨ Key Features

- **🧠 Intelligent Problem Solving**
  - Handles arithmetic, algebra, calculus, statistics, and more
  - Provides step-by-step explanations with clear reasoning
  - Solves complex multi-step problems with precision

- **🔍 Multiple Solving Approaches**
  - Calculator tool for direct computations
  - Advanced reasoning tool for complex problem-solving
  - Wikipedia integration for context and background information

- **💎 Elegant User Experience**
  - Clean, dark-themed UI with professional styling
  - Intuitive chat-based interaction model
  - Interactive input with real-time responses
  - Responsive design with hover and focus effects

- **🔧 Technical Excellence**
  - Powered by Groq's Gemma2-9b-It model for fast, accurate responses
  - Modular architecture for maintainability and extensibility
  - Error handling for complex mathematical expressions
  - Secure API key management

## 🎮 Live Demo

*Coming soon! We're working on deploying a live demo of MathSolveX.*

## 📋 Requirements

- Python 3.8+
- Groq API key ([Get one here](https://console.groq.com/))
- Dependencies listed in `requirements.txt`

## 📥 Installation

### Option 1: Quick Install

```bash
# Clone the repository
git clone https://github.com/yourusername/mathsolvex.git
cd mathsolvex

# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Manual Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/mathsolvex.git
   cd mathsolvex
   ```

2. **Set up environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit langchain langchain-groq python-dotenv wikipedia numexpr
   ```

4. **Configure API keys**
   Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## 🚀 Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Enter your Groq API key** when prompted (or it will be loaded from your `.env` file)

3. **Start solving problems!**
   - Type your mathematical problem in the chat input
   - Get detailed, step-by-step solutions instantly
   - Follow the reasoning process to understand the solution

### Example Problems

MathSolveX can solve a wide variety of math problems, including:

- **Basic Math**: "Calculate the area of a circle with radius 5 cm"
- **Algebra**: "Solve for x: 2x + 5 = 17"
- **Calculus**: "Find the derivative of f(x) = x³ + 2x² - 5x + 3"
- **Statistics**: "What is the standard deviation of [4, 7, 9, 3, 8, 5]?"
- **Word Problems**: "If a train travels 120 miles in 2 hours, what is its speed in mph?"
- **Financial Math**: "Calculate the compound interest on $1000 at 5% annual rate for 3 years"

## 🏗️ System Architecture

MathSolveX is built with a modular architecture designed for maintainability and extensibility:

```
MathSolveX/
├── app.py                   # Application entry point
├── requirements.txt         # Project dependencies
├── .env                     # Environment variables (API keys)
├── src/
│   ├── __init__.py
│   ├── main.py              # Main application logic
│   ├── components/
│   │   ├── __init__.py
│   │   └── ui.py            # UI components and interactions
│   └── utils/
│       ├── __init__.py
│       ├── styling.py       # Custom styling for Streamlit
│       └── tools.py         # LangChain tools and agent setup
```

### Key Components:

- **LLM Integration**: Leverages Groq's Gemma2-9b-It model via the LangChain framework
- **Tool System**: Features specialized tools for mathematical calculations, reasoning, and information lookup
- **UI Framework**: Built on Streamlit for rapid development and elegant interfaces
- **Custom Styling**: Implements a dark-themed, professional UI with responsive design elements

## 🔧 Tools & Technologies

- **[Streamlit](https://streamlit.io/)**: For the interactive web interface
- **[LangChain](https://python.langchain.com/)**: For LLM orchestration and tools
- **[Groq API](https://groq.com/)**: For fast, powerful language model inference
- **[Wikipedia API](https://pypi.org/project/wikipedia/)**: For context and information lookup
- **[Python](https://www.python.org/)**: Core programming language

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add some amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

Please ensure your code follows our coding standards and includes appropriate tests.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- **[ExamProCo](https://github.com/ExamProCo)**: For the GenAI Course that inspired this project
- **[Groq](https://groq.com/)**: For providing the lightning-fast inference API
- **[LangChain](https://python.langchain.com/)**: For the powerful LLM framework
- **[Streamlit](https://streamlit.io/)**: For the elegant UI framework

---

<div align="center">
  <p>💖 Made with love by <a href="https://github.com/yourusername">Your Name</a></p>
  <p>⭐ Star this repository if you found it useful!</p>
</div>
