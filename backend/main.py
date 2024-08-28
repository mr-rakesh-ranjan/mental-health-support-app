from fastapi import FastAPI

from backend.models import CopingInput, UserInput
from backend.services.coping_strategies_service import get_coping_strategies_by_LLM
from backend.services.llm_service import GeminiSevice
from backend.services.strategies_service import CopingStrategiesService

app = FastAPI()


llm_service = GeminiSevice()
coping_service = CopingStrategiesService()

@app.post("/analyze")
async def analyze_input(user_input: UserInput):
    # call the LLM service to get the response
    response = llm_service.get_gemini_response(user_input)
    # call the coping strategies service to get the coping strategies
    coping_strategies = coping_service.get_coping_strategies(response)
    print("-------> ",user_input)


    return {
        "llm_response" : response,        
    }

@app.get("/resources")
async def get_professional_resources():
    # call the coping strategies service to get the professional resources
    return coping_service.get_professional_resources()


# 2.for coping strategies
@app.post("/coping-strategies")
async def get_coping_strategies(coping_input: CopingInput):
    # call the coping strategies service to get the coping strategies
    strategies = get_coping_strategies_by_LLM(coping_input.category, coping_input.subcategory)
    print("Coping strategies -----------------> ", strategies)
    return {
        "coping_strategies": strategies
    }


