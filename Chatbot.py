import streamlit as st
from google import genai

# 1. Page Configuration
st.set_page_config(page_title="Simple AI Chatbot", page_icon="🤖")
st.title("🤖 Simple AI Chatbot")

# 2. Secure Client & State Management
if "messages" not in st.session_state:
    st.session_state.messages = []

if "client" not in st.session_state:
    # Replace with your actual key or use st.secrets
    API_KEY = "AIzaSyBMOMscNX9vKFwN-m85BQMSXGswbJin4jo"
    st.session_state.client = genai.Client(api_key=API_KEY)

# Initialize the chat session if it doesn't exist
if "chat_session" not in st.session_state:
    st.session_state.chat_session = st.session_state.client.chats.create(model="gemini-2.5-flash")

# 3. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Chat Input Logic
if prompt := st.chat_input("What is on your mind?"):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and show assistant response
    with st.chat_message("assistant"):
        try:
            response = st.session_state.chat_session.send_message(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error: {e}")





# import streamlit as st
# from google import genai
# import os
# from dotenv import load_dotenv
# load_dotenv()

# # 2. Setup Client (Securely)
# # In production, use st.secrets["GEMINI_API_KEY"]
# API_KEY = "AIzaSyBMOMscNX9vKFwN-m85BQMSXGswbJin4jo" 
# client = genai.Client(api_key=API_KEY)

# # 3. Model selection (Using 2026 naming conventions)
# # 'gemini-3.5-flash-preview' is the high-intelligence fast model for early 2026
# MODEL_ID = "gemini-3.5-flash-preview"



# # Initialize chat history
# # without sessions, chats are not stored
# if "chat" not in st.session_state:
#     st.session_state.chat = model.start_chat(history=[])

# # Display previous messages
# for message in st.session_state.chat.history:
#     role = "assistant" if message.role == "model" else "user"
#     with st.chat_message(role):
#         st.markdown(message.parts[0].text)

# # Chat input
# if prompt := st.chat_input("Type your message..."):
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     response = st.session_state.chat.send_message(prompt)

#     with st.chat_message("assistant"):
#         st.markdown(response.text)