from features import fetch_data, get_data

def test_api_get(mock_requests_get):
    todo = get_data()
    print(f'Returned json: {todo.json()}')
    assert todo.json() == {
        "userId": 1,
        "id": 1,
        "title": "test todo",
        "completed": False
    }

def test_api_failure(mock_request_get_failure):
    status_code = fetch_data()
    assert status_code == 404