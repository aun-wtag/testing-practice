from unittest.mock import patch
import features

# @patch('features.sub.sum')
# @patch('features.add.sum')
# def test(MockAddFunc, MockSubFunc):
#     # res1 = Mock()
#     # res2 = Mock()
#     # res1.sum.return_value = 10
#     # res2.sum.return_value = 20
#     MockAddFunc.return_value = 10
#     MockSubFunc.return_value = 20
#     assert features.add.func() == 10
#     assert features.sub.func() == 20 - 10000000
#     # and you can check that they were actually called
#     # MockAddFunc.assert_called_once()
#     # MockSubFunc.assert_called_once()

@patch('features.transform.process')
@patch('features.fetch.get_data')
def test_run_pipeline(mock_get_data, mock_process):
    mock_get_data.return_value = {'id':1, 'name':'John', 'age':30}
    mock_process.return_value = ['id,1', 'name,John', 'age,30']
    result = features.processor.run_pipeline()
    print(result)
    assert result == ['id,1', 'name,John', 'age,30']