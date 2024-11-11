import os
import requests
from dotenv import load_dotenv
from datetime import datetime

# global variables 
GENDER = "Male"
WEIGHT_KG = "65"
HEIGHT_CM = "185"
AGE = 22


# load env variables 
load_dotenv()


# get env variables 
app_id = os.getenv("APP_ID")
api_key = os.getenv("NUTRITION_API_KEY")
bearer_token = os.getenv("SHEETY_BEARER_TOKEN")

# exercise endpoint
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/04635aeb0e71e1bfd4d64ec47e4fa49f/myWorkoutSpreadsheet/workouts"
exercise_text = input("Tell me which exercises you did: ")
# exercies parameters 
parameters = {
    "query" : exercise_text,
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age" : AGE,
    "gender" : GENDER,
}

headers = {
    "x-app-id": app_id,
    "x-app-key": api_key,
}

# sheety authentication headers
sheety_headers = {
    "Authorization": f"Bearer {bearer_token}"
    }

# get api
response = requests.post(exercise_endpoint,json=parameters,headers=headers)
result = response.json()
print(result)

# get data from sheety
today_date = datetime.now().strftime("%d/%m/%Y")
# print(today_date)
current_time = datetime.now().strftime("%X")
# print(current_time)

response = requests.get(url=sheety_endpoint)
response.raise_for_status()
data = response.json()
print(data)

# get single exercose fromt the list of exercises
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    
    
sheet_response = requests.post(sheety_endpoint,json=sheet_inputs,headers=bearer_token)
print(sheet_response.text)


# how our nutrionox break down the senetence and take the valuable information 
# When you send a sentence describing your exercise (e.g., "running and cycling") to the Nutritionix API via a POST request, the API uses Natural Language Processing (NLP) to interpret the sentence and break it down into structured data that it can understand. Specifically, it identifies exercise activities, their durations, and other relevant information (like calories burned, if possible).