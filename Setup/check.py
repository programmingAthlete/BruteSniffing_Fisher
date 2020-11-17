import Setup.setup as setup
import subprocess
from importlib import import_module
import Includes.version as getVersion
import os
import subprocess
import sys
import time

def read_libs():
    #f = open('requirements.txt', 'r')
    modules = []

    f = open('Setup/requirements.txt', 'r')
    for line in f:
        if line != "":
            module = line.split(' ----> ')[0].strip(" ")
            packege = line.split(' ----> ')[1].strip("\n").strip(" ")
            modules.append((module, packege))
    return modules

def check(args):
    '''
    Check the libraries, if they are not istalled, it asks if to install the packeges automatically
    :return: void
    '''
    mod= read_libs()
    #print(mod)
    exceptions = []
    for item in mod:
        try:
            import_module(item[0])
        except:
            exceptions.append(item[1])


    #try:
    #    import urllib.request
    #except ImportError:
#
#        exceptions.append('urllib3')
#    try:
#        import requests
#    except ImportError:
#        exceptions.append('requests')
#    try:
#        import bs4
#    except ImportError:
#        exceptions.append('bs4')
#    try:
#        import netaddr
#    except:
#        exceptions.append('netaddr')
#    try:
#        import nmap
#    except:
#        exceptions.append('python-nmap')
#    try:
#        import ctypes
#    except:
#        exceptions.append('ctypes')
#    try:
#        import netaddr
#    except:
#        exceptions.append('netaddr')
#    try:
#        import json
#    except:
#        exceptions.append('json')

    versionList = []
    command_version, version = getVersion.get_version()
    if len(exceptions) > 0:
        print("[-] The following libraries are missing")
        time.sleep(1)
        for item in exceptions:
            print('\t%s' % item)
        print("\n")
        if command_version != '':
            print('''The python version you are using is different than your default version
            \tdefault verion: %s
            \tyour version: %s
            ''' % (command_version, version))
            print('You need to specify the python versions correpsonding command to install the packeges')

        print('''To install the packeges needed:
                        python%s -m pip install 'package name' \n ''' % ( command_version))
        show = '''To install the packages manually:\n
                        \t python%s pip install 'package name\n If you want the program to install the packages automatically, the following commands will be performed''' % (command_version)
        print(show)
        for item in exceptions:
            print('\tpoython%s -m pip install %s' % (str(command_version), item))

        a = str(input('Do you want to install the packages atomatically???? y/n '))
        if str(a) == 'y':
            for item in exceptions:
                try:
                    cmd = 'python%s -m pip install %s' % (str(command_version), item)
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
