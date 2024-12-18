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
    def tokenize(self, stemmer) -> list[str]:
        tokens = []
        for line in self.lines:
            processed_line = str(line).strip().lower().split(" ")
            for token in processed_line:
                processed_token = token.translate(str.maketrans("", "", string.punctuation))
                if processed_token and processed_token not in tokens:
                    stemmed_token = stemmer.stem(processed_token, 0, len(processed_token) - 1)  # Use the stemmer on a token
                    tokens.append(stemmed_token)
        return tokens


# Creating an instance of the class Sonnet
stemmer = PorterStemmer()
sonnet_dict1 = sonnets_dict[0]
sonnet1 = (Sonnet(sonnet_dict1))

print(sonnet1)
print(repr(sonnet1))
print(sonnet1.tokenize(stemmer))


"""
output without stemmer
['look', 'in', 'thy', 'glass', 'and', 'tell', 'the', 'face', 'thou', 'viewest', 'now', 'is', 'time', 'that', 'should', 'form', 'another', 'whose', 'fresh', 'repair', 'if', 'not', 'renewest', 'dost', 'beguile', 'world', 'unbless', 'some', 'mother', 'for', 'where', 'she', 'so', 'fair', 'uneard', 'womb', 'disdains', 'tillage', 'of', 'husbandry', 'or', 'who', 'he', 'fond', 'will', 'be', 'tomb', 'his', 'selflove', 'to', 'stop', 'posterity', 'art', 'mothers', 'thee', 'calls', 'back', 'lovely', 'april', 'her', 'prime', 'through', 'windows', 'thine', 'age', 'shalt', 'see', 'despite', 'wrinkles', 'this', 'golden', 'but', 'live', 'rememberd', 'die', 'single', 'image', 'dies', 'with']
"""

"""
output with stemmer  
['look', 'in', 'thy', 'glass', 'and', 'tell', 'the', 'face', 'thou', 'viewest', 'now', 'is', 'time', 'that', 'should', 'form', !'anoth', 'whose', 'fresh', 'repair', 'if', 'not', 'renewest', 'dost', !'beguil', 'world', 'unbless', 'some', 'mother', 'for', 'where', 'she', 'so', 'fair', 'uneard', 'womb', !'disdain', !'tillag', 'of', !'husbandri', 'or', 'who', 'he', 'fond', 'will', 'be', 'tomb', !'hi', !'selflov', 'to', 'stop', !'poster', 'art', !'mother', 'thee', !'call', 'back', 'love', 'april', 'her', 'prime', 'through', !'window', 'thine', !'ag', 'shalt', 'see', !'despit', !'wrinkl', !'thi', 'golden', 'but', 'live', 'rememberd', 'die', !'singl', !'imag', 'di', 'with']
"""

# We found it interseting that the stemmer did only little changes on the words and is not suitable for stemming such old texts, which had own grammar, e.g. the ending -est for second-person singular simple present indicative of view)
# also "thy" is not changes although there is a method in the stemmer class for converting "y" to "i"