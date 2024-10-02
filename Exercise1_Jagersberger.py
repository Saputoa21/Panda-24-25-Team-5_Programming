import json
with open('books.json', 'r') as file:
    books = json.load(file)

# Exercise 1
# Part 1: Compute statistics
def get_statistics(books: list) -> dict:
    author_stats = {}

    for book in books:
        author = book['author']
        pages = book['total_pages']
        chapters = book['chapter_count']
        title = book['title']
        publication_date = book['publication_date']

        if author not in author_stats:
            author_stats[author] = {
                'total_pages': 0,
                'total_chapters': 0,
                'books': [],
                'publication_dates': []
            }

        author_stats[author]['total_pages'] += pages
        author_stats[author]['total_chapters'] += chapters
        author_stats[author]['books'].append(title)
        author_stats[author]['publication_dates'].append(publication_date)

    for author, stats in author_stats.items():
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

statistics = get_statistics(books)
print(statistics)


# Part 2: Get a list of genres

def get_genres (books: list) -> list:
    list_of_genres = set()
    for book in books:
        genre = book['genre']
        list_of_genres.add(genre)


    return list(list_of_genres)

genre_stats = get_genres(books)
print(genre_stats)