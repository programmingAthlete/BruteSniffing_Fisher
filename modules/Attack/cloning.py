import os
import time

import requests

import utils.utils as include
from Setup.setup import commands


class Cloning:

    def __str__(self):
        return 'Cloning attack'

    @staticmethod
    def run():
        clone()


def clone():
    """
    Clone the page qsked by the user
    :return: filename of the stored html cloned file: str
    """
    slash = include.command(commands, 'slash')
    directory = "data%sCloned" % slash

    url = str(input("URL to clone: "))

    site, name = include.construct_url(url)

    if not os.path.isdir(directory):
        os.system("mkdir data%sCloned" % slash)
    # Check if the the page has been already cloned
    if os.path.isfile("%s%s%s.html" % (directory, slash, name)):
        print('[+] %s page already cloned' % name)
        print('[+] The html %s file is stored in %s' % (name, directory))
        time.sleep(10)
        return directory + slash + name + ".html"

    page = requests.get(site)
    file_name = '%s%sTemp.html' % (directory, slash)
    os.system('%s %s' % (include.command(commands, 'create'), file_name))

    f = open(file_name, 'wb')
    f.write(page.text.encode('utf-8'))
    f.close()

    include.html_parser(file_name, "%s%s%s.html" % (directory, slash, name))

    os.system("%s %s" % (include.command(commands, 'remove'), file_name))

    print('[*] Cloning site %s ....' % site)
    time.sleep(1)
    print('[+] Site %s cloned' % site)
    print('[+] Cloning completed, the html file is stored in %s%s%s.html' % (directory, slash, name))
    time.sleep(5)

    return directory + slash + name + ".html"
