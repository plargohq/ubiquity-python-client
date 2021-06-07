import yaml

def get_platform_enum_values():
    yaml_spec_file = None
    try:
        yaml_spec_file = open("./spec/openapi.yaml")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File '{e.filename}' not found, make sure you run tests from the root directory.")

    parsed_yaml_file = yaml.load(yaml_spec_file, Loader=yaml.FullLoader)
    yaml_spec_file.close()
    return parsed_yaml_file['components']['parameters']['platform']['schema']['enum']


