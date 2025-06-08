from util.web import *
from pathlib import Path
import yaml

with open("config.yml", 'r', encoding='utf-8') as lf:
    data = yaml.safe_load(lf)

makeplot(get_frame(get_json("A", None, "2023-02-20", "2023-03-20")), "THB")