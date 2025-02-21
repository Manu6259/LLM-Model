import streamlit as st
import pandas as pd
import uuid
from datetime import datetime

# File path for donor data
DATA_FILE = "donor_data.csv"

# Function to load existing data or create a new file
def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Donor_ID", "Name", "Email", "Donation_Amount", "Donation_Date", "Payment_Method", "Notes"])

# Function to save new data to the file
def save_data(data, file_path):
    data.to_csv(file_path, index=False)

# Streamlit app for donor interface
st.title("😀🫂 LCA Donor Page")

# Donor submission form
with st.form("donor_form", clear_on_submit=True):
    name = st.text_input("Name", max_chars=50)
    email = st.text_input("Email", max_chars=50)
    donation_amount = st.number_input("Donation Amount (in USD)", min_value=1.0, step=0.1)
    donation_date = st.date_input("Donation Date", value=datetime.today())
    payment_method = st.selectbox("Payment Method", ["Online", "Bank Transfer", "Cash"])
    
    
    submitted = st.form_submit_button("Submit Donation")

# Handle form submission
if submitted:
    # Generate a unique Donor_ID
    donor_id = str(uuid.uuid4())
    
    # Load existing data
    donor_data = load_data(DATA_FILE)
    
    # Check for repeat donors
    if ((donor_data["Donor_Name"] == name) & (donor_data["Email"] == email)).any():
        st.info(f"Welcome back, {name}! Thank you for your continued support!")
    else:
        st.success(f"Thank you, {name}, for your generous donation of ${donation_amount:.2f}!")

    # Add new donation record
    new_record = {
        "Donor_ID": donor_id,
        "Donor_Name": name,
        "Email": email,
        "Donation_Amount": donation_amount,
        "Donation_Date": donation_date,
        "Payment_Method": payment_method,
    }
    donor_data = pd.concat([donor_data, pd.DataFrame([new_record])], ignore_index=True)
    
    # Save updated data
    save_data(donor_data, DATA_FILE)

    # Display confirmation
    st.write("Your donation has been successfully recorded.")


