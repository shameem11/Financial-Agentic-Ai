
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
import streamlit as st

# web search 


from dotenv import load_dotenv
import os

st.header('Financial Agent')
st.write("This app provides financial data and web search results using AI agents.")

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

# Financial Agent

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True,
                         analyst_recommendations=True,
                         company_info=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)


agent_team = Agent(
    model = Groq(id="llama-3.3-70b-versatile"),
    team=[web_agent, finance_agent],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)


user_query = st.text_input(
    "Enter your query:",
    placeholder="Summarize analyst recommendations and share the latest news for..."
)

if st.button("Get Response"):
    if user_query:
        with st.spinner("Processing your query..."):
            # Get the agent's response
            response = agent_team.print_response(user_query, stream=True)
            # Display the response in Streamlit
            st.write(response)
            print(f"Type of response: {type(response)}")
            print(f"Value of response: {response}")
    else:
        st.warning("Please enter a query.")

