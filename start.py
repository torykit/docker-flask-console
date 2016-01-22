#!/usr/bin/python
# coding=utf-8
__author__ = 'torykit@torykit.com'

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello world</h1>'

if __name__=="__main__":
    app.run(debug=True)