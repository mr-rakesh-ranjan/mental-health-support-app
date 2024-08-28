import streamlit as st
import requests

# API endpoints
API_URL = "http://127.0.0.1:8000/analyze"
RESOURCE_URL = "http://127.0.0.1:8000/resources"
COPING_URL = "http://127.0.0.1:8000/coping-strategies"

st.title("Mental health Support APP")

user_input = st.text_area("Describe your mental health concerns here...")

if st.button("Submit"):
    if user_input:
        # response =  requests.post(API_URL, json={"user_query": user_input, "feelings": "stressed"})
        response = requests.post(
            COPING_URL, 
            json={
                "category": "General Emotional State",
                "subcategory": "Mood Swings"
            }
        )

        if response.status_code == 200:
            result = response.json()
            st.subheader("Empathetic Response")
            # st.write(result['llm_response'])
            st.write(result['coping_strategies'])

            # st.subheader("Coping strategies")
            # for strategy in result['coping_stratgies']:
            #     st.write(f" - {strategy}")
        else:
            st.error("Error in processing the request. Please try again.")
    else:
        st.error("Please enter some text before submitting.")
