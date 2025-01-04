import requests
import json
import os
import string
from porter_stemmer import PorterStemmer

stemmer = PorterStemmer()

file_name = "Shakespeare_sonnets.json"
sonnets = []

if not os.path.exists(file_name):
    response = requests.get('https://poetrydb.org/author,title/Shakespeare;Sonnet')
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(response.text)
    print(f"Sonnets stored in file: {file_name}")

    if response.status_code == 200:
        sonnets = json.loads(response.text)
else:
    with open(file_name, "r", encoding="utf-8") as file:
        sonnets = json.load(file)

class Document:
    def __init__(self, lines):
        self.lines = lines
    def tokenize(self, stemmer) -> list[str]:
        tokens = []
        for line in self.lines:
            processed_line = str(line).strip().lower().split(" ")
            for token in processed_line:
                processed_token = token.translate(str.maketrans("", "", string.punctuation))
                if processed_token and processed_token not in tokens:
                    stemmed_token = stemmer.stem(processed_token, 0, len(processed_token) - 1)
                    tokens.append(stemmed_token)
        return tokens

class Sonnet(Document):
    def __init__(self, sonnet):
        full_title = sonnet["title"]
        lines = sonnet["lines"]
        super().__init__(lines)
        parts = full_title.split(": ", 1)
        self.title = parts[1]  # "From fairest creatures we desire increase" - we use strip because there can be a whitespace between two parts, e.g. Sonnet 1_'From ...'.
        self.id = int(parts[0].split(" ")[1]) # we devide the "Sonnet 1" by space between the words and get "Sonnet" at index [0] and the number at index [1]
    def __str__(self):
        lines_print = "\n".join(self.lines)
        return (f"Sonnet {self.id}: {self.title}\n"
                f"{lines_print}\n")
    def __repr__(self):
        lines_print = "\n".join(self.lines)
        return (f"Sonnet {self.id}: {self.title}\n"
                f"{lines_print}\n")
class Query(Document):
    def __init__(self, query: str):
        super().__init__([query])

class Index(dict[str, set[int]]):
    def __init__(self, documents: list[Sonnet]):
        super().__init__()
        self.documents = documents
        self.inverted_index = {}
        for document in documents:
            self.add(document)
    def add(self, document: Sonnet):
        id = document.id
        for token in document.tokenize(stemmer):
            if token not in self.inverted_index:
                self.inverted_index[token] = set()
            else:
                self.inverted_index[token].add(id)
    def get_inverted_index(self):
        return self.inverted_index
    def search(self, query: Query) -> list[Sonnet]:
        query_tokens = query.tokenize(stemmer)  # Tokenize the query
        matching_ids = []
        for token in query_tokens:
            if token in self.inverted_index:
                matching_ids = self.inverted_index[token]
            else:
                matching_ids = matching_ids.intersection(self.inverted_index[token])
            if not matching_ids:
                return []
        matching_sonnets = []
        for document in self.documents:
            if document.id in sorted(matching_ids):
                matching_sonnets.append(document)
        return matching_sonnets

# Creating an instance of the class Sonnet
sonnet1 = (Sonnet(sonnets[0]))

print(sonnet1.id)
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

# Creating list of instances of the class Sonnet
sonnet_list = [Sonnet(sonnet) for sonnet in sonnets]

# Getting inverted index
index = Index(sonnet_list)
inverted_index = index.get_inverted_index()
print(inverted_index)

# Creating an instance of Query class:
query = Query("love hate")
print(query)
print(query.tokenize(stemmer))

# Searching for "love" and "hate" in the list Sonnet instances
matching_sonnets = index.search(query)  # Search the index with the query

# Print the results
for matching_sonnet in matching_sonnets:
    print(matching_sonnet)