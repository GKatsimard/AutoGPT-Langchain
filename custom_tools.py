# Import things that are needed generically
from langchain import LLMMathChain, SerpAPIWrapper
from langchain.agents import AgentType, Tool, initialize_agent, tool
from langchain.chat_models import ChatOpenAI
from langchain.tools import BaseTool
import os
from apikeys import openai_api_key
from financial_tools import MACD_Calculator

os.environ["OPENAI_API_KEY"] = openai_api_key
llm = ChatOpenAI(temperature=0)

from typing import Type

class SearchAirBNB(BaseTool):
    name = "AirBNBSearch"
    description = "useful for when you need to find a place to stay in AirBNB"

    def _run(self, query: str) -> str:
        """Use the tool."""
        return print(f"Searching AirBNB for {query}")
    
    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        return print(f"Searching AirBNB asynchronously for {query}")
    
class SearchBooking(BaseTool):
    name = "BookingSearch"
    description = "useful for when you need to find a place to stay in Booking"

    def _run(self, query: str) -> str:
        """Use the tool."""
        return print(f"Searching Booking for {query}")
    
    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        return print(f"Searching Booking asynchronously for {query}")
    
tools = [SearchAirBNB(), SearchBooking(), MACD_Calculator()]

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run("I want to calculate MACD for AAPL")

