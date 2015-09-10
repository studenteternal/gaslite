#!/usr/bin/python

import requests
import yaml
import json
import pprint

credsFile = open("creds.yaml",'r')
creds = yaml.load(credsFile)

#print creds['username']
#print creds['api_key']

#client = SoftLayer.Client(username=(creds['username']), api_key=(creds['api_key']))

user = creds['username']
passwrd = creds['password']

print user
print passwrd


print 'import successful'


firewall_url = "https://169.57.11.151/rest/conf"


# this works and returns a location value in the header along with the response code.  the output needs a get to the returned location
r = requests.post (firewall_url, auth=(user, passwrd), verify=False )

print r.headers

session = r.headers['location']

#debug line to make sure I capture the information I expect to
#print loc


# print r.json()

# combine the location information from the first call with the host information for a valid URL 
show_string = "https://169.57.11.151/" + session + "/show/vpn/ipsec/site-to-site/peer/192.168.100.1/tunnel" 

print show_string


t = requests.post (show_string, auth=(user, passwrd), verify=False)
print(t.text)

 
#close the configuration session

requests.delete ("https://169.57.11.151/" + session, auth=(user, passwrd), verify=False)

#make sure the sessions are cleaned up

v = requests.get ("https://169.57.11.151/rest/conf", auth=(user, passwrd), verify=False)
print v.text

