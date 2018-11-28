from flask import Flask
import json
import os
import time, threading

app = Flask(__name__)

data = []
DATAFOLDER = "data/"


def update_json():
    files = os.listdir(DATAFOLDER)
    for name in files:
        if "history" in name:
            f = open(DATAFOLDER + "" + name, "r")
            x = f.read()
            f.close()

            if x not in data:
                data.append(json.loads(x))
    threading.Timer(10, update_json).start()


@app.route("/")
def index():
    return "Invalid API endpoint"


@app.route("/api/get_flights")
def get_flights():
    return json.dumps(data)


if __name__ == "__main__":
    update_json()
    app.run(port=1337)
