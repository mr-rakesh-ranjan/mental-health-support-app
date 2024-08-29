import csv
from fastapi import HTTPException
import google.generativeai as genai
from backend.services.llm_service import GeminiSevice

from config import Config

category = [
    {
        "category_name" :"General Emotional State",
        "sub-category": [
            "Emotional Regulation",
            "Mood Swings",
            "Emotional Resilience",
            "Coping with Life Changes",
            "Emotional Self-Awareness",
            "Emotional Sensitivity"
        ]
    },
    {
        "category_name" :"Stress and Anxiety",
        "sub-category": [
            "Generalized Anxiety Disorder (GAD)"
            "Panic Disorder",
            "Social Anxiety Disorder",
            "Performance Anxiety",
            "Work-Related Stress",
            "Health Anxiety (Hypochondria)",
            "Exam/Study Stress"
        ]
    },
    {
        "category_name" :"General Emotional State",
        "sub-category": [
            "Emotional Regulation",
            "Mood Swings",
            "Emotional Resilience",
            "Coping with Life Changes",
            "Emotional Self-Awareness",
            "Emotional Sensitivity"
        ]
    },
]
# safety measures for gemini LLM

llm_service = GeminiSevice()

def get_coping_strategies_by_LLM(category, subcategory):
    # This is a placeholder function. You would replace this with your actual LLM model
    # For demonstration purposes, we'll just return a random list of coping strategies
    user_prompt = f"Give simple, evidence-based coping strategies for {category} under {subcategory}. Briefly explain each strategy and its goal with easy steps to follow. Make response as much as sorter."
    response = llm_service.generate_response_gemini(custom_prompt=user_prompt)
    return response

def read_csv_file():
    """
    Reads the CSV file and returns its content as a list of dictionaries.
    """
    data = []
    try:
        with open('././professional_help.csv', mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="CSV file not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading CSV file: {e}")
    return data