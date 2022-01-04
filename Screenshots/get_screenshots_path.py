import os


def get_screenshots_path():
    screenshots_path = os.path.dirname(os.path.realpath(__file__))
    return screenshots_path
