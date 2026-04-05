# tests/conftest.py
import pytest
from unittest.mock import patch, Mock, MagicMock

import requests.exceptions


@pytest.fixture
def mock_requests_get():
    with patch('features.fetch.requests.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "userId": 1,
            "id": 1,
            "title": "test todo",
            "completed": False
        }
        mock_get.return_value = mock_response
        print("Setting up mock_get...")
        yield mock_get
        print("Tearing down mock_get...")

@pytest.fixture
def mock_request_get_failure():
    with patch('features.fetch.requests.get') as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError("Simulated Connection Error for Testing.")
        yield mock_get

@pytest.fixture
def mock_response(monkeypatch):
    def mock_get(*args, **kwargs):
        res =  MagicMock()
        res.json.return_value = {'test': 'dict'}
        return res

    monkeypatch.setattr(requests, 'get', mock_get)

def pytest_addoption(parser):
    parser.addoption(
        "--stringinput",
        action="append",
        default=[],
        help="list of stringinputs to pass to test functions",
    )

# metafunc object inspects requesting test context
def pytest_generate_tests(metafunc):
    if "stringinput" in metafunc.fixturenames:
        metafunc.parametrize("stringinput", metafunc.config.option.stringinput)
        # under the hood:
        # metafunc.parametrize("stringinput", ["test@example.com", "invalid_email"])
