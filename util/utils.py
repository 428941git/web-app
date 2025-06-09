from util.web import get_json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def get_currencies():
    json = get_json("A", "2025-06-05", None, None)
    i = json[0]
    for o in i.values():
        if isinstance(o, list):
            tab = [p["code"] for p in o]
    return tab

def get_frame(json, currency):
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
    final = sectab_l[sectab_l["code"] == currency][["date", "value"]]
    return final


def makeplot(dataset):
    fig, ax = plt.subplots(figsize=(12, 8))

    dataset["date"] = pd.to_datetime(dataset["date"])
    minx = min(dataset["date"])
    maxx = max(dataset["date"])
    xtic = pd.date_range(start=minx, end=maxx, freq='2D')
    ax.set_xticks(xtic)
    plt.xticks(rotation=70, ha='right')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.grid(True, color='#EEEFEF')
    plt.xlim(minx, maxx)

    sns.lineplot(data=dataset,
                 x="date",
                 y="value",
                 ax=ax)
    plt.show()

    return fig

if __name__ == "__main__":
    test_currencies = get_currencies()
    print(test_currencies)
    test_frame = get_frame(get_json("A", None, "2025-03-11", "2025-03-18"), "USD")
    print(test_frame)
    plt.ion()
    test_plot = makeplot(test_frame)
