from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField
from wtforms.validators import DataRequired, url
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_URL = URLField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), url()])
    open_time = TimeField("Open Time e.g. 8AM", validators=[DataRequired()])
    close_time = TimeField("Closing Time e.g 7PM", validators=[DataRequired()])
    cofee_rating = SelectField("Coffee Rating", choices=["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
                               validators=[DataRequired()])
    wifi_rating = SelectField(" Wifi Strength Rating", choices=["💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
                              validators=[DataRequired()])
    power_outlet_rating = SelectField("Power Socket Availability",
                                      choices=["🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
                                      validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', encoding="utf8", mode="a") as csv_file:

            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location_URL.data},"
                           f"{form.open_time.data},"
                           f"{form.close_time.data},"
                           f"{form.cofee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_outlet_rating.data}")
        return redirect(url_for("cafes"))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', encoding="utf8", newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        print(csv_data)
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
