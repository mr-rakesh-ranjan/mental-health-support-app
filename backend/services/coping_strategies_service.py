import google.generativeai as genai

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

def get_coping_strategies_by_LLM(category, subcategory):
    # This is a placeholder function. You would replace this with your actual LLM model
    # For demonstration purposes, we'll just return a random list of coping strategies
    genai.configure(api_key = Config.GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(
        f"Please identify the best coping strategies for users in the [Mental Health Category] {category}, specifically under the {subcategory} area. Consider evidence-based approaches, and tailor the recommendations to be practical and user-friendly. For each strategy, provide a brief explanation, its intended outcome, and a step-by-step guide on how to implement it in daily life",
        generation_config=genai.types.GenerationConfig(temperature=0)
    )

    return response.text