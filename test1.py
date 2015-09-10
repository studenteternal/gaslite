#!/usr/bin/python

import requests
import yaml
import json

print 'import successful'


firewall_url = "https://169.57.11.151/rest/op/show/version"


# this works and returns a location value in the header along with the response code.  the output needs a get to the returned location
r = requests.post (firewall_url, auth=('jeff', 'scuba123'), verify=False )

loc = r.headers['location']

#debug line to make sure I capture the information I expect to
print loc


# print r.json()

# combine the location information from the first call with the host information for a valid URL 
version_loc = "https://169.57.11.151/" + loc
print version_loc


r = requests.get (version_loc, auth=('jeff', 'scuba123'), verify=False)

print r.text

