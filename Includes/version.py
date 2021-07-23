import subprocess
import sys


def get_version():
    version = sys.version.split(" ")[0]
    output = subprocess.run(["python", "-V"], capture_output=True).stdout.decode('utf-8').strip("\n")
    default_version = output.split(" ")[1]
    if default_version == version:
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
