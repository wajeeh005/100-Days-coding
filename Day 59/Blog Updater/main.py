from flask import Flask, render_template
import requests

json_website = "https://api.npoint.io/c67d1455fa94791892d6"

response = requests.get(url=json_website)
data = response.json()
# print(data)
# id = data[0]["id"]
# title_of = data[0]['title']
# body = data[0]['body']
# subtitle = data[0]["subtitle"]
#
#
# print(id,title)



app = Flask(__name__)



@app.route("/")
def home_page():
    return render_template("index.html", all_data = data)

@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)