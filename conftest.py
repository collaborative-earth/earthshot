import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--config", action="store", default="/home/circleci/project/SERVICE_ACCT.json"
    )


@pytest.fixture()
def config_path(pytestconfig):
    return pytestconfig.getoption("config")
