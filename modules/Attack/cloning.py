import Includes.includes as include
from Setup.setup import commands
import requests
import urllib.request
import time
import os

class Cloning:

    def run():
        clone()

def clone():
    '''
    Clone the page qsked by the user
    :return: filename of the stored html cloned file: str
    '''
    slash = include.command(commands, 'slash')
    dir = "data%sCloned" % slash

    url = str(input("URL to clone: "))

    site, name = include.construct_url(url)

    if os.path.isdir(dir) == False:
        os.system("mkdir data%sCloned" % slash)
    # Check if the the page has been already cloned
    if os.path.isfile("%s%s%s.html" % (dir,slash,name)):
        print('[+] %s page already cloned' % name)
        print('[+] The html %s file is stored in %s' % (name,dir))
        time.sleep(10)
        return dir+slash+name+".html"

    page = requests.get(site)
    fileName = '%s%sTemp.html' % (dir, slash)
    os.system('%s %s' % (include.command(commands, 'create'), fileName))

    f = open(fileName, 'wb')
    f.write(page.text.encode('utf-8'))
    f.close()

    include.HTMLParser(fileName,"%s%s%s.html" % (dir,slash, name))

    os.system("%s %s" % (include.command(commands,'remove'), fileName))

    print('[*] Cloning site %s ....' % site)
    time.sleep(1)
    print('[+] Site %s cloned' % site)
    print('[+] Cloning completed, the html file is stored in %s%s%s.html' % (dir, slash, name))
    time.sleep(5)

    return dir+slash+name+".html"
