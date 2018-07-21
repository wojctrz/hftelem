from flask import Flask, request, current_app, jsonify
import json

app = Flask(__name__)


buffer = ""

@app.route('/')
def index():
    return "Welcome to HF GSM Telemetry Page"

@app.route('/poster', methods = ['POST'])
def poster():
    global buffer
    try:
        if request.is_json:
            buffer = request.get_json()
        else:
            buffer = request.data
        print('CDDDD')
        print(buffer)
        return "OK", 200
    except KeyError:
        return "Something went wrong", 400     #400 - Bad Request


@app.route('/getter', methods = ['GET'])
def getter():
    global buffer
    #TODO - distinguish JSON request from another thingzz
    return jsonify(buffer)

if __name__ == "__main__":
    app.run()
