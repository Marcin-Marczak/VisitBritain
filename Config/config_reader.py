import os
import json


def get_config_data(config_file):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_path = rf"{dir_path}\\{config_file}"
    with open(config_path, "r", encoding="utf-8") as file:
        config_data = file.read()
    return json.loads(config_data)
