from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


class index_page(FlaskForm):
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "Happy face sad soul"

Bootstrap(app)


@app.route('/')
def home():
    a = index_page()
    if a.validate_on_submit():
        return render_template('login.html')
    return render_template('index.html', button=a)


@app.route('/login', methods=["GET", "POST"])
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
