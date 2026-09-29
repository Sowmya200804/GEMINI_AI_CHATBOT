
import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

# Load API key from .env file
load_dotenv()

# Page settings
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Load CSS safely
try:
    with open("style.css", "r", encoding="utf-8") as file:
        css = file.read()

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )
except FileNotFoundError:
    st.warning("style.css not found. Keep it beside app.py.")

# Chatbot heading
st.title("✨ Gemini AI Chatbot")
st.write("Your creative AI assistant — ask anything!")

st.divider()

# Prompt input
prompt = st.text_area(
    "💬 Enter your prompt:",
    placeholder="Example: Explain Artificial Intelligence in simple words",
    height=150
)

# Generate response
if st.button("🚀 Generate Response"):
    if not prompt.strip():
        st.warning("Please enter a prompt first.")

    else:
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            st.error(
                "API key is missing. Add GEMINI_API_KEY "
                "to your .env file."
            )

        else:
            try:
                client = genai.Client(api_key=api_key)

                with st.spinner("🤖 Gemini is thinking..."):
                    response = client.models.generate_content(
                        model="gemini-3.1-flash-lite",
                        contents=prompt
                    )

                if response.text:
                    st.success("Response generated successfully!")
                    st.subheader("💡 Gemini's Answer")
                    st.markdown(response.text)
                else:
                    st.warning("Gemini returned an empty response.")

            except Exception as e:
                st.error(f"Something went wrong: {e}")