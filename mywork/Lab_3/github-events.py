#!/opt/homebrew/bin/python3
import os
import json
import requests
GHUSER = os.getenv('GITHUB_USER')
url = "https://api.github.com/users/{0}/events".format(GHUSER)
print(GHUSER)

response = requests.get(url)
if response.status_code == 200:
    r = json.loads(response.text)  
    print("Recent GitHub Activity:\n")
    
    for x in r[:5]:
        event = x['type'] + ' :: ' + x['repo']['name']
        print(event)

else:
    print(f"Error: Unable to fetch data (Status Code {response.status_code})")