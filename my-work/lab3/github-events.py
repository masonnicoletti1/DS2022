#!/usr/local/bin/python3

import os
import json
import requests

# Access url for api content on personal GitHub account
GHUSER = os.getenv('GITHUB_USER')
url = 'https://api.github.com/users/{0}/events'.format(GHUSER)

# Format url contents
r = json.loads(requests.get(url).text)

# Iterate through apis
for x in r[:5]:
  event = x['type'] + ' :: ' + x['repo']['name']
  print(event)



print(r)

