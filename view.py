from flask import Flask, render_template, request
from util.utils import get_currencies
from load import cr_plot, cr_table
from datetime import datetime
app = Flask("Nazwa aplikacji")


@app.route("/")
def home_page():
    datemin = "2002-01-02"
    datemax = datetime.today().strftime("%Y-%m-%d")
    return render_template("prices.html",
                           currencies=get_currencies(),
                           today=datemax,
                           datem = datemin)

@app.route("/rate/<currency>/<date_start>/<date_end>")
def rate(currency, date_start, date_end):
    currency = currency.upper()
    datemin = "2002-01-02"
    datemax = datetime.today().strftime("%Y-%m-%d")
    return render_template("prices.html",
                           table=cr_table(date_start, date_end, currency),
                           chart=cr_plot(date_start, date_end, currency),
                           currencies = get_currencies(),
                           today=datemax,
                           datem=datemin)


if __name__ == "__main__":
    app.run()