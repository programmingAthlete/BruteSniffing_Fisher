import importlib
import inspect
import sys

class Core:

    def __init__(self,name):

        if " " in name:
            name = name.replace(" ", "")
        if "-" in name:
            name = name.replace("-", "_")
        self.module = name[0].lower() + name[1:]
        self.class_ = self.module[0].upper() + self.module[1:]

    def print_classes(self):
        for name, obj in inspect.getmembers(self.module):
            if inspect.isclass(obj):
                print(obj)

    def run(self):
        try:
            module = importlib.import_module('modules.Attack.'+self.module)
        except ModuleNotFoundError:
            try:
                module = importlib.import_module('modules.Attack.BruteForce.'+self.module)
            except ModuleNotFoundError:
                print('[-] Module %s not found' % self.module)

        class_ = getattr(module, self.class_)
        class_.run()
