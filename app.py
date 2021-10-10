# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:20:51 2021

@author: Abhinash
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 0)
    output = int(output)
    if output==1:
        return render_template('index.html', prediction_text='Patient is Covd Positive')
    else:
         
        return render_template('index.html', prediction_text='Patient is Covd Negative')

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
