from unittest.mock import patch, Mock
import requests.exceptions
from features.fetch import fetch_data

# testing connection fail
@patch('features.fetch.requests.get')
def test_failure(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError("Simulated Connection Error for Testing.")
    status = fetch_data()
    assert status == 404

@patch('features.fetch.requests.get')
def test_success(mock_get):
    mock_get.return_value = Mock(status_code=200)
    assert fetch_data() == 200 # expected success