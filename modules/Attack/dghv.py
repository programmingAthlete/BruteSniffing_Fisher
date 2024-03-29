import ast
import os
import random
import sqlite3

import click
import pydantic
from crypto_pkg.DGHV.dghv import DGHV

path = "modules/Attack/dghv.py"

conn = sqlite3.connect('keys2.db')
c = conn.cursor()


class KeyNotFoundError(Exception):
    """Raised if the no kex is found"""


class DghvKeys(pydantic.BaseModel):
    private: int
    public: int


class Dghv:

    def __str__(self):
        return 'RSA schema attacks'

    @staticmethod
    def run():
        run()

    @staticmethod
    def create_table(c):
        c.execute('CREATE TABLE IF NOT EXISTS keys(schema_name STRING, private_key INT, public_key INT)')

    @staticmethod
    def add_key(c, connection, key, schema_name):
        c.execute(f'INSERT INTO keys(schema_name, private_key, public_key) '
                  f'VALUES ({schema_name}, {int(key.private)}, {int(key.public)})')
        connection.commit()

    @staticmethod
    def show_keys(c):
        c.execute("SELECT * FROM keys")
        return c.fetchall()

    @staticmethod
    def exit(c, connection):
        c.execute("DROP table keys")
        connection.commit()

    @classmethod
    def get_latest_key(cls, c):
        keys = cls.show_keys(c)
        return keys[-1]


def run():
    Dghv.create_table(c)
    print(usage())
    while True:
        try:
            x = str(input("> "))
            if x != "":
                n = f"python {path} {x}"
                print(n)
                os.system(n)
        except KeyboardInterrupt:
            Dghv.exit(c=c, connection=conn)
            break


@click.group
def main():
    """
    CLI manager
    """
    pass


@main.command("generate_keys")
@click.option('-k', '--number_of_bites', help='Number of bits of the private key, - Default = 2700',
              default=100)
@click.option('-t', '--tau', help='Number of components of the public key - Default = 20', default=10)
def generate_keys(number_of_bites=100, tau=10):
    """
    Generate DGHV keys corresponding to k bits prime numbers - for correct decryption use k < 1200. Improvements will
    come in next PR
    """
    private_key = random.getrandbits(number_of_bites)
    public_key = DGHV.generate_public_key(p=private_key, tau=tau)
    print(f"Generated the keys d = {private_key}, e = {public_key}")
    Dghv.add_key(c=c, connection=conn, key=DghvKeys(private=private_key, public=public_key), schema_name="'DGHV'")


@main.command("show_keys")
def show_keys():
    print(Dghv.show_keys(c))


@main.command("encrypt")
@click.option("-m", "--message")
def encrypt(message):
    """
    Encrypt message via DGHV. Message must be without space. Improvement wil come in next PR
    """
    try:
        key = Dghv.get_latest_key(c)
    except KeyNotFoundError:
        print("Generate a key first")
        return
    encrypted = DGHV.encrypt_full_message(message=message, e=int(key[2]))
    print(encrypted)


@main.command("decrypt")
@click.option("-m", "--message", type=str)
def decrypt(message):
    """ Decrypt message via DGHV. Paste the list provided by the encryption with single quotes.
    Decryption reading a file will come in the next PR"""
    try:
        key = Dghv.get_latest_key(c)
    except KeyNotFoundError:
        print("Generate a key first")
        return
    enc_m = ast.literal_eval(message)
    decrypted = DGHV.decrypt_full_message(c=enc_m, p=int(key[1]))
    print(decrypted)


@main.command("help")
def help():
    """
    Display help message
    """
    print(usage())
    os.system(f'python {path} --help')


def usage():
    use = "Encrypt and decrypt messages via textbook RSA schema.\n\n" \
          "\tGenerate the keys via the command \n\t\tgenerate_keys -k <bitsize>\n\t\tMultiple keys can be generated" \
          "\n\t See the generated keys via the command show_keys\n" \
          "\t Encrypt a message via the command \n\t\tencrypt -m <message>\n\t\tAt the moment the message can only be" \
          " an integer number.The last generated keys is used. At the moment" \
          "there is still not option to explicitly choose the key with which to encrypt.\n" \
          "\tDecrypt a message via the command\n\t\tdecrypt message -m <message>\n" \
          "\t\tThe last generated keys is used. At the moment there is still not option to explicitly choose the key " \
          "with which to decrypt.\n" \
          "Get help of a specific command by\n" \
          "\t<command> --help\n\n"
    return use


if __name__ == '__main__':
    main()
