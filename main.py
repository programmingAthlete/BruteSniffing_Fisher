from Setup import setup, check
import sys

## Check the reauirements
check.check(sys.argv)

import modules.controller as controller

print('''

Welcome to the BRUTESNIFFING FICHER, an hacking tool that anables you to do bruteforcing attacks - on web servers and on secured files, fishing attacks and scanning and sniffing attacks

''')

intro = controller.Directory(setup.intro, 0)
attack = controller.Attack(dire=intro)
session = controller.Router(dire=intro, directories=setup.directories, links=setup.links, attack=attack)
try:
    session.start()
except KeyboardInterrupt:
    print('\nExiting...')
    sys.exit(0)
