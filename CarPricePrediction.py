import pickle
import json
import numpy as np
from os import path

fuel_values = None
title_values = None
transmission_values = None
drive_values = None
car_type = None
model = None

def load_saved_attributes():

    global fuel_values
    global title_values
    global transmission_values
    global drive_values
    global car_type_values
    global model

    with open("columns.json", "r") as f:
        resp = json.load(f)
        fuel_values = resp["fuel"]
        title_values = resp["title"]
        transmission_values = resp["transmission"]
        drive_values = resp["drive"]
        car_type_values = resp["car_type"]

    model = pickle.load(open("car_price_predictor.pickle", "rb"))

def get_fuel_names():
    return fuel_values

def get_title_names():
    return title_values

def get_transmission_names():
    return transmission_values

def get_drive_names():
    return drive_values

def get_car_type_names():
    return car_type_values


def predict_car_price(fuel, title, transmission, drive, car_type, cylinders, odometer, description_Length, age):
    try:
        fuel_index = fuel_values.index(fuel)
        title_index = title_values.index(title)
        transmission_index = transmission_values.index(transmission)
        drive_index = drive_values.index(drive)
        car_type_index = car_type_values.index(car_type)

    except:
        fuel_index = -1
        title_index = -1
        transmission_index = -1
        drive_index = -1
        car_type_index = -1

    fuel_array = np.zeros(len(fuel_values))
    if fuel_index >= 0:
        fuel_array[fuel_index] = 1

    title_array = np.zeros(len(title_values))
    if title_index >= 0:
        title_array[title_index] = 1

    transmission_array = np.zeros(len(transmission_values))
    if transmission_index >= 0:
        transmission_array[transmission_index] = 1

    drive_array = np.zeros(len(drive_values))
    if drive_index >= 0:
        drive_array[drive_index] = 1

    car_type_array = np.zeros(len(car_type_values))
    if car_type_index >= 0:
        car_type_array[car_type_index] = 1

    fuel_array = fuel_array[:-1]
    title_array = title_array[:-1]
    transmission_array = transmission_array[:-1]
    drive_array = drive_array[:-1]
    car_type_array = car_type_array[:-1]

    sample = np.concatenate((fuel_array, title_array, transmission_array, drive_array, car_type_array,np.array([cylinders, odometer, description_Length, age])))

    return model.predict(sample.reshape(1,-1))[0]


if __name__ == '__main__':
    load_saved_attributes()
else:
    load_saved_attributes()
