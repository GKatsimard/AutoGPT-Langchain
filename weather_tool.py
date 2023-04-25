# Import things that are needed generically
from langchain import LLMMathChain, SerpAPIWrapper
from langchain.agents import AgentType, Tool, initialize_agent, tool
from langchain.chat_models import ChatOpenAI
from langchain.tools import BaseTool
from weather_api import WeatherAPI

llm = ChatOpenAI(temperature=0)

from typing import Type

class CustomWeatherTool(BaseTool):
    name = "Weather Tool"
    description = "useful for when you need to answer questions about weather in a city"

    def _run(self, query: str) -> str:
        """Use the tool."""
        weather = WeatherAPI(
            api_key="b6907d289e10d714a6e88b30761fae22"
        )
        return weather.get_weather(query)
    
    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        weather = WeatherAPI(
            api_key="b6907d289e10d714a6e88b30761fae22"
        )
        raise weather.get_weather(query)