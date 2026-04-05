from unittest.mock import Mock
# import unittest.tests as tests
# from features.add import func


mock = Mock(side_effect=ValueError('Mock created and a ValueError was raised'))
# calling tests() again returns another Mock object
# m1 = tests()
# m1.val = 1
# m1.get_val.return_value = 2
#
# print(m1.val)
# print(m1.get_val())

mock.side_effect = [1, 2, 3, 4, 5]

for i in range(5):
    print(mock())