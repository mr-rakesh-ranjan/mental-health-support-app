# Mental Health Support App Using LLM

This project is an innovative mental health support application that leverages **Gemini** (GPT-based LLM) and **FastAPI** to provide empathetic responses, coping strategies, and resources for professional help. The application enables users to anonymously discuss their mental health concerns, offering support in real-time.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Frontend (Streamlit)](#frontend-streamlit)
- [Backend (FastAPI)](#backend-fastapi)
- [Best Practices](#best-practices)
- [Future Enhancements](#future-enhancements)

---

## Features
- **Anonymous Mental Health Support**: Users can submit concerns without revealing their identity.
- **Empathetic Responses**: Powered by **Gemini** LLM, the app provides empathetic and non-judgmental responses.
- **Coping Strategies**: Users receive personalized coping strategies based on their input.
- **Professional Resources**: The app suggests professional mental health resources if needed.
- **Interactive Client Interface**: Simple and intuitive user interface using **Streamlit**.
  
---

## Tech Stack
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **LLM**: Gemini (via OpenAI GPT API)
- **Other Libraries**:
  - `requests` for API calls
  - `pydantic` for data validation in FastAPI
  - `uvicorn` to run the FastAPI server

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/mr-rakesh-ranjan/mental-health-support-app.git
cd mental-health-support-app
```

### 2. Set up Virtual Environment
It’s recommended to use a virtual environment to avoid dependency conflicts.
```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Configuration

You need an **GEMINI API Key** to interact with the **Gemini** LLM.

1. Create a `.env` file or set environment variables for your API key.

```bash
GEMINI_API_KEY=your_gemini_api_key
```

2. You can also update the `config.py` file to hardcode your API key (not recommended for production).

---

## Usage

### 1. Run the FastAPI Backend
First, start the backend API service using FastAPI and Uvicorn.

```bash
cd backend
uvicorn backend.main:app --reload
```

This will start the backend on `http://localhost:8000`.

### 2. Run the Streamlit Frontend
Next, start the Streamlit client interface where users can submit their concerns.

```bash
cd frontend
streamlit run frontend/app.py
```

This will launch the frontend in your browser at `http://localhost:8501`.

---

## API Documentation

The FastAPI backend exposes the following endpoints:

### 1. Analyze Input (POST `/analyze/`)
- **Description**: Analyzes user input to provide empathetic responses and coping strategies.
- **Request**:
  - Body (JSON):
    ```json
    {
      "text": "I feel very stressed and anxious about work."
    }
    ```
- **Response** (JSON):
  ```json
  {
    "llm_response": "It's completely normal to feel anxious during tough times at work. Try taking breaks and practicing mindfulness.",
    "coping_strategies": [
      "Take deep breaths and focus on the present moment.",
      "Engage in a hobby or activity that brings you joy.",
      "Reach out to a trusted friend or family member."
    ]
  }
  ```

### 2. Get Professional Resources (GET `/resources/`)
- **Description**: Provides a list of professional mental health resources.
- **Response** (JSON):
  ```json
  [
    {"name": "National Suicide Prevention Lifeline", "contact": "1-800-273-8255"},
    {"name": "BetterHelp", "website": "https://www.betterhelp.com"},
    {"name": "Talkspace", "website": "https://www.talkspace.com"}
  ]
  ```

---

## Frontend (Streamlit)
The **Streamlit** client provides an easy-to-use interface for users to input their mental health concerns.

### Key Features:
- **User Input**: Users can submit their text, which is sent to the FastAPI backend for analysis.
- **Real-Time Response**: The app shows LLM-generated empathetic responses and coping strategies directly on the interface.

### How to Use:
1. Enter your mental health concerns in the provided text area.
2. Click **Submit** to receive suggestions and feedback.
3. View the **Empathetic Response** and a list of **Coping Strategies**.

---

## Backend (FastAPI)

The **FastAPI** backend provides the main logic for processing input, calling the Gemini LLM API, and returning coping strategies.

### Key Components:
1. **LLM Service**: This handles communication with the Gemini API (through OpenAI) to generate responses based on user input.
2. **Coping Strategies Service**: This module returns helpful strategies and professional resources.
3. **Data Validation**: The input is validated using Pydantic models.

### FastAPI Server
You can run the FastAPI server locally using `uvicorn`.

```bash
uvicorn backend.main:app --reload
```

---

## Best Practices

### 1. Security
- **API Key Management**: Store your OpenAI API key in environment variables, not in code.
- **Input Sanitization**: Ensure proper input sanitization to avoid malicious content being processed.

### 2. Modularity
- **Separation of Concerns**: The project is divided into backend and frontend components for better modularity and maintainability.
- **Service-Oriented**: The backend services (LLM, coping strategies) are isolated into separate modules for future scalability.

### 3. Scalability
- **Containerization**: Consider using **Docker** to containerize the FastAPI and Streamlit services for easy deployment.
- **Caching**: Implement caching for frequently used resources (e.g., coping strategies).

---

## Future Enhancements

1. **User Authentication**: Implement user authentication for personalized experiences and mental health tracking over time.
2. **Analytics Dashboard**: Use Streamlit or another frontend to provide users with data on their progress and insights.
3. **Advanced NLP Models**: Incorporate more advanced NLP techniques or custom-trained models for better text understanding.
4. **Mental Health Assessment**: Expand the service to offer assessments for various mental health conditions.
5. **Support for Multiple Languages**: Implement support for users in different languages.

---

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

---

Feel free to modify the README as per your specific project requirements and branding! Let me know if you need further adjustments or additions.