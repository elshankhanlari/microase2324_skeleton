from flask import Flask, render_template, request, make_response, jsonify
import requests
import time
import os

app = Flask(__name__, instance_relative_config=True)

LOG_URL = os.environ["LOG_URL"]


@app.route("/concat")
def concat():
    a = request.args.get("a", type=str)
    b = request.args.get("b", type=str)
    if a and b:
        send_log(request.endpoint, [a, b], 200)
        return make_response(jsonify(s=a + b), 200)  # HTTP 200 OK
    else:
        send_log(request.endpoint, [a, b], 400)
        return make_response("Invalid input\n", 400)  # HTTP 400 BAD REQUEST


@app.route("/upper")
def upper():
    a = request.args.get("a", 0, type=str)
    send_log(request.endpoint, [a], 200)
    return make_response(jsonify(s=a.upper()), 200)


@app.route("/lower")
def mul():
    a = request.args.get("a", 0, type=str)
    send_log(request.endpoint, [a], 200)
    return make_response(jsonify(s=a.lower()), 200)


def send_log(op, args, res):
    SERVICE = "str"
    ts = time.time()
    requests.get(LOG_URL + f"/addlog?ts={ts}&s={SERVICE}&op={op}&args={args}&res={res}")


def create_app():
    return app
