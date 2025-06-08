from util.web import *
from pathlib import Path
from util.config import load_config
from util.web import *
import yaml
import json

CONFIG_FILE = "config.yml"

from flask import Flask, render_template, request

app = Flask("Nazwa aplikacji")


@app.route("/template1")
def template1():
    return render_template("template.html")

@app.route("/rate/<currency>/<date_start>/<date_end>")
def rate(currency, date_start, date_end):
    ap = []
    ap.append(currency)
    currency = [a.upper() for a in ap]
    return render_template("prices.html", abc=makeplot(get_frame(get_json("A", None, date_start, date_end)), currency), xyz="sraka")
if __name__ == "__main__":
    app.run()