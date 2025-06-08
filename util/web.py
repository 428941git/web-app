import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os
from datetime import datetime, timedelta



plt.ion()
def get_json(tab, date, start, end):
    if start == None and end == None:
        result = requests.get(f"https://api.nbp.pl/api/exchangerates/tables/{tab}/{date}/?format=json")
    if date == None:
        result = requests.get(f"https://api.nbp.pl/api/exchangerates/tables/{tab}/{start}/{end}/?format=json")
    return result.json()

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
            getcode = tabpand[i][["currency", "code"]]
        else:
            sectab[i] = tabpand[i].set_index("code")["mid"]
    sectab_l = sectab.reset_index().melt(id_vars="code", var_name="date", value_name="value")
    sectab_l = sectab_l.merge(getcode, left_on="code", right_on="code", how="inner")
    return sectab_l


def makeplot(dataset, code):
    fig, ax = plt.subplots(figsize=(12, 8))

    dataset["date"] = pd.to_datetime(dataset["date"])
    minx = min(dataset["date"])
    maxx = max(dataset["date"])
    xtic = pd.date_range(start=minx, end=maxx, freq='5D')
    ax.set_xticks(xtic)
    plt.grid(True, color='#EEEFEF')
    plt.xlim(minx, maxx)

    sns.lineplot(data=dataset[dataset["code"].isin(code)],
                 x="date",
                 y="value",
                 hue="currency",
                 ax=ax)
    plt.legend(bbox_to_anchor=(1.15, 1), loc="upper right")
    plt.show()

def cr_plot(tab, date, start, end, code):
    makeplot(get_frame(get_json(tab, date, start, end)), code)

if __name__ == "__main__":
    cr_plot("A", None, "2024-12-02", "2025-01-01", ["THB"])
