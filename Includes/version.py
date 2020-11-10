import subprocess
import sys

def get_version():
    version = sys.version.split(" ")[0][:3]
    command_version = ''
    cmd = "python -V"
    p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
    defaultVersion = p.stderr.read(10).decode('utf-8')
    if defaultVersion[:-3] == version:
        command_version = ''
    else:
        if float(version) < 3.:
            print('[-] Python version not compatible')
            sys.exit()
        elif 3.6 <= float(version) <= 3.7:
            command_version = version
        else:
            command_version = '3'
    return command_version, version
