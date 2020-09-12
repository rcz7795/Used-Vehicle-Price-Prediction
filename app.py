from flask import Flask, request, render_template, jsonify
from flask_cors import cross_origin
import datetime as dt

import CarPricePrediction as tm

app = Flask(__name__)

@app.route('/get_fuel_names', methods=['GET'])
def get_fuel_names():
    response = jsonify({
        'fuel': tm.get_fuel_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_title_names', methods=['GET'])
def get_title_names():
    response = jsonify({
        'title': tm.get_title_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_transmission_names', methods=['GET'])
def get_transmission_names():
    response = jsonify({
        'transmission': tm.get_transmission_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_drive_names', methods=['GET'])
def get_drive_names():
    response = jsonify({
        'drive': tm.get_drive_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_car_type_names', methods=['GET'])
def get_car_type_names():
    response = jsonify({
        'car_type': tm.get_car_type_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
# @cross_origin()
def predict():
    if request.method == "POST":
        fuel = request.form.get('fuel')
        title = request.form.get('title')
        transmission = request.form.get('transmission')
        drive = request.form.get('drive')
        car_type = request.form.get('car_type')
        cylinder = request.form.get('cylinder')
        odometer = request.form.get('odometer')
        description = request.form.get('description')
        dop = request.form.get('dop')

        description_length = len(description)
        age = CalculateAge(dt.datetime.strptime(dop, '%Y-%m-%d'))

        prediction = round(float(tm.predict_car_price(fuel, title, transmission, drive, car_type, cylinder, odometer, description_length, age), 2))

        return render_template("index.html", prediction_text="The estimated car price is $" + str(prediction))

    return render_template("index.html")

def CalculateAge(dob):
    today = dt.datetime.date.today()
    years = today.year - dob.year
    if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
        years -= 1
    return years

if __name__ == "__main__":
    tm.load_saved_attributes()
    app.run(debug=True)