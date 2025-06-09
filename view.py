from util.web import *
from pathlib import Path
from util.config import load_config
from util.web import *
import yaml
import json
import pandas as pd
from datetime import date

CONFIG_FILE = "config.yml"

from flask import Flask, render_template, request

app = Flask("Nazwa aplikacji")


@app.route("/template1")
def template1():
    return render_template("template.html")

@app.route("/rate/<currency>/<date_start>/<date_end>")
def rate(currency, date_start, date_end):
    currency = currency.upper()
    date = datetime.today().strftime("%Y-%m-%d")
    return render_template("prices.html",
                           xyz=get_frame(get_json("A", None, date_start, date_end), currency=currency).to_dict(orient="records"),
                           abc=makeplot(get_frame(get_json("A", None, date_start, date_end), currency=currency)),
                           currencies = get_currencies(get_json("A", None, date_start, date_end)),
                           today=date)
if __name__ == "__main__":
    app.run()