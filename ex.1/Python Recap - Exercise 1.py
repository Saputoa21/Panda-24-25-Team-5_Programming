import json
with open('books.json', 'r') as file:
    books = json.load(file)

# Exercise 1
# Part 1: Compute statistics
def get_statistics(books: list) -> dict:
    author_stats = {} # empty dictionary that holds author information

    for book in books: # loop through the books and extract information
        author = book['author']
        pages = book['total_pages']
        chapters = book['chapter_count']
        title = book['title']
        publication_date = book['publication_date']

        if author not in author_stats: # check if  author is already in the dictionary; if not initialize new entry
            author_stats[author] = {
                'total_pages': 0,
                'total_chapters': 0,
                'books': [],
                'publication_dates': []
            }

        a_stats = author_stats[author]
        a_stats['total_pages'] += pages # update the values for each author
        a_stats['total_chapters'] += chapters
        a_stats['books'].append(title)
        a_stats['publication_dates'].append(publication_date)

    for author, stats in author_stats.items(): # loop over each author to calculate statistics.
        stats['average_chapters'] = stats['total_chapters'] / len(stats['books'])
        stats['first_publication'] = min(stats['publication_dates'])
        stats['last_publication'] = max(stats['publication_dates'])

        author_stats[author] = {
            'total_pages': stats['total_pages'],
            'average_chapters': stats['average_chapters'],
            'books': stats['books'],
            'publication_period': (stats['first_publication'], stats['last_publication'])
        }

    return author_stats

# Assuming books.json is already loaded into a variable `books`
final_dict = get_statistics(books)

# Print the result
print(final_dict)

def print_statistics(final_dict: dict):
    for author, data in final_dict.items():
        print(f"Author: {author}")
        print(f"  Total Pages: {data['total_pages']}")
        print(f"  Titles: {', '.join(data['books'])}")
        print(f"  Average Chapters: {data['average_chapters']:.2f}")
        print(f"  Publication Period: {data['publication_period'][0]} to {data['publication_period'][1]}")
        print("\n" + "-"*50 + "\n")

# Call the function to print the final dictionary
print_statistics(final_dict)


# Part 2: Get a list of genres

def get_genres (books: list) -> list:
    list_of_genres = set()
    for book in books:
        genre = book['genre']
        list_of_genres.add(genre)


    return list(list_of_genres)

genre_stats = get_genres(books)
print(genre_stats)

