import os
import socket
from datetime import datetime



import Setup.setup as setup


def command(commands, cmd):
    """ Generalise the Unix <-> Windows commands """
    return commands[cmd][os.name]


def construct_url(url: str) -> (str, str):
    """
    build the url depending on what the user inputs

    :param      url:        user input:         str
    :return:    url:        builded url:        str
                siteDomain: domain of the site: str
    """
    if 'www' in url:
        site_domain = url.split(".")[1]
        if 'facebook' in site_domain:
            url = "https://%s/login.php?" % url
        else:
            url = "https://%s" % url
    else:
        site_domain = url
        if url == 'facebook':
            url = "https://%s.com/login.php?" % url
        else:
            url = "https://%s.com" % url
    return url, site_domain


def ifexists(file_name: str) -> str:
    """
    Checks the existence of a file
        if False creates it and saves it't location in 'fileName'
        if True, asks if to overwrirte the file
            if False recalls the function with a new input

    :param:     fineName:       str
    :return:    outputFileName: str
    """

    slash = command(setup.commands, 'slash')
    directory = ''
    if slash in file_name:
        directory = slash.join(file_name.split(slash)[:1])
    if not os.path.exists(file_name):
        print('[*] Creating the file %s' % file_name)
        os.system("%s %s" % (command(setup.commands, 'create'), file_name))
        print('[+] %s created' % file_name)
        return file_name
    else:
        print("%s already exists" % file_name)
        x = str(input("\tDo you want to overwrite it? y/n "))
        if x == 'y' or x == 'Y' or x == 'yes':
            print('[*] Overwriting the file %s ....' % file_name)
            os.system("%s %s" % (command(setup.commands, 'create'), file_name))
            print('[+] %s overwritten' % file_name)
            return file_name
        elif x == 'n' or x == 'N' or x == 'no':
            output = str(input('output file: '))
            if not directory:
                return ifexists(output)
            else:
                return ifexists('%s%s%s' % (directory, slash, output))
        else:
            print('[-] Invalid input')
            return ifexists(file_name)


def check_proxychains(proxychains: int) -> int:
    """
    Cheks the existence of the proxychains.conf file
    and sets the proxychans and tor options defines in the "Setup.setup.py" file
    :param   proxychains: int
    :return: proxychains: int
    """
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
                ret = os.system(cmd)
                if ret == 0:
                    print("[+] tor activated")
                else:
                    print("[-] Unable to activate tor")
        else:
            print("[-] /etc/proxychains.conf does not exist. Unable to activate proxychains")
            proxychains = 0
    return proxychains


def get_ip():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_name, host_ip
    except Exception:
        print("Unable to get Hostname and IP")
        return


def get_version() -> str:
    os.system('python --version "$1" > tempFile 2>&1')
    python_version = open('tempFile', 'r').readline().split("Python ")[1].strip('\n')
    if '3' in python_version:
        version = ""
    elif '2' in python_version:
        version = '3'
    else:
        raise Exception("Version Not Found")
    return version


def exception_handler(error: str, file: str) -> None:
    now = datetime.now()
    with open("Logs/" + file + ".txt", 'a') as f:
        f.write("*" * 90 + "\n")
        f.write(str(now.strftime("%d/%m/%Y %H:%M:%S")) + "\n")
        f.write(error + "\n\n")
