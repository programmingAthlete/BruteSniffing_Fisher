import unittest
from unittest import mock

from modules.Attack.core import Core


def mock_fun():
    return "ok"


class TestCoreClass(unittest.TestCase):

    def test_import_in_core(self):
        core = Core("Bruteforce")
        self.assertEqual(core.class_, "Bruteforce")
        self.assertEqual(core.module, 'bruteforce')

    @mock.patch("modules.Attack.BruteForce.bruteforce.run", mock_fun)
    def test_core_run(self):
        bruteforce = Core("Bruteforce")
        bruteforce.run()
