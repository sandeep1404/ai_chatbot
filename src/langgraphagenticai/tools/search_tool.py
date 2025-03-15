from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode


## create a new search tool if u want to add more tools u can add them in tools [] list

def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """
    tools=[TavilySearchResults(max_results=2)]
    return tools

def create_tool_node(tools):
    """
    creates and returns a tool node for the graph
    """
    return ToolNode(tools=tools)