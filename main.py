from Setup import setup, check
import sys

## Check the reauirements
check.pip_installation()
check.check()

import modules.controller as controller

print('''

Welcome to the BRUTESNIFFING FICHER, and hacking tools that anables you to do bruteforcing attacks - on web servers and on secured files, fishing attacks and scanning and sniffing attcks all in one tool

''')

intro = controller.Directory(setup.directories[0], 0)
attack = controller.Attack(dire=intro)
session = controller.Router(dire=intro, directories=setup.directories, links=setup.links, attack=attack)
try:
    session.start()
except KeyboardInterrupt:
    print('\nExiting...')
    sys.exit(0)
