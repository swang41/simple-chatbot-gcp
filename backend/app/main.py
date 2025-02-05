import logging
import google.generativeai as genai
from fastapi import FastAPI
from pydantic import BaseModel
from app.config import get_secret

# Build a FastAPI
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Fetch secrets
PROJECT_ID = "simple-llm-chatbot" 
API_KEY = get_secret("GEMINI_API_KEY", PROJECT_ID)

# Initialize Gemini model
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def get_response(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    response = get_response(request.prompt)
    #log first 100 char for insepection
    logger.info(response[:100])
    return {"response": response}