import torch
import gc
gc.collect()
torch.cuda.empty_cache()
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import re
import os
# from ctransformers import AutoModelForCausalLM, AutoTokenizer
import os 
# from Openai_api import apikey
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get('apikey')
os.environ['OPENAI_API_KEY'] = api_key
st.title("Personalized Diet and Workout Recommender:coffee:")
st.markdown('<style>h1{color: orange; text-align: center;}</style>', unsafe_allow_html=True)
st.subheader('Your Best Food and Exercise Advisor:spoon:')
st.markdown('<style>h3{color: pink;  text-align: center;}</style>', unsafe_allow_html=True)

#llm = CTransformers(model="llama-2-7b-chat.Q4_K_M.gguf", config={'max_new_tokens': 1024, "temperature": 0.3},gpu_layers=50)
#llm = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-7B-Chat-GGUF",model_file="llama-2-7b-chat.Q4_K_M.gguf", gpu_layers=50)
llm = OpenAI(temperature=0.9)

prompt_template = PromptTemplate(
    input_variables=['age', 'gender', 'weight', 'height', 'veg_or_nonveg', 'address', 'allergies'],
    template="Diet Recommendation System:\n"
             "Please recommend 5 restaurants names, 5 breakfast names, 5 dinner names, and 5 workout names, "
             "based on the following criteria given below:\n"
             "Age: {age}\n"
             "Gender: {gender}\n"
             "Weight: {weight}\n"
             "Height: {height}\n"
             "Veg_or_Nonveg: {veg_or_nonveg}\n"
             "Address: {address}\n"
             "Food allergies: {allergies}."
             
)

age = st.number_input("Age", min_value=0)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
weight = st.number_input("Weight (pounds)", min_value=0)
height = st.number_input("Height (cm)", min_value=0)
veg_or_nonveg = st.selectbox("Veg or Non-Veg", ["Veg", "Non-Veg"])
address = st.text_input("Address")
allergies = st.text_input("Food allergies")

if st.button("Get Recommendations"):
    chain = LLMChain(llm=llm, prompt=prompt_template)
    input_data = {
        'age': age,
        'gender': gender,
        'weight': weight,
        'height': height,
        'veg_or_nonveg': veg_or_nonveg,
        'address': address,
        'allergies': allergies
    }
    results = chain.run(input_data)

    # Initialize recommendation lists
    restaurant_names = []
    breakfast_names = []
    dinner_names = []
    workout_names = []

    # Extracting the different recommendations using regular expressions
    restaurant_matches = re.findall(r'Restaurants:(.*?)Breakfast:', results, re.DOTALL)
    if restaurant_matches:
        restaurant_names = [name.strip() for name in restaurant_matches[0].strip().split('\n') if name.strip()]
 
    breakfast_matches = re.findall(r'Breakfast:(.*?)Dinner:', results, re.DOTALL)
    if breakfast_matches:
        breakfast_names = [name.strip() for name in breakfast_matches[0].strip().split('\n') if name.strip()]

    dinner_matches = re.findall(r'Dinner:(.*?)Workouts:', results, re.DOTALL)
    if dinner_matches:
        dinner_names = [name.strip() for name in dinner_matches[0].strip().split('\n') if name.strip()]

    workout_matches = re.findall(r'Workouts:(.*?)$', results, re.DOTALL)
    if workout_matches:
        workout_names = [name.strip() for name in workout_matches[0].strip().split('\n') if name.strip()]

    st.subheader("Recommendations")
    st.markdown("#### Restaurants")
    if restaurant_names:
        for restaurant in restaurant_names:
            st.write(restaurant)
    else:
        st.write("No restaurant recommendations available.")

    st.markdown("#### Breakfast")
    if breakfast_names:
        for breakfast in breakfast_names:
            st.write(breakfast)
    else:
        st.write("No breakfast recommendations available.")

    st.markdown("#### Dinner")
    if dinner_names:
        for dinner in dinner_names:
            st.write(dinner)
    else:
        st.write("No dinner recommendations available.")

    st.markdown("#### Workouts")
    if workout_names:
        for workout in workout_names:
            st.write(workout)
    else:
        st.write("No workout recommendations available.")