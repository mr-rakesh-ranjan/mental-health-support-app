from fastapi import FastAPI

from backend.models import ConversationData, CopingInput, UserInput
from backend.services.coping_strategies_service import get_coping_strategies_by_LLM, read_csv_file
from backend.services.generate_report_service import generate_combined_graphs, get_mental_health_report
from backend.services.llm_service import GeminiSevice
from backend.services.strategies_service import CopingStrategiesService
from backend.mental_prompts import mental_system_prompt

from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
import csv
import json
app = FastAPI()


llm_service = GeminiSevice()
coping_service = CopingStrategiesService()

def get_professional_data():
    # This function should return a list of dictionaries containing professional data 
    with open('./professional_help.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

def get_emergency_assistance_data():
    with open('./emergency_assistance.json') as jsfile:
        return json.load(jsfile)

emergency_data = coping_service.get_emergency_assistance()
professional_help_data = get_professional_data()

print(f"eme_data -----> {emergency_data} \n\n\n prof_data ------------------> {professional_help_data}")

@app.post("/analyze")
async def analyze_input(user_input: UserInput):
    # call the LLM service to get the response
    user_prompt = f"Use this prompt {mental_system_prompt} to Empathize and provide mental health support based on the following: \n\n {user_input.user_query}. \n\n The current feeling of user is {user_input.feelings} but dont mention this in your response. If any history is required then use this {user_input.history}. For your requirement, if user will ask any professional help and emergency assistance you should use only this data {professional_help_data} and {emergency_data}. If user specifies professional help in {user_input.user_query}, then provide {professional_help_data} only."
    response = llm_service.generate_response_gemini(custom_prompt=user_prompt)
    # print("1: ---->", response) # for debugging onnly
    return {
        "llm_response" : response,        
    }

@app.get("/emergency-assistance")
async def get_emergency_assistance():
    # call the coping strategies service to get the professional resources
    return coping_service.get_emergency_assistance()


# 2.for coping strategies
@app.post("/coping-strategies")
async def get_coping_strategies(coping_input: CopingInput):
    # call the coping strategies service to get the coping strategies
    strategies = get_coping_strategies_by_LLM(coping_input.category, coping_input.subcategory)
    print("Coping strategies -----------------> ", strategies)
    return {
        "coping_strategies": strategies
    }

@app.get("/professional-help", summary="Get professional help details based on mental health category")
async def get_professional_help(category: Optional[str] = Query(None, description="Mental health category to search for")):
    """
    Fetch professional help details based on the specified mental health category, or return all records if no category is specified.
    """
    data = read_csv_file()

    if category:
        # Filter data based on the category (case-insensitive match)
        results = [row for row in data if row['MentalHealthCategory'].strip().lower() == category.strip().lower()]
    else:
        # Return all records if no category is specified
        results = data

    if not results:
        raise HTTPException(status_code=404, detail="No professional help found for the specified criteria.")

    return results


@app.post("/generate_report")
async def generate_report(data: ConversationData):
    try:
        # Get the mental health report from the LLM
        report = get_mental_health_report(data.conversation_data)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

    # Generate graphs based on the LLM report
    graphs = generate_combined_graphs(report)

    return {"graphs": graphs}


@app.post('/get_report_data')
async def get_report_data(data: ConversationData):
    try:
        # Get the mental health report from the LLM
        report = get_mental_health_report(conversation_data=data.conversation_data)
    except HTTPException as e:
        return HTTPException(status_code=e.status_code, detail=e.detail)
    
    return {"report_data": report}