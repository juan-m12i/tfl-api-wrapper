import os
import unittest

from tfl_api import TfLAPI, Client, Response
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
    def __init__(self, *args, **kwargs):
        super(TestTfLAPI, self).__init__(*args, **kwargs)
        self.credentials = config.get_credentials()
        self.TfL_no_cred = TfLAPI()
        self.TfL = TfLAPI(self.credentials["app_id"], self.credentials["app_key"])

    def test_get_line_arrivals(self):
        ret = self.TfL.get_line_arrivals("c2", "490003380N")
        self.assertEqual(ret.code, 200)

    def test_get_arrivals(self):
        ret = self.TfL.get_arrivals("490003380N")
        self.assertEqual(ret.code, 200)

    def test_stop_points_by_location(self):
        ret = self.TfL.get_stop_points_by_location(51.5, -0.12)
        self.assertEqual(ret.code, 200)


if __name__ == '__main__':
    unittest.main()
