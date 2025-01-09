import requests
import json
import string
from porter_stemmer import PorterStemmer

stemmer = PorterStemmer()

sonnets = requests.get('https://poetrydb.org/author,title/Shakespeare;Sonnet')
#print(sonnets.text)

dict_sonnets = json.loads(sonnets.text)
print(json.dumps(dict_sonnets, indent=4))

#sorted_sonnets = sorted(dict_sonnets, key=lambda x: int(re.search(pattern r'\d+', x['title']).group()))

class Document:
    def __init__(self, lines: List[str]):
        self.lines = lines
        self.stemmer = PorterStemmer()

    def tokenize(self) -> List[str]:
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
    def __init__(self, sonnet: dict):
        super().__init__(sonnet['lines'])
        title = sonnet["title"]
        if "Sonnet" in title and ":" in title:
            parts = title.split(": ") # Splitting by the column and the white space
            self.id = int(parts[0].replace("Sonnet", "").strip())
            #self.id = int(sonnet['title'].split(': ')[0].split()[-1])
            self.title = parts[1].strip()
        else:
            raise ValueError("Invalid title format")

        self.lines = sonnet["lines"]


    #no need to store the line count data
    # def line_count(self):
    #     line_count = len(self.lines)

    def __str__(self):
        return f"Sonnet {self.id}: {self.title}\n" + "\n".join(self.lines)

    def __repr__(self):
        return f"Sonnet({self.id}, {repr(self.title)})"

    # Part 3. Add tokenization to your Sonnet class
    # def tokenize(self, stemmer) -> list[str]:
    #     tokens = []
    #     punctuation = string.punctuation #Py module
    #     # Process each line of the sonnet
    #     for line in self.lines:
    #         # Remove punctuation from the line and convert to lowercase
    #         line = line.translate(str.maketrans("", "", punctuation))  # Remove punctuation
    #         words = line.lower().split()  # Convert to lowercase and split into words
    #         stemmed_words = [stemmer.stem(word, 0, len(word) -1) for word in words]
    #         tokens.extend(stemmed_words)  # Add the words to the tokens list
    #
    #     return tokens


class Query(Document):
    def __init__(self, query: str):
        super().__init__([query])


class Index(dict[str, set[int]]):
    def __init__(self, documents: List[Sonnet]):
        super().__init__()
        self.documents = documents

        for document in documents:
            self.add(document)

    def add(self, document: Sonnet) -> None:
        tokens = document.tokenize()

        for token in tokens:
            if token not in self:
                self[token] = set()

            self[token].add(document.id)

    def search(self, query: Query) -> List[Sonnet]:
        query_tokens = query.tokenize()
        if not query_tokens:
            return []

        posting_lists = []
        for token in query_tokens:
            if token in self:
                posting_lists.append(self[token])
            else:
                return []

        matching_ids = set.intersection(*posting_lists)
        matching_sonnets = [
            doc for doc in self.documents
            if doc.id in matching_ids
        ]
        matching_sonnets.sort(key=lambda x: x.id)

        return matching_sonnets







# sonnet_instances = [Sonnet(sonnet_dict) for sonnet_dict in dict_sonnets]
# print(sonnet_instances[0])
# sonnet_instances = list(map(Sonnet, dict_sonnets))
# print(sonnet_instances[5])

