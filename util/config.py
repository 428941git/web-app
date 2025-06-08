import yaml

def load_config(file_path='config.yml'):
    with open(file_path, 'r', encoding="utf-8") as f:
        return yaml.safe_load(f)
