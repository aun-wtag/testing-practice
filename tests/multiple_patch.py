from unittest.mock import patch, DEFAULT, MagicMock

import features.processor as processor

@patch.multiple(
    'features.processor',
    get_data=DEFAULT,
    process=DEFAULT
)
def test_run_pipeline(**kwargs):
    get_data = kwargs['get_data']
    process = kwargs['process']
    fake_data = {'id': 1, 'name': 'Alice', 'age': 30}
    get_data.return_value = fake_data
    process.return_value = ['id,1', 'name,Alice', 'age,30']
    assert processor.run_pipeline() == ['id,1', 'name,Alice', 'age,30']
    get_data.assert_called_once()
    process.assert_called_once_with(fake_data)

# def test_run_pipeline():
#     with patch.multiple(
#         'features.processor',
#         get_data=DEFAULT,
#         process=DEFAULT
#     ) as mocks:
#         mocks['get_data'].return_value = {'id':1, 'name':'Bob'}
#         mocks['process'].return_value = ['id,1', 'name,Bob']
#         assert processor.run_pipeline() == ['id,1', 'name,Bob']
#         mocks['get_data'].assert_called_once()
#         mocks['process'].assert_called_once_with({'id':1, 'name':'Bob'})
#

### WORKS
# thing = object()
# other = object()
# @patch.multiple('tests.multiple_patch', thing=DEFAULT, other=DEFAULT)
# def test_function(**kwargs):
#     thing = kwargs['thing']
#     other = kwargs['other']
#     assert isinstance(thing, MagicMock)
#     assert isinstance(other, MagicMock)
