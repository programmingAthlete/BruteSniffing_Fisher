import unittest

from modules.Attack.core import Core


class TestCoreClass(unittest.TestCase):

    def test_import_in_core(self):
        core = Core("Bruteforce")
        self.assertEqual(core.class_, "Bruteforce")
        self.assertEqual(core.module, 'bruteforce')

    def test_core_run(self):
        bruteforce = Core("Bruteforce")
        bruteforce.run()
