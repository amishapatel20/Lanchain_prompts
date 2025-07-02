from langchain_core.messages import SystemMessage, HumanMessage , AIMessage
from Langchain_openai import ChatOpenAI
from dotenv import load_dotenv 

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content='Yor are a helpful assistant'),
    HumanMesssage(content='Tell me about LangChain')
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)