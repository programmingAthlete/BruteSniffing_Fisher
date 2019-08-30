import argparse
import json
import requests
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', type=str, required=True)
parser.add_argument('-P', '--payloads', type=str)
parser.add_argument('-C', '--cookie', type=str)
parser.add_argument('-H', '--headers', type=str)
parser.add_argument('-d', '--data')
args = parser.parse_args()

#payloads = json.loads(args.payloads)
#cookie = json.loads(args.cookie)
#headers = json.loads(args.headers)
data = json.loads(args.data)
payloads = data['payload']
cookie = data['cookie']
headers = data['headers']
r = requests.post(args.url, data=payloads, cookies=cookie, headers=headers)

#r = requests.post(args.url, data=payloads, cookies=cookie, headers=headers)
if 'Find Friends' in r.text:
    open('temp','w').write(str(r.content))
    print('\npassword is : ',passw)
    sys.exit(0)
else:
    sys.exit(1)
