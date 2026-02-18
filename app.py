import streamlit as st
import pandas as pd 
import time
# from google import genai  # Ensure 'google-genai' is installed
from google.genai import Client
import sys
import os

# Manually add the User site-packages to the path
user_site = r"C:\Users\ARUNIMA\AppData\Roaming\Python\Python313\site-packages"
if user_site not in sys.path:
    sys.path.append(user_site)



# # Then initialize like this:
# client = Client(api_key="AIzaSyBd8UuXOwGOppnY7tyyKaxaSOOamxPRCek")
# 1. Initialize the client at the top-level so the function can see it
API_KEY = "AIzaSyBd8UuXOwGOppnY7tyyKaxaSOOamxPRCek"
client =Client(api_key=API_KEY)

def cook_food(prompt):
    if prompt:
        # User feedback with toasts
        st.toast("Gathering ideas...")
        time.sleep(1)
        st.toast("Ideating...")
        time.sleep(1)
        st.toast("Ready!")
        
        st.write(f"### So you want a poem with **{prompt}** today.")
        st.write("Let's see :")
        
        # 2. Call the new SDK method correctly
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash", # Use 2.0 or 1.5 (2.5 isn't public yet)
                contents=f"Write a summarized recipe for: {prompt}"
            )
            st.markdown(response.text)
        except Exception as e:
            st.error(f"API Error: {e}")

if __name__ == "__main__":
    st.title("🍳 Recipe Generator")
    
    # Use chat_input for a modern look
    prompt = st.chat_input("What's cooking?")
    
    if prompt:
        cook_food(prompt)



























# # import streamlit as st
# # import pandas as pd 
# # import time

# import google.generativeai as genai
# # API_KEY="AIzaSyBd8UuXOwGOppnY7tyyKaxaSOOamxPRCek"
# # # Access the secret directly
# # api_key = st.secrets["API_KEY"]
# # genai.configure(api_key=api_key)
# import streamlit as st
# import pandas as pd 
# import time
# # from google import genai

# def cook_food(prompt):
#     if prompt:
#         msg = st.toast("Gathering ingredients...")
#         time.sleep(2)
#         msg = st.toast("Cooking...")
#         time.sleep(2)
#         msg = st.toast("Ready!", icon="🥞")
#         time.sleep(2)
#         st.write(f"So you want to prepare {prompt} today.")
#         time.sleep(1)
#         st.write("Let's see how you can make it.")
#         response = client.models.generate_content(
#             model="gemini-2.5-flash", 
#             contents=f"Write a summarized recipe on {prompt}")
#         st.write(response.text)

# # a function to pull up images goes here
# # I will write this function later 

# if __name__=="__main__":
#     API_KEY = "AIzaSyBd8UuXOwGOppnY7tyyKaxaSOOamxPRCek"   # YOUR API
#     # initialize the client
#     client = genai.Client(api_key=API_KEY)
#     # title 
#     st.title("Recipe Generator")
#     prompt = st.chat_input("What's cooking?")
#     cook_food(prompt)
    
    

# # model = genai.GenerativeModel('gemini-1.5-flash')

# # st.title("🍳 AI Chef")

# # # 3. Get Input
# # ingredients = st.text_input("List the ingredients (e.g., Tomato, Egg, Onion)")

# # # 4. Handle API Request
# # if st.button("Cook"):
# #     if ingredients:
# #         with st.spinner("Cooking up a recipe..."):
# #             try:
# #                 # 5. Send to API
# #                 response = model.generate_content(f"Give me a simple recipe using these ingredients: {ingredients}")
                
# #                 # 6. Display Output
# #                 st.success("Here is your recipe!")
# #                 st.markdown(response.text)
# #             except Exception as e:
# #                 st.error(f"An error occurred: {e}")
# #     else:
# #         st.warning("Please enter some ingredients first!")
        
        
# # # st.text_input("List the ingredients")
# # # if st.button("Cook"):
# # #     st.success("Cooked")
    
# # # def cook_food(prompt):
# # #     if prompt:
# # #         msg = st.toast("Gathering ingredients...")
# # #         time.sleep(2)
# # #         msg = st.toast("Cooking...")