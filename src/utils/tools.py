"""
Module for setting up LangChain tools and agents.
"""

from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import AgentType, Tool, initialize_agent

def setup_llm(groq_api_key):
    """
    Initialize the language model.
    
    Args:
        groq_api_key (str): API key for Groq
        
    Returns:
        ChatGroq: Initialized language model
    """
    return ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

def setup_tools(llm):
    """
    Set up the various tools used by the agent.
    
    Args:
        llm: The language model to use
        
    Returns:
        tuple: (wikipedia_tool, math_tool, reasoning_tool)
    """
    # Wikipedia Tool
    wikipedia_wrapper = WikipediaAPIWrapper()
    wikipedia_tool = Tool(
        name="Wikipedia",
        func=wikipedia_wrapper.run,
        description="A tool for searching the Internet to find the various information on the things mentioned"
    )
    
    # Math Tool
    math_prompt = """
    You are a mathematical problem solver. Given a mathematical problem, please respond with ONLY the mathematical expression needed to solve it. 
    For example:
    Problem: What is 5 + 10?
    Response: 5 + 10

    Problem: If 3x + 5 = 20, what is x?
    Response: (20 - 5) / 3

    Do not include variable terms in the final expression. First solve for any variables symbolically, then substitute the values to create a pure numerical expression.
    If the problem requires complex mathematical reasoning with multiple steps, don't try to solve it in one expression. Instead, say "USE_REASONING_TOOL".

    Problem: {question}
    Response:
    """

    math_prompt_template = PromptTemplate(
        template=math_prompt,
        input_variables=["question"]
    )

    math_chain = LLMMathChain.from_llm(
        llm=llm,
        verbose=True,
        prompt=math_prompt_template
    )

    def math_tool_handler(input_str):
        """Custom handler for math tool to catch cases where reasoning is needed instead"""
        if "USE_REASONING_TOOL" in input_str:
            return "This problem requires complex reasoning. Please use the Reasoning Tool instead."
        try:
            return math_chain.run(input_str)
        except ValueError as e:
            # If the math chain fails, suggest using reasoning instead
            return f"Error processing mathematical expression. This may require complex reasoning instead. Original error: {str(e)}"

    math_tool = Tool(
        name="Math Calculator",
        func=math_tool_handler,
        description="A tool for solving mathematical expressions with numbers only. For complex word problems or equations with variables, use the Reasoning Tool instead."
    )

    # Reasoning Tool
    reasoning_prompt = """
    You are a helpful agent tasked with solving user's math problems and searching for information on the internet.
    When faced with a math problem, decide whether it's a:
    1. Simple calculation (use Math Calculator)
    2. Complex math problem requiring step-by-step reasoning (use Reasoning Tool)
    3. Information lookup problem (use Wikipedia)

    For calculations with pure numbers, prefer the Math Calculator.
    For problems with variables or multi-step problems, prefer the Reasoning Tool.
    For factual information, prefer Wikipedia.

    Logically arrive at the solution and provide a detailed explanation. 
    Display it pointwise for the question below
    Question:{question},
    Answer:
    """

    reasoning_prompt_template = PromptTemplate(
        input_variables=["question"],
        template=reasoning_prompt
    )

    llm_chain = LLMChain(
        llm=llm,
        prompt=reasoning_prompt_template
    )

    reasoning_tool = Tool(
        name="Reasoning Tool",
        func=llm_chain.run,
        description="A tool for answering logic-based and reasoning questions."
    )
    
    return wikipedia_tool, math_tool, reasoning_tool

def setup_agent(llm, tools):
    """
    Initialize the agent with the given tools.
    
    Args:
        llm: The language model to use
        tools: List of tools to provide to the agent
        
    Returns:
        Agent: Initialized agent
    """
    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=10
    )
