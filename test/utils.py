import json
import yaml
import socket

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

def get_platforms_v1():
    platforms_json_file = read_file("./test/platforms_v1.json")
    platforms = json.load(platforms_json_file)

    platforms_json_file.close()
    return platforms

def get_open_port():
    s = socket.socket()
    s.bind(('', 0))
    return s.getsockname()[1]
