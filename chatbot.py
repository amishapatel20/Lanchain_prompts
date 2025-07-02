from langchain_huggingface import HuggingFaceEndpoint
import os


os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_YOUR_ACTUAL_TOKEN_HERE"


chat_model = HuggingFaceEndpoint(
    repo_id="tiiuae/falcon-7b-instruct",
    task="text-generation",
    max_new_tokens=512,
    temperature=0.7,
)

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input.strip().lower() == "exit":
        break
    response = chat_model.invoke(chat_history)
    chat_history.append(response.content)
    print("AI:", response)

print(chat_history)
