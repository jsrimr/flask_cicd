import unittest
from app import app
import requests
import json

### https://blog.nerdfactory.ai/2019/04/04/flask-unittest.html 참고
class UnitTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.domain = 'http://localhost:5000/'

    def test_hello(self):
        res = self.app.get('/')
        data = res.get_data().decode()
        self.assertEqual('hello!', data)

if __name__ == '__main__':
    unittest.main()