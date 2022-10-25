import json
import os
import sqlite3

import click
from crypto_pkg.rsa.rsa_scheme import RSA

path = "modules/Attack/rsa.py"

conn = sqlite3.connect('keys.db')
c = conn.cursor()


class Rsa:

    def __str__(self):
        return 'RSA schema attacks'

    @staticmethod
    def run():
        run()

    @staticmethod
    def create_table(c):
        c.execute('CREATE TABLE IF NOT EXISTS keys(schema_name STRING, private_key INT, public_key INT, modulo INT)')

    @staticmethod
    def add_key(c, connection, key, schema_name):
        c.execute(f'INSERT INTO keys(schema_name, private_key, public_key, modulo) '
                  f'VALUES ({schema_name}, {key.private}, {key.public}, {key.modulus})')
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
    Rsa.create_table(c)
    print(usage())
    while True:
        try:
            x = str(input("> "))
            if x != "":
                n = f"python {path} {x}"
                print(n)
                os.system(n)
        except KeyboardInterrupt:
            Rsa.exit(c=c, connection=conn)
            break


@click.group
def main():
    """
    CLI manager
    """
    pass


@main.command("generate_keys")
@click.option('-k', '--number_of_bites', default=20)
def generate_keys(number_of_bites=20):
    """
    Generate RSA keys corresponding to k bits prime numbers - for correct decryption use k < 50. Improvements will
    come in next PR
    """
    rsa = RSA(k=int(number_of_bites))
    primes = rsa.generate_primes()
    print(f"Generated the primes p = {primes.p.base_10} and q = {primes.q.base_10}")
    rsa_keys = rsa.generate_keys(p=primes.p, q=primes.q)
    print(f"Generated the keys d = {rsa_keys.private}, e = {rsa_keys.public}, N = {rsa_keys.modulus}")
    Rsa.add_key(c=c, connection=conn, key=rsa_keys, schema_name="'RSA'")


@main.command("show_keys")
def show_keys():
    """
    Display all generated keys
    """
    print(Rsa.show_keys(c))


@main.command("encrypt")
@click.option("-m", "--message")
def encrypt(message):
    """
    Encrypt message via TextBook RSA. Message must be without space. Improvement wil come in next PR
    """
    key = Rsa.get_latest_key(c)
    encrypted = RSA.encrypt_message(message=message, e=key[2], n=key[3])
    print(encrypted)


@main.command("decrypt")
@click.option("-m", "--message")
def decrypt(message):
    """ Decrypt message via TextBook RSA. Paste the list provided by the encryption with single quotes.
    Decryption reading a file will come in the next PR"""
    key = Rsa.get_latest_key(c)

    message_list = json.loads(message)
    decrypted = RSA.decrypt_message(cipher_text=message_list, d=key[1], n=key[3])
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
