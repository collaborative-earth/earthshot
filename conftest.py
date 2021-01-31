import ee
import json
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--config", action="store", default="/home/circleci/project/SERVICE_ACCT.json"
    )


@pytest.fixture(scope="session")
def authenticate_gee(pytestconfig):
    try:
        config_path = pytestconfig.getoption("config")
        with open(config_path) as f:
            config = json.load(f)
    except FileNotFoundError as e:
        raise ValueError(
            f"Service account config, {config_path}, not found. Please ensure the "
            "path provided to --config command line argument is correct."
        )
    service_acct = config["client_email"]
    ee.Initialize(ee.ServiceAccountCredentials(service_acct, config_path))
