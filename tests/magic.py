from unittest.mock import MagicMock

mock = MagicMock()
mock.__str__.return_value = 'Hello'

print(mock)