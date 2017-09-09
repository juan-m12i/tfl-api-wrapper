import os
import unittest

from tfl-api import TfLAPI, Client, Response
from cfg import config


class TestClient(unittest.TestCase):
    def test_post(self):
        self.assertRaises(NotImplementedError, Client.post)

    # def test_get(self):
        # self.assertEqual(1, 2)


class TestResponse(unittest.TestCase):
    def test_response(self):
        res = Response(200, {'hello': 'test'})
        self.assertEqual(res.code, 200)
        self.assertEqual(res.data, {'hello': 'test'})


class TestTfLAPI(unittest.TestCase):
    def __init__():
        self.credentials = config.get_credentials()
        self.TfL_no_cred = TflAPI()
        self.TfL = TfLAPI(credentials["app_id"], credentials["app_key"])

    def test_no_key_raises_error(self):
        self.assertRaises(ValueError, TfLAPI)

    def test_key_on_env_var(self):
        os.environ['COMPANY_HOUSE_API_KEY'] = 'test'
        api = CompanyHouseAPI()
        self.assertEqual(api._key, 'test')



if __name__ == '__main__':
    unittest.main()
