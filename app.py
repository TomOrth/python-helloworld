from flask import Flask
from flask import jsonify
import logging

logging.basicConfig(
            filename="app.log",
            filemode="w",
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.DEBUG,
            datefmt='%Y-%m-%d %H:%M:%S')

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    logging.debug("STATUS ENPOINT REACHED")
    return jsonify({"result": "OK - healthy"})

@app.route("/metrics")
def metrics():
    logging.debug("STATUS ENPOINT REACHED")
    return jsonify({"data": {"UserCount": 140, "UserCountActive": 23}})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000')
