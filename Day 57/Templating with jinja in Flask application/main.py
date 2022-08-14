from flask import Flask, render_template
import random
import requests




app = Flask(__name__)


@app.route("/")
def hello():
    random_number = random.randint(1,10)

    return render_template("index.html", num=random_number)

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    age_url = f"https://api.agify.io?name={name}"
    response = requests.get(url=gender_url)
    gender = response.json()["gender"]
    age_response = requests.get(url=age_url)
    age = age_response.json()["age"]
    return render_template("index.html", gender=gender, age=age, name=name)


if __name__ == "__main__":
    app.run(debug=True)
