import requests
import json
import string


# Part 1. Get Shakespeare’s sonnets

sonnets = requests.get('https://poetrydb.org/author,title/Shakespeare;Sonnet')
#print(sonnets.text)

dict_sonnets = json.loads(sonnets.text)
print(json.dumps(dict_sonnets, indent=4))

# Part 2. Convert the list of dictionaries to a list of Sonnet instances

class Sonnet:
    def __init__(self, sonnet):
        title = sonnet["title"]
        if "Sonnet" in title and ":" in title:
            parts = title.split(":") 
            self.id = int(parts[0].replace("Sonnet", "").strip()) 
            self.title = parts[1].strip()  
        else:
            raise ValueError("Invalid title format")

        self.lines = sonnet["lines"]

    def __str__(self):
        return f"Sonnet {self.id}: {self.title}\n" + "\n".join(self.lines)

    def __repr__(self):
        return f"Sonnet({self.id}, {repr(self.title)})"

    # Part 3. Add tokenization to your Sonnet class
    def tokenize(self) -> list[str]:
        tokens = []
        punctuation = string.punctuation
        # Process each line of the sonnet
        for line in self.lines:
            # Remove punctuation from the line and convert to lowercase
            line = line.translate(str.maketrans("", "", punctuation))  # Remove punctuation
            words = line.lower().split()  # Convert to lowercase and split into words
            tokens.extend(words)  # Add the words to the tokens list

        return tokens



sonnet_instances = [Sonnet(sonnet_dict) for sonnet_dict in dict_sonnets]
print(sonnet_instances[0])
sonnet_instances = list(map(Sonnet, dict_sonnets))
print(sonnet_instances[5])








