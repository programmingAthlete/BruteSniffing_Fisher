import sys
import traceback

from Setup.check import check, setup
from utils.utils import exception_handler


@check
def main():
    import modules.controller as controller

    print('''
    Welcome to the BRUTESNIFFING FICHER, an hacking tool that anables you to do bruteforcing attacks - 
    on web servers and on secured files, fishing attacks and scanning and sniffing attacks
    ''')

    intro = controller.Directory(setup.intro, 0)
    attack = controller.Attack(dire=intro)
    session = controller.Router(dire=intro, directories=setup.directories, links=setup.links, attack=attack)
    try:
        session.start()
    except KeyboardInterrupt:
        print('\nExiting...')
        sys.exit(0)
    except Exception as e:
        print("\n[-] Exception occored\n")
        print(e)
        exception_handler(traceback.format_exc(), "main")


if __name__ == "__main__":
    main()
