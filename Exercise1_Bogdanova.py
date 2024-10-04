import json

with open('books.json', 'r') as file:
    books = json.load(file)

#Part1
# 1. Total number of pages across all the books by that author.
# 2. Average number of chapters per book by that author.
# 3. A list of titles of the books by that author.
# 4. The Publication period, which is the date of the first and last
# publication by that author.

def get_statistics(books: list) -> dict:
    final_dict = {}  # Empty dict to store stats for each author

    # Loop through each book
    for book in books:
        author = book["author"]

        # Initialize author in final_dict if not already present
        if author not in final_dict:
            final_dict[author] = {
                "total_pages": 0,
                "chapter_count": 0,
                "book_count": 0,
                "titles": [],
                "earliest_date": None,
                "latest_date": None
            }

        # Update total pages, chapter count, and book count for this author
        final_dict[author]["total_pages"] += book["total_pages"]
        final_dict[author]["chapter_count"] += book["chapter_count"]
        final_dict[author]["book_count"] += 1
        final_dict[author]["titles"].append(book["title"])

        pub_date = book["publication_date"]

        # Update earliest_date if it's None or the current pub_date is earlier
        if final_dict[author]["earliest_date"] is None or pub_date < final_dict[author]["earliest_date"]:
            final_dict[author]["earliest_date"] = pub_date

        # Update latest_date if it's None or the current pub_date is later
        if final_dict[author]["latest_date"] is None or pub_date > final_dict[author]["latest_date"]:
            final_dict[author]["latest_date"] = pub_date

    # Post-process the data for each author
    for author, data in final_dict.items():
        # Calculate average chapters
        data["avg_chapters"] = data["chapter_count"] / data["book_count"]

        # Create publication period as a tuple (earliest_date, latest_date)
        data["publication_period"] = (
            data["earliest_date"],
            data["latest_date"]
        )

        # Clean up unnecessary keys
        del data["chapter_count"]
        del data["book_count"]
        del data["earliest_date"]
        del data["latest_date"]

    return final_dict


# Assuming books.json is already loaded into a variable `books`
final_dict = get_statistics(books)

# Print the result
print(final_dict)

def print_statistics(final_dict: dict):
    for author, data in final_dict.items():
        print(f"Author: {author}")
        print(f"  Total Pages: {data['total_pages']}")
        print(f"  Titles: {', '.join(data['titles'])}")
        print(f"  Average Chapters: {data['avg_chapters']:.2f}")
        print(f"  Publication Period: {data['publication_period'][0]} to {data['publication_period'][1]}")
        print("\n" + "-"*50 + "\n")

# Call the function to print the final dictionary
print_statistics(final_dict)

#Part 2

def get_genres(books: list) -> list:
    genres = set()
    for book in books:
        genre = book["genre"]  # Extract the genre from the current book
        genres.add(genre)  # Add the genre to the set

    return list(genres)
genres = get_genres(books)
print(genres)

