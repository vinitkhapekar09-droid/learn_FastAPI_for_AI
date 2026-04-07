import os
from fastapi import FastAPI
from pydantic import BaseModel
from .ai.gemini import Gemini

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    response: str


def load_system_prompt():
    with open("src/prompts/system_prompt.md", "r") as f:
        return f.read()


system_prompt = load_system_prompt()
gemini_api_key = os.getenv("GOOGLE_API_KEY")

if not gemini_api_key:
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables.")

ai_platform = Gemini(api_key=gemini_api_key, system_prompt=system_prompt)


@app.get("/")
async def root():
    return {"message": "API is working!"}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response_text = ai_platform.chat(request.prompt)
    return ChatResponse(response=response_text)
