import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os

plt.ion()

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

get_json("A", None, "2024-03-02", "2024-03-05")

with open("util/A_2024-03-02_to_2024-03-05.json", "r") as f:
    file = json.load(f)

def get_frame(json):
    tabpand = {}
    sectab = pd.DataFrame()
    for i in json:
        for o in i.values():
            if isinstance(o, list):
                tabpand[i["effectiveDate"]] = (pd.json_normalize(o))
    for i in tabpand:
        if sectab.empty:
            sectab[i] = tabpand[i].set_index("code")["mid"]
        else:
            sectab[i] = tabpand[i].set_index("code")["mid"]
    sectab_l = sectab.reset_index().melt(id_vars="code", var_name="date", value_name="value")
    return sectab_l

def makeplot(dataset):
    fig, ax = plt.subplots()
    sns.lineplot(data=dataset,
                 x="date",
                 y="value",
                 hue="code",
                 ax = ax)
    plt.show()
makeplot(get_frame(file))