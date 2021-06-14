import json
import yaml

def read_file(path):
    try:
        fd = open(path)
        return fd
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File '{e.filename}' not found, make sure you run tests from the root directory.")

def get_platforms():
    platforms_json_file = read_file("./test/platforms.json")
    platforms = json.load(platforms_json_file)

    platforms_json_file.close()
    return platforms

