from flask import Flask, render_template, request
import requests

json_website = "https://api.npoint.io/c67d1455fa94791892d6"

response = requests.get(url=json_website)
data = response.json()

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

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for post in data:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html",post=requested_post)



@app.route("/contact", methods=["GET", "POST"]
def contact():
    if request.method == "POST":
        form_data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent = True)
    return render_template("contact.html",msg_sent = False)



if __name__ == "__main__":
    app.run(debug=True)