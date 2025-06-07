import requests
import pandas as pd
import numpy as np
import json
import os

def get_json(tab, date, start, end):
    if start == None and end == None:
        result = requests.get(f"https://api.nbp.pl/api/exchangerates/tables/{tab}/{date}/?format=json")
        folder = r"/Users/nienawidzeczarnoskorych/PycharmProjects/PythonProject/.venv/Python pliki/currency-app/util"
        path = os.path.join(folder, f"{tab}_{date}.json")
        with open(path, "w") as f:
            json.dump(result.json()[0], f, indent=4)
    if date == None:
        result = requests.get(f"https://api.nbp.pl/api/exchangerates/tables/{tab}/{start}/{end}/?format=json")
        folder = r"/Users/nienawidzeczarnoskorych/PycharmProjects/PythonProject/.venv/Python pliki/currency-app/util"
        path = os.path.join(folder, f"{tab}_{start}_to_{end}.json")
        with open(path, "w") as f:
            json.dump(result.json(), f, indent=4)
get_json("A", None, "2024-03-02", "2024-04-02")
with open("util/A_2024-03-02_to_2024-04-02.json", "r") as f:
    file = json.load(f)
def get_frame(json):
    tabpand = []
    for i in json:
        for o in i.values():
            if isinstance(o, list):
                tabpand.append(pd.json_normalize(o))
    print(tabpand[0])
get_frame(file)