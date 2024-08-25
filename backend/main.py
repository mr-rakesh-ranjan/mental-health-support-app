from fastapi import FastAPI
from pydantic import BaseModel

from backend.services.llm_service import GeminiSevice
from backend.services.strategies_service import CopingStrategiesService

app = FastAPI()

# models
class UserInput(BaseModel):
    text: str

llm_service = GeminiSevice()
coping_service = CopingStrategiesService()

@app.post("/analyze")
async def analyze_input(user_input: UserInput):
    # call the LLM service to get the response
    response = llm_service.get_gemini_response(user_input.text)
    # call the coping strategies service to get the coping strategies
    coping_strategies = coping_service.get_coping_strategies(response)

    return {
        "llm_response" : response,
        "coping_stratgies": coping_strategies
    }

@app.get("/resources")
async def get_professional_resources():
    # call the coping strategies service to get the professional resources
    return coping_service.get_professional_resources()

