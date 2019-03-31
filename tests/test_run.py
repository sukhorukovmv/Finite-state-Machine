import sys
sys.path.append('../src')

import app

import unittest

class TestRun(unittest.TestCase):


      def test_index(self):
        """Начальный тест. Убедимся, что фласк установлен корректно"""
        tester = app.app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


      def test_home(self):
          tester = app.test_client(self)
          response = tester.get('/', content_type='html/text')
          self.assertEqual(response.status_code, 200)
          self.assertEqual(response.data, b'Hello, World!')

if __name__ == '__main__':
  unittest.main()
