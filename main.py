from flask import Flask, request, current_app, jsonify
import json

app = Flask(__name__)

class PostData:
    def __init__(self):
        self.buffer = ""
        self.datatype = ""

postdata = PostData()
print('abcdef')


@app.route('/')
def index():
    return "Welcome to HF GSM Telemetry Page"

@app.route('/poster', methods = ['POST'])
def poster():
    global postdata
    try:
        if request.is_json:
            postdata.buffer = request.get_json()
            postdata.datatype = "JSON"
        else:
            postdata.buffer = request.data
            postdata.datatype = "rawtext"
        print('CDDDD')
        print(postdata.buffer)
        return "OK", 200
    except KeyError:
        return "Something went wrong", 400     #400 - Bad Request


@app.route('/getter', methods = ['GET'])
def getter():
    global postdata
    #TODO - distinguish JSON request from another thingzz
    if postdata.datatype == "JSON":
        return jsonify(postdata.buffer)
    else:
        return postdata.buffer

if __name__ == "__main__":
    app.run()
