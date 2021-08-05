# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 13:56:57 2021

@author: hrith
"""

from flask import Flask,request,render_template
from joblib import load
app= Flask(__name__)
column=load('onehot.save')
model=load('model.save')

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/y_predict',methods=['Post'])
def y_predict():
    x_test=[[x for x in request.form.values()]]
    print(x_test)
    x_test=column.transform(x_test)
    print(x_test)
    prediction=model.predict(x_test)
    print(prediction)
    output=prediction[0]
    print(output)
    return render_template('index.html',prediction_text='Profit {}'.format(output))

if __name__=='__main__':
    app.run(debug=True)
    