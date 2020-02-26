import Includes.menu as menu

####### commands generalisation unix <-> microsoft
commands = { 'create':
                {'posix' : 'touch', 'nt' : 'echo '' > '},
            'clear':
                {'posix' : 'clear', 'nt' : 'clr'},
            'copy':
                {'posix' : 'cp', 'nt' : 'copy'},
            'move':
                {'posix' : 'mv', 'nt' : 'rename'},
            'remove':
                {'posix' : 'rm', 'nt' : 'del'},
            'open':
                {'posix' : 'open', 'nt' : 'type'},
             'slash':
                {'posix' : '/', 'nt' : '\\'}
            }

####### prepare menus
directories, links = menu.construct_menus()
intro = directories[0]

########################################################################
## If you want to specify the python version for the run function of
## bruteforce attack, uncomment the corresponding version bruteforce
## attack
######################################################################## 
#pythonVersion = "3"
#pythonVersion = "3.1"
#pythonVersion = "3.5"
#pythonVersion = "3.6"
#pythonVersion = "3.7"

#######################################################
## proxychanis and tor only vailable for Linux users
## Set to "On" to activate 
########################################################
proxychains = "Off"
tor = "Off" # activate only if proxychains is on
