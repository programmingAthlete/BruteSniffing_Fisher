import requests
import Setup.setup as setup
import utils.utils as includes
from bs4 import BeautifulSoup
from zipfile import ZipFile
import json
import os
import sys

class Zip_fileBruteforce:

	def run():
		zip_bruteForce()


def passFile_input_descriptio():
	'''
	Prints information about the password file
	:return: void
	'''
	print('Input a password file (leave blanck if you want to use the default file: %s%spasswords.txt' % (dir, slash))
	print('\tThe password file will be searched in the %s directory' % dir)
	print('\tIf you want to select it from the current directory or specify a specific path to the file, add the "-d" argument')
	print('\t\tExample:\n\t\t <pasword file> -d')

def zip_bruteForce():
	'''
    Zip password Bruteforcer
    :return: void
    '''
	try:
		zipArchive = ZipFile(input('Protected archive:'))
		passFile_input_descriptio()
		passFile = input("Password file:")
		found = ""
	except:
		print('error')
		sys.exit(0)

	if passFile == '':
		passFile = dir+slash+'passwords.txt'
	elif passFile != "" and "-d" not in passFile:
		passFile = dir+slash+passFile

	with open(passFile, "r") as f:
		for line in f:
			password = line.strip("\n")
			password = password.encode("utf-8")

			try:
				found = zipArchive.extractall(pwd=password)
				if found == None:
					print("[+] Password found ", password.decode())
			except RuntimeError:
				pass
		if found == "":
			print("[-] Password not found")
