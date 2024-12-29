from phi.agent import Agent                    # type: ignore # required to create an agent
from phi.model.groq import Groq                # required for model selection from Groq
from phi.tools.yfinance import YFinanceTools   # type: ignore # required tool for latest financial news 
from dotenv import load_dotenv                 # required import for API key
import streamlit as st
from typing import Iterator
from phi.agent import Agent, RunResponse # type: ignore
from phi.utils.pprint import pprint_run_response

st.title("Finance Page")

## API Key setup
load_dotenv()

## Finance Agent setup
agent = Agent(

    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],   # these tools can be multiple that's its an array
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables and charts to display the data"]
)

response_stream: Iterator[RunResponse] = agent.run("Summarise and compare analyst recommendations and fundaments for Tesla and Nvidia", stream=True)
st.markdown(pprint_run_response(response_stream, markdown=True, show_time=True))

