from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv


st.set_page_config(page_title="AI Code Tutor | LangChain + Ollama")

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGCHAIN_API_KEY"] = ""


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a code tutor. Help the user with code questions. Give clear explanations followed by code examples."),
    ("user", "Question: {question}")
])


st.title('🤖 AI Code Tutor ')


input_text = st.text_input("Enter your programming question here...")


llm = Ollama(model="mistral")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser


if input_text:
    response = chain.invoke({"question": input_text})
   
    if "```" in response:
        st.markdown(response)
    else:
        st.write(response)
