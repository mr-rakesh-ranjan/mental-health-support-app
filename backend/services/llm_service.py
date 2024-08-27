import openai
from backend.models import UserInput
from config import Config
from backend.utils.mental_prompts import mental_system_prompt

class LLMService:
    def __init__(self) -> None:
        openai.api_key = Config.OPENAI_API_KEY

    def get_llm_reseponse(self, text: str) -> str:
        """Get response from LLM model."""
        response = openai.Completion.create(
            model="gpt-4o-mini",
            prompt=f"Empathize and provide mental health support based on the following: \n\n {text}",
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    

import google.generativeai as genai
class GeminiSevice:
    # def __init__(self) -> None:
    #     genai.configure(api_key = Config.GEMINI_API_KEY)
    

    def get_gemini_response(self, user_input: UserInput) -> str:
        """Get response from Gemini model."""
        print("api -key -----> ", Config.GEMINI_API_KEY)
        genai.configure(api_key = Config.GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(
            f"Use this prompt {mental_system_prompt} to Empathize and provide mental health support based on the following: \n\n {user_input.user_query}. \n\n My current feeling is {user_input.feelings}. If any history is required then use this {user_input.history}",
            generation_config=genai.types.GenerationConfig(temperature=0)
        )

        return response.text


