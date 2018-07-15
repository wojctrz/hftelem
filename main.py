from flask import Flask, request, current_app, jsonify
import json

app = Flask(__name__)


class FlightData:
    lat = 0
    lon = 0
    height = 0

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)


fldat = FlightData()
fldat.lat = 1

@app.route('/')
def index():
    return "Welcome to HF GSM Telemetry Page"

@app.route('/poster', methods = ['POST'])
def poster():
    global fldat
    #return str(current_app.xd)
    if request.is_json:
        try:
            content = request.get_json()
            fldat.lat = content['Latitude']
            fldat.lon = content['Longitude']
            fldat.height = content['Height']
            return "OK", 200
        except KeyError:
            return "Something went wrong", 400     #400 - Bad Request

@app.route('/getter', methods = ['GET'])
def getter():
    global fldat
    return fldat.toJSON()

if __name__ == "__main__":
    app.run(debug=True)