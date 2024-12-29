from phi.agent import Agent   # type: ignore
from phi.model.groq import Groq     #type: ignore
from phi.tools.duckduckgo import DuckDuckGo     # type:ignore
from phi.tools.yfinance import YFinanceTools   # type:ignore
from dotenv import load_dotenv

load_dotenv()

web_agent = Agent(

    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["always include sources"],
    markdown=True,
    show_tool_calls=True
)


finance_agent = Agent(

    name="Finance Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions="use tables/charts to display the data",
    markdown=True,
    show_tool_calls=True
)


agent_team = Agent(

    team=[web_agent, finance_agent],
    instructions=["always include sources", "use tables to display the data"],
    model=Groq(id="llama-3.3-70b-versatile"),
    markdown=True,
    show_tool_calls=True
)

agent_team.print_response("summarize analyst recommendations and share the latest news for NVDA", stream=True)