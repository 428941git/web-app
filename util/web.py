import requests

def get_json(tab, date, start, end):
    if start == None and end == None:
        result = requests.get(f"https://api.nbp.pl/api/exchangerates/tables/{tab}/{date}/?format=json")
    if date == None:
        result = requests.get(f"https://api.nbp.pl/api/exchangerates/tables/{tab}/{start}/{end}/?format=json")
    return result.json()


if __name__ == "__main__":
    print(get_json("A", "2025-06-05", None, None))
