from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain.messages import AIMessage , SystemMessage , HumanMessage

import streamlit as st

import os
import dotenv
dotenv.load_dotenv()

HUGGINGFACEHUB_ACCESS_TOKEN = os.getenv('HUGGINGFACEHUB_ACCESS_TOKEN')
llm = HuggingFaceEndpoint(repo_id='meta-llama/Llama-3.1-8B-Instruct',huggingfacehub_api_token=HUGGINGFACEHUB_ACCESS_TOKEN)
model = ChatHuggingFace(llm=llm)

system_message = SystemMessage(content='''
                               You are an expert chef and recipe generator. Your task is to create complete, clear, and easy-to-follow recipes based on the ingredients provided by the user. Follow these rules:

1. Start with a **recipe title**.
2. List all **ingredients with quantities**.
3. Provide **step-by-step instructions** for preparing the dish.
4. Keep instructions simple, concise, and easy to follow.
5. Suggest optional **tips or variations** if appropriate.
6. Assume the cuisine can be adapted to the user's region or style (e.g., Nepali, vegetarian, quick meals) if not specified.
7. Avoid adding ingredients that are not listed unless necessary for basic cooking (like salt, water, or oil).

Respond in **clear, structured text** that a user can immediately follow to cook the dish.
                               Reply if the use provide positive or negaitve feedback.
                               '''
                               )
history = []

if "history" not in st.session_state:
    st.session_state.history = [system_message]

for msg in st.session_state.history:
    if msg.type == 'system':
        continue
    with st.chat_message(msg.type):
        st.write(msg.content)
    

prompt = st.chat_input("Your message ...")

if prompt:
    st.session_state.history.append(HumanMessage(content=prompt))

    result = model.invoke(st.session_state.history)

    st.session_state.history.append(AIMessage(content=result.content))

    with st.chat_message("user"):
        st.write(prompt)

    
    with st.chat_message("assistant"):
        st.write(result.content)

    
