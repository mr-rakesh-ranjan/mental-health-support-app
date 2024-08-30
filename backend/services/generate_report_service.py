import re
from backend.services.llm_service import GeminiSevice

import matplotlib.pyplot as plt
import io
import base64
import json as js

def get_mental_health_report(conversation_data):
    prompt = """
    Instructions:
    1. Identify primary emotions expressed and their frequency as percentages.
    2. Analyze sentiment trends throughout the conversation (start, middle, end) with scores from 1 to 10.
    3. Determine the emotional intensity and provide an average score from 1 to 10.
    4. List the key mental health topics discussed and their frequency.
    5. Provide results in a structured JSON format.
    6. you should always generate the response in this example format and don't use % symbol in response:
        {
            "primary_emotions": {
                "sadness": integer type range 1 to 100,
                ...
            },
            "sentiment_trends": {
                "start": range 1 to 10,
                "middle":  range 1 to 10,
                "end":  range 1 to 10
            },
            "emotional_intensity":  range 1 to 10,
            "mental_health_topics": {
                "stress":  range 1 to 10,
                "loneliness":  range 1 to 10,
                "anxiety":  range 1 to 10,
                "depression":  range 1 to 10
            }
        }
    """
    prompt2 = f"""
    Analyze the following conversation data and provide a mental health statistics report in JSON format:
    {conversation_data} \n\n {prompt}
    """

    response = GeminiSevice().generate_response_gemini(custom_prompt=prompt2)
    response_clean = response.strip('```json').strip()
    response_clean_percent = re.sub(r'(\d+)\%', r'\1', response_clean)
    # print(response_clean_percent)
    response_data = js.loads(response_clean_percent)
    return response_data


# Function to generate graphs based on the report
def generate_graphs(report):
    graphs = {}
    print(report)
    # Plot primary emotions
    primary_emotions = report.get('primary_emotions', {})
    # print(primary_emotions)
    if primary_emotions:
        print("1")
        emotions = list(primary_emotions.keys())
        frequencies = list(primary_emotions.values())
        plt.figure()
        plt.barh(emotions, frequencies, color='skyblue')
        plt.title("Primary Emotion Frequency")
        plt.xlabel("Emotions")
        plt.ylabel("Frequency (%)")
        plt.show()
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        graphs['emotion_graph'] = base64.b64encode(buf.getvalue()).decode('utf-8')
        plt.close()

    # Plot sentiment trend
    sentiment_trends = report.get("sentiment_trends", {})
    if sentiment_trends:
        print("2")
        stages = list(sentiment_trends.keys())
        scores = list(sentiment_trends.values())
        plt.figure()
        plt.plot(stages, scores, marker='o', color='red')
        plt.title("Sentiment Trend")
        plt.xlabel("Conversation Stage")
        plt.ylabel("Sentiment Score")
        plt.show()
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        graphs['sentiment_graph'] = base64.b64encode(buf.getvalue()).decode('utf-8')
        plt.close()

    # Plot mental health topics frequency
    mental_health_topics = report.get("mental_health_topics", [])
    if mental_health_topics:
        print("3")
        topics = [list(topic.keys())[0] for topic in mental_health_topics]
        frequencies = [list(topic.values())[0] for topic in mental_health_topics]
        plt.figure()
        plt.pie(frequencies, labels=topics, autopct='%1.1f%%', colors=plt.cm.Paired(range(len(topics))))
        plt.title("Mental Health Topics")
        plt.show()
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        graphs['topics_graph'] = base64.b64encode(buf.getvalue()).decode('utf-8')
        plt.close()

    return graphs


def generate_combined_graphs(report):
    graphs = {}
    
    # Create 2x2 subplot layout
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))  # Increase figure size (14x10 inches)
    axes = axes.flatten()   # Flatten the 2x2 grid into a list for easier access
    
    # Plot primary emotions
    primary_emotions = report.get('primary_emotions', {})
    if primary_emotions:
        emotions = list(primary_emotions.keys())
        frequencies = list(primary_emotions.values())
        axes[0].barh(emotions, frequencies, color='skyblue')
        axes[0].set_title("Primary Emotion Frequency")
        axes[0].set_xlabel("Frequency (%)")
        axes[0].set_ylabel("Emotions")
    
    # Plot sentiment trend
    sentiment_trends = report.get("sentiment_trends", {})
    if sentiment_trends:
        stages = list(sentiment_trends.keys())
        scores = list(sentiment_trends.values())
        axes[1].plot(stages, scores, marker='o', color='red')
        axes[1].set_title("Sentiment Trend")
        axes[1].set_xlabel("Conversation Stage")
        axes[1].set_ylabel("Sentiment Score")
    
    # Plot mental health topics frequency
    mental_health_topics = report.get("mental_health_topics", [])
    if mental_health_topics:
        topics = [list(topic.keys())[0] for topic in mental_health_topics]
        frequencies = [list(topic.values())[0] for topic in mental_health_topics]
        axes[2].pie(frequencies, labels=topics, autopct='%1.1f%%', colors=plt.cm.Paired(range(len(topics))))
        axes[2].set_title("Mental Health Topics")
    
    # Hide the 4th subplot (axes[3]) since we don't have a 4th graph
    axes[3].axis('off')


    
    # Adjust layout to prevent overlap
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0.4, wspace=0.3)
    
    # Save the figure to a buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    # Encode the figure as a base64 string
    graphs['combined_graph'] = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    # Close the plot to free memory
    plt.show()
    plt.close()
    
    return graphs
