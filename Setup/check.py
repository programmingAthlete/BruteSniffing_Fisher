import Setup.setup as setup
import Includes.includes as includes
from importlib import import_module
import os
import sys
import time

def pip_installation():
    '''
    Checks is pip is intalled, if it istalls it
    :return:  void
    '''
    version = ''
    os.system('python --version "$1" > tempFile 2>&1')
    pythonVersion = open('tempFile', 'r').readline().split("Python ")[1].strip('\n')
    #pythonVersion = open('tempFile', 'r').readline().split("python ")[1].split(")")[0]
    if '3' in pythonVersion:
        version = ""
    elif '2' in pythonVersion:
        version = '3'
    os.system(includes.command(setup.commands, 'remove') + " tempFile")
    try:
        os.system("pip%s --version" % version)
    except:
        print("[-] pip is not installed")
        print("[*] Trying to install pip.....")

        if os.name == 'nt':
            try:
                os.system("python%s -m ensurpip --default-pip" % version)
                print("[+] pip has been succeffuly installed")
                # Restart the Script
                os.execv(sys.executable, [sys.executable] + sys.argv)
            except:
                print("[-] Some issues occored while installing pip")
                print("[-] Unable to install pip")
                sys.exit(0)
        elif os.name == 'posix':
            cmd = ""
            if os.path.isfile('/etc/os-release'):
                cmd = 'sudo apt-get install python%s-pip' % version
            else:
                cmd = 'brew install pip%s' % version
            try:
                os.system(cmd)
                print('[+] pip has been succeffuly installed')
                # Restart the Script
                os.execv(sys.executable, [sys.executable] + sys.argv)
            except:
                print('[-] Some issues occored while installing pip')
                print('[-] Unable to install pip')
                sys.exit(0)


def check(args):
    '''
    Check the libraries, if they are not istalled, it asks if to install the packeges automatically
    :return: void
    '''
    exceptions = []
    try:
        import urllib.request
    except ImportError:

        exceptions.append('urllib3')
    try:
        import requests
    except ImportError:
        exceptions.append('requests')
    try:
        import bs4
    except ImportError:
        exceptions.append('bs4')
    try:
        import netaddr
    except:
        exceptions.append('netaddr')
    try:
        import nmap
    except:
        exceptions.append('python-nmap')
    try:
        import ctypes
    except:
        exceptions.append('ctypes')
    try:
        import netaddr
    except:
        exceptions.append('netaddr')
    try:
        import json
    except:
        exceptions.append('json')

    versionList = []
    version = sys.version.split(" ")[0][:3]
    if len(exceptions) > 0:
        print("[-] The following libraries are missing")
        time.sleep(1)
        for item in exceptions:
            print('\t%s' % item)
        print("\n")
        if os.name == 'nt':
            os.system('pip --version > tempFile')
        else:
            os.system('echo $(pip --version) >> tempFile')
        pipVersion = args[0][-3:]
        if version == pipVersion:
            print("[+] Your pip default version corresponds with the python default version")
            version = ""
        else:
            print("[-] Your pip default version does not correspond with your python default version")
            print('''To install the packages needed you need to specify the python version you are using:
                    your pip default version:           %s
                    python version you are using:   %s
you have to specify the phyton version on the pip command to install the packages
            Example:
                        pip%s install 'package name' \n''' % (str(pipVersion), str(version), str(version)))
        show = '''To install the packages manually:\n
                        \t pip%s install 'package name'\n
    If you want the program to install the packages automatically, the following commands will be performed''' % ( str(version.split(".")[0]))
        print(show)
        for item in exceptions:
            print('\tpip%s install %s' % (str(version), item))

        a = str(input('Do you want to install the packages atomatically???? y/n '))
        if str(a) == 'y':
            for item in exceptions:
                try:
                    cmd = 'pip%s install %s' % (str(version), item)
                    os.system(cmd)

                except:
                    print("An error occored while installing the package")
                    print("check the your 'pip' settings or your python version")
                    sys.exit(0)
                try:
                    import_module( item)
                    print("[+] %s Succeffuly installed" % item)
                except:
                    print("An error occored while installing the package")
                    print("check the your 'pip' settings or your python version")
                    sys.exit(0)

            os.execv(sys.executable, [sys.executable] + sys.argv)
        elif a == 'n':
            os.execv(sys.executable, [sys.executable] + sys.argv)
            sys.exit(0)
        else:
            print('anwer not valid')
            print('You need to answer yes (y) or no (n)')
            exit(0)

    print('[+] All the necessary packeges are present')
    time.sleep(2)
