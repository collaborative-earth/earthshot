import ee
import json
import pytest


def test_valid_config(config_path):
    with open(config_path) as f:
        config = json.load(f)


def test_ee_api_connection(config_path):
    with open(config_path) as f:
        config = json.load(f)
    service_acct = config["client_email"]
    ee.Initialize(ee.ServiceAccountCredentials(service_acct, config_path))
