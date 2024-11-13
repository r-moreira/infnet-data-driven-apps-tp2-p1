from fastapi import APIRouter
from ..models.chat_model import ChatInput, ChatOutput
from transformers import pipeline
import torch

router = APIRouter()

def autocomplete_message(message: str) -> str:
    device = torch.device("cpu")
    generator = pipeline(
        "text-generation",
        model="gpt2-large",
        device=device, 
        torch_dtype=torch.bfloat16
    )
    return generator(message)[0]['generated_text']

def translate_en_fr(text):
    device = torch.device("cpu")
    generator = pipeline(
        "translation",
        model='Helsinki-NLP/opus-mt-en-fr',
        device=device, 
        torch_dtype=torch.bfloat16
    )
    return generator(text)[0]['translation_text']

@router.post("/gpt2/autocomplete/")
async def autocomplete(body: ChatInput) -> ChatOutput:
    response = autocomplete_message(body.message)
    return ChatOutput(message=response)

@router.post("/helsinki/translate/en-fr/")
async def translate(body: ChatInput) -> ChatOutput:
    response = translate_en_fr(body.message)
    return ChatOutput(message=response)