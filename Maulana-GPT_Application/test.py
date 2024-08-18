import streamlit as st
from langchain_community.llms import Ollama

def create_response(prompt, input_array):

    title, page, snippet = input_array
    llm = Ollama(model="phi3")

     # Use the 'model' object to generate the result
    result = llm.invoke(prompt + "use the following text to answer like a shia scholar with short text" + snippet) 
    return(result)  # Display the 'result', not the 'prompt'
