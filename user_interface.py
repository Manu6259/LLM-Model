import streamlit as st
import pandas as pd
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain_experimental.agents import create_csv_agent
import os

# File path for donor data
DATA_FILE = "donor_data.csv"
os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

# Initialize LLM
llm = OpenAI(temperature=0)
agent = create_csv_agent(llm, DATA_FILE, verbose=False, allow_dangerous_code=True)

# Initialize row count
def initialize_row_count():
    try:
        donor_data = pd.read_csv(DATA_FILE)
        return len(donor_data)
    except FileNotFoundError:
        return 0

# Check for new rows
def check_for_new_rows(previous_row_count):
    try:
        donor_data = pd.read_csv(DATA_FILE)
        current_row_count = len(donor_data)
        
        # If new rows are added
        if current_row_count > previous_row_count:
            new_rows = donor_data.iloc[previous_row_count:]  # Get only new rows
            return new_rows, current_row_count
        else:
            return None, current_row_count
    except FileNotFoundError:
        return None, previous_row_count

def generate_thank_you_message(name, amount, impact):
    prompt = PromptTemplate(
        input_variables=["name", "amount", "impact"],
        template="""
        Write a thank-you email for a donor:
        Name: {name}
        Amount: ${amount}
        Impact: {impact}

        """,
    )
    # Generate the message from LLM
    generated_message = llm(prompt.format(name=name, amount=amount, impact=impact))
    return generated_message.strip()

# Streamlit app for user interface
st.title("User Interface - Donor Tracking")

# Tabs for different functionalities
tab1, tab2 = st.tabs(["Donor Tracking", "Query Donor Data"])

with tab1:
    # Initialize or load row count into session state
    if "row_count" not in st.session_state:
        st.session_state.row_count = initialize_row_count()

    # Display current donor data
    st.write("### Current Donor Data")
    try:
        current_data = pd.read_csv(DATA_FILE)
        st.write(current_data)
    except FileNotFoundError:
        st.warning("No donor data file found.")

    # Button to check for new donations
    if st.button("Refresh Donations"):
        new_rows, updated_row_count = check_for_new_rows(st.session_state.row_count)
        
        if new_rows is not None:
            st.write("### New Donations Detected!")
            st.write(new_rows)
            st.session_state.row_count = updated_row_count
        else:
            st.info("No new donations detected.")

    # Summary statistics
    if "row_count" in st.session_state and st.session_state.row_count > 0:
        st.write("### Summary Statistics")
        total_donations = current_data["Donation_Amount"].sum()
        total_donors = len(current_data["Email"].unique())
        avg_donation = current_data["Donation_Amount"].mean()
        
        st.write(f"**Total Donations Received:** ${total_donations:.2f}")
        st.write(f"**Total Unique Donors:** {total_donors}")
        st.write(f"**Average Donation Amount:** ${avg_donation:.2f}")

    # Section for message generation
    st.write("### Generate Thank-You Messages")

    if not current_data.empty:
        # Allow user to select a donor
        donor_name = st.selectbox("Select a donor", current_data["Donor_Name"])
        
        # Get donor details
        donor_details = current_data[current_data["Donor_Name"] == donor_name].iloc[0]
        donation_amount = donor_details["Donation_Amount"]
        impact_statement = f"{int(donation_amount / 5)} meals provided to families in need"  # Example impact calculation

        # Generate message
        if st.button("Generate Thank-You Message"):
            message = generate_thank_you_message(donor_name, donation_amount, impact_statement)
            st.text_area("Generated Message", value=message, height=200)

with tab2:
    # Querying Section
    st.write("### Query Donor Data")

    # Predefined questions
    st.write("#### Predefined Queries")
    queries = [
        "What is the total donation amount?",
        "Who are the top 5 donors?",
        "What is the average donation amount?",
    ]
    query_choice = st.selectbox("Select a predefined query", [""] + queries)

    if query_choice:
        st.write(f"**Query:** {query_choice}")
        response = agent.run(query_choice)
        st.write(f"**Result:** {response}")

    # Custom query input
    st.write("#### Custom Query")
    user_query = st.text_input("Ask your question about the donor data")
    if user_query:
        st.write(f"**Query:** {user_query}")
        response = agent.run(user_query)
        st.write(f"**Result:** {response}")
