#!/usr/bin/env python3

from flask import Flask, jsonify
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>', 200

@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(parameter)  # This will output to console
    return parameter, 200

@app.route('/count/<int:parameter>')
def count(parameter):
    return '\n'.join(str(i) for i in range(parameter)) + '\n', 200

@app.route('/math/<int:left>/<operation>/<int:right>')
def math(left, operation, right):
    if operation == '+':
        result = left + right
    elif operation == '-':
        result = left - right
    elif operation == '*':
        result = left * right
    elif operation == 'div':
        result = left / right
    elif operation == '%':
        result = left % right
    else:
        return "Invalid operation", 400
    
    return str(result), 200

if __name__ == '__main__':
    app.run(debug=True)



































