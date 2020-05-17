# -*- coding: utf-8 -*-
"""
Created on Thu May 14 12:36:11 2020
Build Website with Python and Flask

@author: SowjanyaG
"""

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ =="__main__":
    app.run(port=5000)