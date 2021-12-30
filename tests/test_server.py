import unittest
import logging
from server import app

class TestFoo(unittest.TestCase):

    def test_alive_request(self):
        tester = app.test_client(self)
        response = tester.get('/alive')
        self.assertEqual(response.status_code, 202)
        
    def test_request_url_wml(self):
        tester = app.test_client(self)
        response = tester.get('/api_v1/card/WML')
        logging.info(f'Message from server {response.get_json()}')
        self.assertEqual(response.status_code, 200)
        