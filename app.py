from flask import Flask, request, jsonify
from flask.helpers import send_file

app = Flask(__name__, static_url_path='/', static_folder='web')

@app.route("/")
def indexPage():
     return send_file("web/index.html")

@app.route("/calculate")
def calculate():
    operation = request.args.get('operation', type=str)
    num1 = request.args.get('num1', default=0, type=float)
    num2 = request.args.get('num2', default=0, type=float)
    
    try:
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify(error="Cannot divide by zero"), 400
            result = num1 / num2
        else:
            return jsonify(error="Invalid operation"), 400
    except Exception as e:
        return jsonify(error=str(e)), 500

    return jsonify(result=result)