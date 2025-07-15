from langchain_community.llms import Ollama
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt


load_dotenv()

st.set_page_config(page_title="Research Paper Summarizer")

st.title("📄 Research Paper Summarizer (Open Source)")
st.markdown("Powered by **LangChain + Ollama + Streamlit**")

paper_input = st.selectbox(
    "Select Research Paper",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

template = load_prompt("template.json")


llm = Ollama(model="mistral")  

if st.button("Summarize"):
    with st.spinner("Generating summary..."):
        chain = template | llm
        result = chain.invoke({
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input
        })
        st.markdown(result)  

