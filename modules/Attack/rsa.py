import sqlite3

import click
from crypto_pkg.rsa.rsa_scheme import RSA


class Rsa:

    def __str__(self):
        return 'RSA schema attacks'

    @staticmethod
    def run():
        run()

    @staticmethod
    def create_table(c):
        c.execute('CREATE TABLE IF NOT EXISTS keys(private_key INT, public_key INT, modulo INT)')

    @staticmethod
    def add_key(c, connection, key):
        c.execute(f'INSERT INTO keys(private_key, public_key, modulo) '
                  f'VALUES ({key.private_key}, {key.public_key}, {key.modulo})')
        connection.commit()


def run():
    conn = sqlite3.connect('keys.db')
    c = conn.cursor()
    Rsa.create_table(c)


@click.group()
@click.version_option(prog_name='RSA')
def main():
    pass


@main.command()
@click.option('-k', '--number_of_bites')
def generate_keys(conn, c, number_of_bites):
    rsa = RSA(k=number_of_bites)
