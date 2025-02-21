import streamlit as st
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain_experimental.agents import create_csv_agent
import matplotlib.pyplot as plt
import os

os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

# Load the CSV data
DATA_FILE = "simulated_outreach_demand_data.csv"

@st.cache_data
def load_data():
    """Load data from the CSV file."""
    return pd.read_csv(DATA_FILE)

# Initialize LLM and LangChain Agent
def initialize_agent(data_file):
    """Initialize the LangChain agent with a chat-based OpenAI model."""
    llm = ChatOpenAI(model="gpt-4", temperature=0)  # Use ChatOpenAI for chat models
    agent = create_csv_agent(llm, data_file, verbose=True, allow_dangerous_code=True)
    return agent

# Streamlit app
st.title("LLM-Powered Outreach and Demand Insights")

# Load data
data = load_data()
st.write("### Simulated Outreach and Demand Data")
st.dataframe(data)

# Initialize LangChain agent
if "agent" not in st.session_state:
    st.session_state.agent = initialize_agent(DATA_FILE)

st.write("### Ask Questions About the Data")
query = st.text_input("Enter your query (e.g., 'Which region had the highest demand last year?')")

if st.button("Get Insights"):
    if query:
        try:
            response = st.session_state.agent.run(query)
            st.write("### LLM Response")
            st.write(response)
        except Exception as e:
            st.error(f"Error generating response: {e}")
    else:
        st.warning("Please enter a query.")


