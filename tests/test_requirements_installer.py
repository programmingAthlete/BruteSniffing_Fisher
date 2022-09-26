import os
import unittest

from Setup.check import read_requirements


class TestRequirementsInstaller(unittest.TestCase):

    def test_read_requirements(self):
        base_path = os.path.abspath(__file__).split("BruteSniffing_Fisher")[0]
        requirement_file_path = os.path.join(base_path, "BruteSniffing_Fisher/requirements.txt")
        with open(requirement_file_path, "r") as f:
            lines_list = set([item.strip("\n") for item in f.readlines()])
        r = list(read_requirements())
        self.assertEqual(set(r), lines_list)
