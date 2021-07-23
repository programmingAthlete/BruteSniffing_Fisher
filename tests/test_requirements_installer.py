import unittest

from Setup.check import read_requirements


class TestRequirementsInstaller(unittest.TestCase):

    def test_read_requirements(self):
        r = list(read_requirements())
        self.assertEqual(r,['requests', 'beautifulsoup4', 'netaddr', 'nmap'] )