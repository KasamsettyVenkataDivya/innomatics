import streamlit as st
import google.generativeai as palm
import os

# Streamlit App Title
st.title("🤖 Gemini-2 AI Chatbot")

# API Key Input (User should provide their own key)
api_key="AIzaSyCgNwQLU0bY17ktDe5Fr9PaSK4-IrAI-Nw"

# User Input for prompt
user_input = st.text_area("Enter your prompt:")

if st.button("Generate Response"):
    if api_key and user_input:
        # Configure API key
        palm.configure(api_key=api_key)

        # Define System Prompt
        system_prompt = "you have to analyze the submitted code and identify potential bugs, errors and give corrected code ."

        # Initialize the Gemini Model
        model = palm.GenerativeModel(
            model_name="gemini-2.0-flash-thinking-exp",
            system_instruction=system_prompt
        )

        # Generate Response
        response = model.generate_content(user_input)

        # Display the output
        if response and hasattr(response, "text"):
            st.markdown(f"### ✨ AI Response:\n\n{response.text}")
        else:
            st.error("Failed to generate response. Please check your API key or try again.")

    else:
        st.warning("Please enter both API Key and a prompt!")

