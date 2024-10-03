import json

with open('books.json', 'r') as file:
    books = json.load(file)
    print(books)
#    for info in books:
#        print(info["author"])

# ... your logic here ...
''' Exercise 1 '''
def get_statistics(books: list) -> dict:
    selected_author = input("Please, choose an author: ")
    selected_books = {}
    total_number_of_pages = 0
    total_chapter_count = 0
    number_of_books = 0
    list_of_titles = []
    average_chapter_count = 0
    publication_period = []
    publication_years = []
    publication_dates = []

    # choosing an author

    for info in books:
        if selected_author in info["author"]:
            selected_books["your author"] = selected_author
        continue

    # total number of pages

    for info in books:
        if selected_author in info["author"]:
            total_number_of_pages += int(info["total_pages"])
            selected_books["total number of pages by your author"] = total_number_of_pages
        continue

    # average chapter count

    for info in books:
        if selected_author in info["author"]:
            number_of_books += 1
            total_chapter_count += int(info["chapter_count"])
            average_chapter_count = total_chapter_count // number_of_books
            selected_books["average chapter count by your author"] = average_chapter_count
        continue

    # list of titles

    for info in books:
        if selected_author in info["author"]:
            list_of_titles.append(info["title"])
            selected_books["list of titles"] = list_of_titles
        continue

    # publication period

    for info in books:
        if selected_author in info["author"]:
            publication_dates.append(str(info["publication_date"]))
            i = 0
            publication_years.append(publication_dates[i][:4])
            i +=1
        continue
    publication_period.append(min(publication_years))
    publication_period.append(max(publication_years))
    selected_books["period of publication"] = publication_period
    return selected_books

"""Exercise 2"""

def get_genres(books: list) -> list

if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

print(get_statistics(books))

print(get_genres(books))



