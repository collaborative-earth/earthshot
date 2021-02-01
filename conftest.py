import ee
import json
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--config",
        action="store",
        default="/home/circleci/project/SERVICE_ACCT.json",
        help="Path to Google service account config.",
    )
    parser.addoption(
        "--interactive",
        action="store_true",
        default=False,
        help="Use interactive Google authentication session. MUST also call option -s.",
    )


@pytest.fixture(scope="session")
def authenticate_gee(pytestconfig):
    """This function is designed to support interactive Google auth flow for
    running tests locally, and also to support authentication via a service
    account configuration file.

    NOTE: to use interactive authentication flow, users should call pytest using
    both the -s and --interactive options, e.g. as:

    pytest -s --interactive .
    """
    if pytestconfig.getoption("interactive"):
        ee.Authenticate()
        ee.Initialize()
    else:
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
