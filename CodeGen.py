import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a code completion tool, please complete the code/program given by user"),
    ("user", "Question: {question}")
])

st.title("Langchain Demo with Gemma ")
input_text = st.text_input("Your question: ")

model = Ollama(model="gemma2:2b")      # your model name goes here

output_parser = StrOutputParser()

chain = prompt | model | output_parser

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)