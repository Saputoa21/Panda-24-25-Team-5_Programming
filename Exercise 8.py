import json

import requests

sonnets = requests.get('https://poetrydb.org/author,title/Shakespeare;Sonnet')

print(sonnets.text)

sonnets_dict = json.loads('sonnets')

