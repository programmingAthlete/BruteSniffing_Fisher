import os
import unittest

from modules.Attack.dghv import usage as dghv_usage
from modules.Attack.rsa import usage as rsa_usage


class TestCryptoAnalysis(unittest.TestCase):

    def test_usage(self):
        rsa_help_message = rsa_usage()
        self.assertEqual(rsa_help_message, """Encrypt and decrypt messages via textbook RSA schema.

	Generate the keys via the command 
		generate_keys -k <bitsize>
		Multiple keys can be generated
	 See the generated keys via the command show_keys
	 Encrypt a message via the command 
		encrypt -m <message>
		At the moment the message can only be decrypted with small keys. The last generated keys is used. At the momentthere is still not option to explicitly choose the key with which to encrypt.
	Decrypt a message via the command
		decrypt message -m <message>
		The last generated keys is used. At the moment there is still not option to explicitly choose the key with which to decrypt.
Get help of a specific command by
	<command> --help

"""
)

        dghv_help_message = dghv_usage()
        self.assertEqual(dghv_help_message, dghv_help_message)
