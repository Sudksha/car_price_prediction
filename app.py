
from flask import Flask,jsonify, request
import numpy as np
import joblib
import pandas as pd
import numpy as np

import pickle


import flask
app= Flask(__name__,template_folder='template')
model = joblib.load('model.pkl')

@app.route('/',methods=['GET'])

def home():
    return flask.render_template('index.html')
    
    
@app.route("/predict", methods=["POST"])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Present_Price=float(request.form['Present_Price'])
        
        Owner=int(request.form['Owner'])
        Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
        if(Fuel_Type_Petrol=='Petrol'):
                Fuel_Type_Petrol=1
                Fuel_Type_Diesel=0
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        Year=2020-Year
        Seller_Type_Individual=request.form['Seller_Type_Individual']
        if(Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0	
        Transmission_Mannual=request.form['Transmission_Mannual']
        if(Transmission_Mannual=='Mannual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0
        prediction=model.predict([[Present_Price,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
        output=round(prediction[0],2)
        if output<0:
            return flask.render_template('result.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return flask.render_template('result.html',prediction_text="{} Lakh".format(output))
    else:
        return flask.render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)