from transformers import pipeline
import torch

class LLMService:
    def __init__(self):
        pass

    @staticmethod  
    def autocomplete_message(message: str) -> str:
        device = torch.device("cpu")
        generator = pipeline(
            "text-generation",
            model="gpt2-large",
            device=device, 
            torch_dtype=torch.bfloat16
        )
        return generator(message)[0]['generated_text']

    @staticmethod
    def translate_en_fr(text) -> str:
        device = torch.device("cpu")
        generator = pipeline(
            "translation",
            model='Helsinki-NLP/opus-mt-en-fr',
            device=device, 
            torch_dtype=torch.bfloat16
        )
        return generator(text)[0]['translation_text']