#Part 1
from gettext import install

import requests
import json
import string

sonnets = requests.get('https://poetrydb.org/author,title/Shakespeare;Sonnet')
print(sonnets.text)
print(type(sonnets.text))


sonnets_dict = json.loads(sonnets.text)
print(sonnets_dict[0])
print(type(sonnets_dict))

#Part 2

import re

class Sonnet:
    def __init__(self, sonnet):
        full_title = sonnet.get("title", " ")
        self.lines = sonnet.get("lines", [])
        self.linecount = sonnet.get("linecount", " ")

        match = re.match(r"Sonnet (\d+):\s*(.*)", full_title)
        if match:
            self.id = int(match.group(1))
            self.title = match.group(2)
    def __str__(self):
        lines_print = "\n".join(self.lines)
        return (f"Sonnet {self.id}: {self.title}"
                f"{lines_print}\n")
    def __repr__(self):
        return f"Sonnet(id={self.id}, title='{self.title}', lines={self.lines})"


sonnet_dict1 = sonnets_dict[0]
sonnet1 = (Sonnet(sonnet_dict1))

print(sonnet1)
print(repr(sonnet1))

#Part 3