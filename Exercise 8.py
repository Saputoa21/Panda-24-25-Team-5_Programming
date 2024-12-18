from gettext import install
import requests
import json
import string
from porter_stemmer import PorterStemmer

sonnets = requests.get('https://poetrydb.org/author,title/Shakespeare;Sonnet')
print(sonnets.text)
print(type(sonnets.text))

sonnets_dict = json.loads(sonnets.text)
print(sonnets_dict[0])
print(type(sonnets_dict))

class Sonnet:
    def __init__(self, sonnet):
        full_title = sonnet.get("title", " ")
        self.lines = sonnet.get("lines", [])
        self.linecount = sonnet.get("linecount", " ")

        parts = full_title.split(":")
        sonnet_number_part = parts[0]  # "Sonnet 1"
        self.title = parts[1].strip()  # "From fairest creatures we desire increase" - we use strip because there can be a whitespace between two parts, e.g. Sonnet 1_'From ...'.
        self.id = int(sonnet_number_part.split(" ")[1]) # we devide the "Sonnet 1" by space between the words and get "Sonnet" at index [0] and the number at index [1]
    def __str__(self):
        lines_print = "\n".join(self.lines)
        return (f"Sonnet {self.id}: {self.title}\n"
                f"{lines_print}\n")
    def __repr__(self):
        return f"Sonnet(id={self.id}, title='{self.title}', lines={self.lines})"

#Tokenise meethod as a couple of for-loops
    # def tokenize(self) -> list[str]:
    #     tokens = []
    #     for line in self.lines:
    #         processed_line = str(line).strip().lower().split(" ")
    #         for token in processed_line:
    #             # if token not in string.punctuation:
    #             for char in token:
    #                 if char in string.punctuation:
    #                     char.replace(char, "")
    #                     if token not in tokens:
    #                         tokens.append(token)
    #                 else:
    #                     if token not in tokens:
    #                         tokens.append(token)
    #     return tokens
    def tokenize(self) -> list[str]:
        tokens = []
        for line in self.lines:
            processed_line = str(line).strip().lower().split(" ")
            for token in processed_line:
                processed_token = token.translate(str.maketrans("", "", string.punctuation))
                if processed_token and processed_token not in tokens:
                    tokens.append(processed_token)
        return tokens


# Creating an instance of the class Sonnet
sonnet_dict1 = sonnets_dict[0]
sonnet1 = (Sonnet(sonnet_dict1))

print(sonnet1)
print(repr(sonnet1))
print(sonnet1.tokenize())