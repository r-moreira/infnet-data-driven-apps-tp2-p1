from fastapi import APIRouter
from ..models.chat_model import ChatInput, ChatOutput
from ..services.llm_service import LLMService

router = APIRouter()

@router.post("/gpt2/autocomplete/")
async def autocomplete(body: ChatInput) -> ChatOutput:
    response = LLMService.autocomplete_message(body.message)
    return ChatOutput(message=response)

@router.post("/helsinki/translate/en-fr/")
async def translate(body: ChatInput) -> ChatOutput:
    response = LLMService.translate_en_fr(body.message)
    return ChatOutput(message=response)