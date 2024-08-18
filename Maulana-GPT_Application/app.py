import streamlit as st
from search import prompt_search
from test import create_response
#from agent import create_response

st.title("🕌🤖 Maulana-GPT")
prompt = st.text_input("Enter your prompt: ") 

if st.button("Enter"):
    info = prompt_search(prompt)
    if info:
        st.write(f"**Title:** {info[0]}")
        st.write(f"**Link:** {info[1]}")
        st.write(f"**Snippet:** {info[2]}")
        
        reply = create_response(prompt, info)
        st.write(f"**Response:** {reply}")
    else:
        st.write("An error occured.")
