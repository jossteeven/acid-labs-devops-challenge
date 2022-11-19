import json
import pickle

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
## Load the model
pickle_model=pickle.load(open('app/pickle_model.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    print("inside api")
    data=request.json['data']
    print(type(data))
    output=pickle_model.predict(np.array(data).reshape(1,-1))
    print(output[0])
    return jsonify("{}".format(output[0]))

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
   
     
