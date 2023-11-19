from flask import Flask, render_template, request, make_response, jsonify
import requests
import time
import os

LOG_URL = os.environ["LOG_URL"]
app = Flask(__name__, instance_relative_config=True)


@app.route("/add")
def add():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    if a and b:
        send_log(request.endpoint, [a, b], 200)
        return make_response(jsonify(s=a + b), 200)  # HTTP 200 OK
    else:
        send_log(request.endpoint, [a, b], 400)
        return make_response("Invalid input\n", 400)  # HTTP 400 BAD REQUEST


# add other routes here


@app.route("/sub")
def sub():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    if a and b:
        send_log(request.endpoint, [a, b], 200)
        return make_response(jsonify(s=a - b), 200)  # HTTP 200 OK
    else:
        send_log(request.endpoint, [a, b], 400)
        return make_response("Invalid input\n", 400)  # HTTP 400 BAD REQUEST


@app.route("/mul")
def mul():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    if a and b:
        send_log(request.endpoint, [a, b], 200)
        return make_response(jsonify(s=a * b), 200)  # HTTP 200 OK
    else:
        send_log(request.endpoint, [a, b], 400)
        return make_response("Invalid input\n", 400)  # HTTP 400 BAD REQUEST


@app.route("/div")
def div():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    if a and b:
        send_log(request.endpoint, [a, b], 200)
        return make_response(jsonify(s=a / b), 200)  # HTTP 200 OK
    else:
        send_log(request.endpoint, [a, b], 400)
        return make_response("Invalid input\n", 400)  # HTTP 400 BAD REQUEST


@app.route("/mod")
def mod():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    if a and b:
        send_log(request.endpoint, [a, b], 200)
        return make_response(jsonify(s=a / b), 200)  # HTTP 200 OK
    else:
        send_log(request.endpoint, [a, b], 400)
        return make_response("Invalid input\n", 400)  # HTTP 400 BAD REQUEST


def send_log(op, args, res):
    SERVICE = "math"
    ts = time.time()
    requests.get(LOG_URL + f"/addlog?ts={ts}&s={SERVICE}&op={op}&args={args}&res={res}")


def create_app():
    return app
