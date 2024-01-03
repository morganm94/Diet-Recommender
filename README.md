# Personalized Diet and Workout Recommender App

## Overview

This is a Streamlit web application designed to provide personalized diet and workout recommendations based on user input. The recommendations are generated using a language model (LLM) to create a natural language dialogue for a more interactive experience.

## Features

- **User Input**: Collects user information such as age, gender, weight, height, dietary preferences, address, and food allergies.

- **LLM Integration**: Utilizes a language model for generating recommendations tailored to user input.

- **Recommendation Categories**: Provides recommendations for restaurants, breakfast, dinner, and workouts.

- **Interactive Interface**: Utilizes the Streamlit framework to create a user-friendly and interactive web interface.

## Getting Started

1. Install the required dependencies:

    ```bash
    pip install torch streamlit transformers ctransformers
    ```

2. Set up your OpenAI API key:

    Obtain an API key from OpenAI and set it as an environment variable.

    ```bash
    export OPENAI_API_KEY=your_api_key
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run your_app_file.py
    ```

## Usage

1. Open the web application in your browser.

2. Input your personal details including age, gender, weight, height, dietary preferences, address, and food allergies.

3. Click the "Get Recommendations" button.

4. View the personalized recommendations for restaurants, breakfast, dinner, and workouts.
