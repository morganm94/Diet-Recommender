# Personalized Diet and Workout Recommender App

## Overview

This is a web application designed to provide personalized diet and workout recommendations based on user input. The recommendations are generated using a language model (LLM) for a more interactive experience.

## Features

- **User Input**: Collects user information such as age, gender, weight, height, dietary preferences, address, and food allergies.

- **LLM Integration**: Utilizes a language model for generating recommendations tailored to user input.

- **Recommendation Categories**: Provides recommendations for restaurants, breakfast, dinner, and workouts.

- **Interactive Interface**: Utilizes the Streamlit framework to create a user-friendly and interactive web interface.


## Demo Results
<img width="947" alt="image" src="https://github.com/Deepakv1210/Diet-Recommender/assets/154148155/723ecf56-9ee3-4de8-a684-f6f0494c82be">
<img width="514" alt="image" src="https://github.com/Deepakv1210/Diet-Recommender/assets/154148155/7475c1e9-7ac4-4116-a6a7-92af1d76361c">


## Getting Started

1. Install the required dependencies if using Llama2 LLM:

    ```bash
    pip install torch streamlit transformers ctransformers
    ```

2. Set up your OpenAI API key:

    Obtain an API key from OpenAI and set it as an environment variable.

    ```bash
    export OPENAI_API_KEY=api_key
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Usage

1. Open the web application in your browser.

2. Input your personal details including age, gender, weight, height, dietary preferences, address, and food allergies.

3. Click the "Get Recommendations" button.

4. View the personalized recommendations for restaurants, breakfast, dinner, and workouts.
