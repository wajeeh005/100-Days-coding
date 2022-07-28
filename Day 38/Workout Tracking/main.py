
import requests
from datetime import datetime

APP_ID = "9369d036"
API_KEY = "d0da53042a2257bc9acf304653cca7c1"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/b81388f9eed7a355e7b0839c2c4aad5b/workoutTracking/workouts"


GENDER = input("male / female / other:  ").lower()
WEIGHT_KG = float(input("Tell me your weight in KG:   "))
HEIGHT_CM = float(input("Tell me your Height in cm:   "))
AGE = int(input("Tell me your age:  "))
exercise_text = input("Which exercise you did? running,walking,workout,etc and how much you did\n for example' i do 6 miles running and 3 miles walking.\n': ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
# print(result)


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

print(sheet_response.text)
