import ee
import json
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--config", action="store", default="/home/circleci/project/SERVICE_ACCT.json"
    )


@pytest.fixture(scope="session")
def config_path(pytestconfig):
    return pytestconfig.getoption("config")


@pytest.fixture(scope="session")
def authenticate_gee(config_path):
    with open(config_path) as f:
        config = json.load(f)
    service_acct = config["client_email"]
    ee.Initialize(ee.ServiceAccountCredentials(service_acct, config_path))
