from dotenv import load_dotenv
import os

load_dotenv()
print("Token:", os.getenv("HUGGINGFACEHUB_API_TOKEN"))  

