Personalized Diet and Workout Recommender App
Overview
This is a Streamlit web application designed to provide personalized diet and workout recommendations based on user input. The recommendations are generated using a language model (LLM) to create a natural language dialogue for a more interactive experience.

Features
User Input: Collects user information such as age, gender, weight, height, dietary preferences, address, and food allergies.

LLM Integration: Utilizes a language model for generating recommendations tailored to user input.

Recommendation Categories: Provides recommendations for restaurants, breakfast, dinner, and workouts.

Interactive Interface: Utilizes the Streamlit framework to create a user-friendly and interactive web interface.

Getting Started
Install the required dependencies:

bash
Copy code
pip install torch streamlit transformers ctransformers
Set up your OpenAI API key:

Obtain an API key from OpenAI and set it as an environment variable.

bash
Copy code
export OPENAI_API_KEY=your_api_key
Run the Streamlit app:

bash
Copy code
streamlit run your_app_file.py
Usage
Open the web application in your browser.

Input your personal details including age, gender, weight, height, dietary preferences, address, and food allergies.

Click the "Get Recommendations" button.

View the personalized recommendations for restaurants, breakfast, dinner, and workouts.
