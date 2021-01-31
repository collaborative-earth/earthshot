import ee
import json


def test_valid_config(config_path):
    with open(config_path) as f:
        config = json.load(f)


def test_ee_api_connection(authenticate_gee):
    """This function makes use of the authenticate_gee fixture as-is."""
