from flask import Flask, render_template, request, make_response, jsonify
import requests

app = Flask(__name__, instance_relative_config=True)


@app.route("/addlog")
def addLog():
    ts = request.args.get("ts", type=str)
    s = request.args.get("s", type=str)
    op = request.args.get("op", type=str)
    args = request.args.get("args", type=str)
    res = request.args.get("res", type=str)

    with open(f"{s}.txt", "w") as my_file:
        my_file.write(f"{s}| timestamp:{ts} operation:{op} args:{args} result:{res} ")
        return make_response(jsonify(None), 200)
    return make_response(jsonify(None), 400)


@app.route("/getLog/<srv>")
def getLog(srv):
    logs_file = open(f"{srv}.txt", "r").read()
    return make_response(jsonify(logs_file), 200)


def create_app():
    return app
