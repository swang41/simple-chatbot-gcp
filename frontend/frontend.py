import streamlit as st  
import requests  

# Replace with your Cloud Run backend URL
BACKEND_URL = "https://simple-chatbot-gcp-1031374583793.us-central1.run.app/chat"

st.title("LLM Chatbot")
user_input = st.text_input("Ask me anything:")

if user_input:
    try:
        response = requests.post(
            BACKEND_URL,
            json={"prompt": user_input}
        )
        if response.status_code == 200:
            st.write("**Response:**")
            st.write(response.json()["response"])
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Failed to connect to the backend: {str(e)}")