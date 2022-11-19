import json
import pickle

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
## Load the model
pickle_model=pickle.load(open('pickle_model.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    output=pickle_model.predict(np.array(data).reshape(1,-1))
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    print("aqui")
    data=[float(x) for x in request.form.values()]
    print(data)
    output=pickle_model.predict(np.array(data).reshape(1,-1))
    print(output)
    return render_template("home.html",prediction_text="La probabilidad de retraso es: {}".format(output))



if __name__=="__main__":
    app.run(debug=True)
   
     
