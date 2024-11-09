import os
import requests
from dotenv import load_dotenv

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

# exercise endpoint
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
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

# get api
response = requests.post(exercise_endpoint,json=parameters,headers=headers)
result = response.json()
print(result)