import json

with open('books.json', 'r') as file:
    books = json.load(file)
    print(books)

# ... your logic here ...
#def get_statistics(books: list) -> dict:
    for author in books:
        author_info = {}
        author_info["author"] = books["author"]
        author_info["total_pages"] += books["total_pages"]
        author_info["total_pages"] += books["total_pages"]

