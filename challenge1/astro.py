#! usr/bin/env python3

import requests

url = 'http://api.open-notify.org/astros.json'

data = requests.get(url).json()

print (f'Number in space: {data["number"]}')

for x in data['people']:
    print(f'{x["name"]} is on {x["craft"]}')
