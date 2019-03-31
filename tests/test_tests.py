import unittest
from src.core import get_message 

class HelloworldTestCase(unittest.TestCase):
    def test_helloworld(self):
        self.assertEqual(get_message(), 'Hello World!')

if __name__ == '__main__':
    unittest.main()

