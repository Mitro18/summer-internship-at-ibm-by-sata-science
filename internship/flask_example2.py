# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 11:43:59 2021

@author: hrith
"""

from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def hello():
    return("Hello Internz")
@app.route('/admin')
def hello_admin():
    return("Hello i am admin")
@app.route('/data/<id>')
def id_data(id):
    return("Hello your id is %s" % id)
@app.route('/user/<name>')
def user_name(name):
    if name=="Hrithik":
        return redirect(url_for('hello_admin'))
    else:
        return('Your name is %s' % name)
    
if __name__=='__main__':
    app.run(debug=True)
    