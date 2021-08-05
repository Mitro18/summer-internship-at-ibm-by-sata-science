# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 15:42:00 2021

@author: hrith
"""

from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return("Hello Internz")
@app.route('/data/')
def fun():
    print("i am new")
    return('this is debug call')

if __name__=='__main__':
    app.run(debug=True)
