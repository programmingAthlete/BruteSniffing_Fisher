# BruteSniffing fisher

## Introduction
Welcome to the ButeSniffing_Ficher, a multiplatform python hacking tool in a menu style.</br>

Launch the program by the command line by</br>

    python main.py


depending on your python installation you may need to specify the python version.

For example for a 3.6 version:

     python3.6 main.py


It allows you do to:
* Sniffing
* Zip-file Bruteforce
* Website attacks
    * Information gathering
    * Web Server Bruteforcing
    * Cloning
    * Fishing

## Python version
The program has been developed using python3.6. However no issue should occur with older 3. versions.


## Requirements Installation
Automatically checks for the presence of the required libraries and installs them if you consent it. If you don't consent it, it shows you the command to perform the installation of the libraries.

Libraries to install:
* requests
* urllib3
* BeautifulSoup
* json
* ctypes
* netaddr
* python-nmap

## Structure
Hirerchy of the project:
* main.py
* Setup
    * setup.py - sets the python version, the menus to show, the unix-windows commands generalisation and Proxychains and Tor settings
    * check.py - checks on the required libraries
    * server.config - constant to set if using localhost (choose between MAMP , XAMPP aphache servers and apache2 server)
    * menus.txt - file from which the menus are read. Edit here to add/remove menus
    * menu.py - python file to extract the menus into dictionaries from the 'menu.txt' file
* Includes
    * includes.py - some functions used by the modules
* modules - objects for the controller (navigator between menus) and the attacks. Edit here to add/remove features. Each attack should be a class with a run method.
* data - Where the cloned pages and the found credentials are stored - the relative directories will be created. A password list is also found in the BruteForce subdirectory.
* Server - code to put in the index.php file on the server for the fishing

You can add more menus by updating the file Setup/menus.txt - RESPECT THE FORMAT!!

You can add the corresponding features by updating the modules/Attack directory and the Attack object in the 'controller.py' file.

## Proxychains and Tor
Proxychains and Tor are supported for Linux platforms. Edit the settings in the Setup/setup.py file

## Screenshots

<img src="Screenshot/introMenu.png">
<img src="Screenshot/webAttackMenu.png">

## Issues and Improvements
* Functionalities can be added adding 'menus' in the Setup/menus.txt file, modules in the modules directories and functions in the Includes/includes.py file.
* The server settings may be improved, the goal would be to make the fishing attack available using the default web server of a system
* In the fishing attack the python program waits for a tmp.txt file to be created by the php code, then deletes it. The process has to be slowed down for the python program to grab the tmp.txt file.

## References
Reference for the web page bruteforcing: https://github.com/IAmBlackHacker/Facebook-BruteForce
