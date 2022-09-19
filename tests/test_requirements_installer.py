import unittest

from Setup.check import read_requirements


class TestRequirementsInstaller(unittest.TestCase):

    def test_read_requirements(self):
        r = list(read_requirements())
        self.assertEqual(r, ['requests==2.26.0', 'nmap==0.0.1', 'netaddr==0.8.0', 'bs4', 'click==8.1.3',
                             'pydantic==1.10.2', 'git+https://github.com/programmingAthlete/crypto_pkg'])
