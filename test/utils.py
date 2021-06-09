import json
import yaml

def read_file(path):
    try:
        fd = open(path)
        return fd
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File '{e.filename}' not found, make sure you run tests from the root directory.")

def get_platform_enum_values():
    yaml_spec_file = read_file("./spec/openapi.yaml")

    parsed_yaml_file = yaml.load(yaml_spec_file, Loader=yaml.FullLoader)
    yaml_spec_file.close()
    return parsed_yaml_file['components']['parameters']['platform']['schema']['enum']

