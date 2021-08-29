import unittest

from modules.controller import max_index


class TestController(unittest.TestCase):

    def test_max_index_helper_fun(self):
        d = {1: "hello", 98: "hello world"}
        result = max_index(d)
        self.assertEqual(result, 1)
