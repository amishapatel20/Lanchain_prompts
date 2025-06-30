import os
from langchain_community.llms import HuggingFaceHub
from langchain_core.prompts import load_prompt
import streamlit as st

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")



llm = HuggingFaceHub(
    repo_id="LaMini-Flan-T5-783M",
    task="summarization",
    huggingfacehub_api_token=hf_token,
    model_kwargs={
        "temperature": 0.7,
        "max_new_tokens": 300
    }
)


st.title("📚 Research Paper Summarizer")

paper_input = st.selectbox("Select Research Paper Name", [
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis"
])

style_input = st.selectbox("Select Explanation Style", [
    "Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"
])

length_input = st.selectbox("Select Explanation Length", [
    "Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"
])


template = load_prompt('template.json')


if st.button("Summarize"):
    with st.spinner("Generating summary..."):
        try:
            final_prompt = template.format(
                paper_input=paper_input,
                style_input=style_input,
                length_input=length_input
            )
            result = llm.invoke(final_prompt)
            st.success("Summary Generated")
            st.write(result)
        except Exception as e:
            st.error(f"Could not generate summary: {e}")

