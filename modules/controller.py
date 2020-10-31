import Setup.setup as setup
import Includes.includes as includes
import os
import sys
import modules.Attack.core as core


def max_index(dictionary):
    '''
    returns the bigger index < 98 on the current menu
    :param dictionary:
    :return: maxIndex: int
    '''
    keys = list(dictionary.keys())
    L = []
    for key in keys:
        if key < 98:
            L.append(key)
    return max(L)

class Directory:

    def __init__(self, dict, flag):
        self.dict = dict
        self.flag = flag

    def show(self):
        for key in self.dict:
            print("%d) %s" % (key, self.dict[key]))

    def change_directory(self, newDict, newFlag):
        self._oldFlag = self.flag
        self.dict = newDict
        self.flag = newFlag

    def clear_screen(self):
        os.system(includes.command(setup.commands, 'clear'))



    def printt(self, cmd):
        print(includes.command(setup.commands,cmd))

class Router:

    def __init__(self, dire, directories, links, attack):
        self.dire = dire
        self.attack = attack
        self.dirS = directories
        self.links = links


    def start(self):
        while 1:

            self.dire.show()
            try:
                x = int(input(">> "))
            except KeyboardInterrupt:
                print("\nExiting...")
                sys.exit(0)
            except:
                print("\nInput mus be an integer")
                continue

            if x == 99:
                sys.exit(0)
            elif x == 98:
                self.dire.change_directory(self.dirS[self.dire._oldFlag], self.dire._oldFlag)
                self.dire.clear_screen()
                continue
            elif x > max_index(self.dire.dict):
                print('\n[-]',x,"is not a valid argument\n")
                continue
            if any(self.links[i][0] in list(self.dire.dict.values()) and x == self.links[i][1] for i in range(len(self.links))):
                self.dire.change_directory(self.dirS[x],x)
            else:
                self.attack.name = self.dire.dict[x]
                self.attack.run()
                #break

            self.dire.clear_screen()


class Attack:

    def __init__(self, dire):
        self.name = ""
        self.dire = dire

    def run(self):
        attack = core.Core(self.name)
        attack.run()
