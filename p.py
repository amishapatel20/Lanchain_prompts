from langchain_community.llms import HuggingFaceHub
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Load LLM for summarization
llm = HuggingFaceHub(
    repo_id="google/pegasus-xsum",
    model_kwargs={"max_length": 100, "temperature": 0.7}
)

# Custom CSS to improve the look
st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .title {
        font-size: 40px;
        color: #ff4081;
        text-align: center;
    }
    .subtitle {
        font-size: 20px;
        color: #3f51b5;
        text-align: center;
    }
    .text-area {
        border-radius: 15px;
        border: 2px dashed #3f51b5;
        padding: 10px;
        background-color: #fffaf0;
    }
    </style>
""", unsafe_allow_html=True)

# Cartoon image header
st.image("https://cdn.pixabay.com/photo/2016/04/01/09/00/cartoon-1299394_1280.png", width=200)

st.markdown("<div class='title'>📝 Cartoon Text Summarizer</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Summarize anything with a touch of fun!</div><br>", unsafe_allow_html=True)

input_text = st.text_area("✍️ Enter your text to summarize:", height=300, key="input_text")

if st.button("✨ Summarize"):
    if input_text.strip():
        with st.spinner("Summarizing with cartoon magic..."):
            summary = llm.invoke(input_text)
            st.success("Here’s your summary:")
            st.info(summary)
            st.image("https://cdn.pixabay.com/photo/2014/04/02/14/10/smiley-307571_1280.png", width=100)
    else:
        st.warning("Please enter some text to summarize first!")
