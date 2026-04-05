import features

def mock_add():
    return 1 + 2

def test_add(monkeypatch):
    monkeypatch.setattr(features, 'func', mock_add)
    print(f"Mocked Function Output: {features.func()}")
    assert features.func() == 3

def test_get_todo(mock_response):
    assert features.get_todo() == {'test' : 'dict'}