import json
import pickle

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)

## Load the pickle_model.pkl model proposed
pickle_model=pickle.load(open('pickle_model.pkl','rb'))

## Defining the root endpoint to expose a web UI to use the predition model
@app.route('/')
def home():
    return render_template('home.html')

## Defining the /predict_api REST API endpoint to expose the model
@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    output=pickle_model.predict(np.array(data).reshape(1,-1))
    print(output[0])
    return jsonify("{}".format(output[0]))

## Defining the /predict_api to be used by the UI already defined
@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    output=pickle_model.predict(np.array(data).reshape(1,-1))
    print(output)
    return render_template("home.html",prediction_text="La probabilidad de retraso es: {}".format(output))



if __name__=="__main__":
    app.run(debug=True)
   
     
