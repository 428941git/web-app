from util.web import *
from pathlib import Path
import yaml

with open("config.yml", 'r', encoding='utf-8') as lf:
    data = yaml.safe_load(lf)

makeplot(get_frame(get_json(data["table"], None, data["start_date"], data["end_date"])), [c.upper() for c in data["currencies"]])