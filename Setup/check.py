import os
import sys
import time
from importlib import import_module

import Setup.setup as setup
from utils.version import get_version


def read_libs():
    modules = []
    slash = setup.commands['slash'][os.name]
    f = open('Setup' + slash + '/requirements.txt', 'r')
    for line in f:
        if line != "\n" and "LIBRERY" not in line:
            module = line.split(' ----> ')[0].strip(" ")
            package = line.split(' ----> ')[1].strip("\n").strip(" ")
            modules.append((module, package))
    return modules


def read_requirements():
    with open('requirements.txt', 'r') as f:
        for line in f:
            yield line.strip("\n")


def check(fun):
    """
    Check the libraries, if they are not istalled, it asks if to install the packeges automatically
    :return: void
    """

    def wrapper():
        mod = list(read_requirements())
        exceptions = []
        for item in mod:
            try:
                if item and "#" != item[0]:
                    if item[:3] == "git":
                        import_module(item.split("/")[-1].split("@")[0])
                    else:
                        pkg = item.split("==")
                        if pkg[0] == "beautifulsoup4":
                            import_module("bs4")
                        elif pkg[0] == 'python-nmap':
                            import_module("nmap")
                        else:
                            import_module(pkg[0])
            except ImportError:
                exceptions.append(item)

        if len(exceptions) > 0:
            print("[-] The following libraries are missing")
            time.sleep(1)
            for item in exceptions:
                print('\t%s' % item)
            print("\n")

            print('''To install the packeges needed:
                            python -m pip install <package name> \n ''')
            show = '''To install the packages manually:\n
                        \t python pip install <package name>\n If you want the program to install the packages
                         automatically, the following commands will be performed'''
            print(show)
            for item in exceptions:
                command = f"python -m pip install '{item}'"
                print(f'\t{command}')

            a = str(input('Do you want to install the packages atomatically???? y/n '))
            if str(a) == 'y':
                os.system(f"python -m pip install -r requirements.txt")
            elif a == 'n':
                os.execv(sys.executable, [sys.executable] + sys.argv)
                sys.exit(0)
            else:
                print('answer not valid')
                print('You need to answer yes (y) or no (n)')
                exit(0)

        print('[+] All the necessary packages are present')
        time.sleep(2)
        return fun()

    return wrapper
