import os
import openai
from chat_model import MessageRequestDTO





class ChatGptService:

    @classmethod
    def get_ai_model_answer(cls, data: MessageRequestDTO):
        return openai.Completion.create(
            prompt=data.question,
            model=data.model_id,
            temperature=data.temperature,
            max_tokens=data.max_tokens
        )

    @classmethod
    def list_models(cls):
        return openai.Model.list()
