import os
import json


def configuration_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_path = rf"{dir_path}\\configuration_data.json"
    with open(config_path, "r") as file:
        config_data = file.read()
    return json.loads(config_data)


def env():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_path = rf"{dir_path}\\env.json"
    with open(config_path, "r") as file:
        config_data = file.read()
    return json.loads(config_data)


def valid_test_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_path = rf"{dir_path}\\valid_test_data.json"
    with open(config_path, "r") as file:
        valid_data = file.read()
    return json.loads(valid_data)


def invalid_test_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_path = rf"{dir_path}\\invalid_test_data.json"
    with open(config_path, "r", encoding="utf-8") as file:
        invalid_data = file.read()
    return json.loads(invalid_data)


def validation_error_texts():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_path = rf"{dir_path}\\validation_error_texts.json"
    with open(config_path, "r") as file:
        validation_texts = file.read()
    return json.loads(validation_texts)
