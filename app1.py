import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os

# Load API Key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Streamlit UI Configuration
st.title("AI Travel Assistant")

# User Inputs
source = st.text_input("Departure City")
destination = st.text_input("Destination City")
mode = st.selectbox("Preferred Mode", ["Any", "Flight", "Train", "Bus", "Cab"])
currency = st.selectbox("Currency", ["USD", "INR", "EUR", "GBP"])

# Function to fetch travel options
def get_travel_options(source, destination, mode, currency):
    prompt = [
        SystemMessage(content="You are a travel assistant providing travel options with estimated costs."),
        HumanMessage(content=f"Traveling from {source} to {destination} in {currency}. Mode: {mode}.")
    ]
    llm = ChatGoogleGenerativeAI(model="gemini-2.0", google_api_key=GOOGLE_API_KEY)
    return llm.invoke(prompt).content

# Fetch Travel Options
if st.button("Find Travel Options"):
    if source and destination:
        travel_info = get_travel_options(source, destination, mode, currency)
        st.write(travel_info)
    else:
        st.warning("Please enter both source and destination.")
