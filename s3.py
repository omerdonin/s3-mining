#!/usr/bin/env python
import requests
import sys
from time import sleep

url = 'https://s3.amazonaws.com/'
name = sys.argv[1].strip()

common = ['test', 'dev', 'bucket', 's3', 'aws', 'prd', 'prod', 'pub', 'public', 'production', 'development', 'testing',
          'archive', 'backup', 'web', 'devops', 'sec', 'secure', 'hidden', 'secret', 'staging', 'download']
connectors = ['-', '_', '']

url = url + name

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def check_code(r, name):
    if r.status_code == 404:
        print "None",
    elif r.status_code == 403:
        print bcolors.WARNING+"Secure",
    elif r.status_code == 301:
        print bcolors.OKBLUE+"Redirect",
    elif r.status_code == 200:
        print bcolors.OKGREEN+"BINGO!",
    elif r.status_code == 400:
        print "BadName",
    else:
        print r.status_code,
    print name+bcolors.ENDC
    return

def get_code(url, name, counter):
    if counter < 3:
        try:
            r = requests.get(url)
        except requests.exceptions.ConnectionError:
            print "Connection refused, waiting for a green light"
            sleep(5)
            get_code(url, name, counter +1)
    else:
        print bcolors.WARNING+"I tried sweetheart, but google is block you. \n" \
                              "Change your IP or somthing and try again later"+bcolors.ENDC
        exit()
    check_code(r, name)
    for ext in common:
        for i in connectors:
            r = requests.get(url + i + ext)
            check_code(r, name + i + ext)


get_code(url, name, 0)
if '.' in name:
    n2 = 'www.' + name
    url = 'https://s3.amazonaws.com/' + n2
    get_code(url, n2)
    n2 = 's3.' + name
    url = 'https://s3.amazonaws.com/' + n2
    get_code(url, n2)
    n3 = name.split('.')[0]
    url = 'https://s3.amazonaws.com/' + n3
    get_code(url, n3)



