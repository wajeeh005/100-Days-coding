from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length
from flask_bootstrap import bootstrap

class LoginForm(FlaskForm):
    email = StringField(label='Email',validators=[DataRequired(), Email()])
    password = PasswordField(label='Password',validators=[DataRequired(),Length(min=8)])
    submit = SubmitField(label="Log In")



app = Flask(__name__)
app.secret_key = "Happy face sad soul"
bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login',methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@gmail.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    # login_form.validate_on_submit()
    return render_template('login.html', form=login_form)

if __name__ == "__main__":
    app.run(debug=True)
