import unittest
from src.core import get_message 

class HelloworldTestCase(unittest.TestCase):
    def test_helloworld(self):
        self.assertEqual(get_message(), 'Hello World!')

if __name__ == '__main__':
    unittest.main()

#import pytest

#def setup_module(module):
#    #init_something()
#    pass
#
#def teardown_module(module):
#    #teardown_something()
#    pass
#
#def test_upper():
#    assert 'foo'.upper() == 'FOO'
#
#def test_isupper():
#    assert 'FOO'.isupper()
#
#def test_failed_upper():
#    assert 'foo'.upper() == 'FOo'
