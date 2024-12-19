#Exercise: Text Analysis and Manipulation on Song Lyrics

from collections import Counter
import string
import logging
import sys

#Step 8: Logging the output

log_file = "execution_log.txt"

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[
        logging.FileHandler(log_file, mode="w"),
        logging.StreamHandler(sys.stdout),
    ]
)

class ConsoleLogger:
    def __init__(self, logger):
        self.logger = logger
    def write(self, message):
        if message.strip():
            self.logger.info(message)
    def flush(self):
        pass

sys.stdout = ConsoleLogger(logging.getLogger())

#Step 1: Storing Lyrics in a File

lyrics = """… So, so you think you can tell heaven from hell?
Blue skies from pain?
Can you tell a green field from a cold steel rail?
A smile from a veil?
Do you think you can tell?
… Did they get you to trade your heroes for ghosts?
Hot ashes for trees?
Hot air for a cool breeze?
Cold comfort for change?
Did you exchange a walk on part in the war
For a lead role in a cage?
… How I wish, how I wish you were here
We're just two lost souls swimming in a fish bowl
Year after year
Running over the same old ground, what have we found?
The same old fears, wish you were here"""

with open('song.txt', 'w', encoding='utf-8') as file:
    file.write(lyrics)


#Step 2: Display the Lyrics Content

with open('song.txt', 'r', encoding='utf-8') as file:
    content = file.read()


print("===== Contents of 'song.txt' ===== \n")
print(content,"\n")

#Step 3: Counting Letter Frequencies

letter_frequencies = Counter(char.lower() for char in lyrics if char.lower() in string.ascii_lowercase)

non_alphabet_count = sum(1 for char in lyrics if char not in string.ascii_letters)

print("==== Letter Frequencies Results ==== \n")
for letter, count in sorted(letter_frequencies.items()):
    print(f"{letter}: {count}")

print("\nNon-alphabet characters:", non_alphabet_count,"\n")

#Step 4: Identifying Most and Least Frequently Used Characters

most_common_chars = letter_frequencies.most_common(5)

least_common_chars = letter_frequencies.most_common()[:-6:-1]

unused_letters = [char for char in string.ascii_lowercase if char not in letter_frequencies]

print("===== Top 5 Most Frequently Used Characters =====")
for char, freq in most_common_chars:
    print(f"{char}: {freq}")

print("\n===== Top 5 Least Frequently Used Characters =====")
for char, freq in least_common_chars:
    print(f"{char}: {freq}")

print("\n===== Unused Alphabet Characters =====")
print(", ".join(unused_letters))

#Step 5: Counting Words and Unique Word Frequencies

processed_lyrics = lyrics.translate(str.maketrans('', '', string.punctuation)).lower()
words = processed_lyrics.split()
word_frequencies = Counter(words)
total_words = sum(word_frequencies.values())
word_percentages = {word: (freq / total_words) * 100 for word, freq in word_frequencies.items()}

print(" ===== Word Frequency Results =====\n")

unique_words = set()
for word, count in word_frequencies.items():
    print(f"{word}: {count}")
    unique_words.add(word)

print("\nTotal unique words found in the lyrics: ", len(unique_words),"\n")

table = [
    ["Word", "Occurencies", "Percentage (%)"],
    ["----------","-----------","---------------"]
        ]

for word, count in word_frequencies.items():
    percentage = word_percentages[word]
    table.append([word, count, f"{percentage:.2f}"])

print("===== Word Types and Their Percentage of Total Content ===== \n")

row_format = "{:<10} {:<11} {:<15}"
for row in table:
    print(row_format.format(*row))

#Step 6: Identifying Top 10 Most Frequent Words and Their Percentage of Total

top_10_words = word_frequencies.most_common(10)
top_10_total = sum(freq for _, freq in top_10_words)
top_10_percentage = (top_10_total / total_words) * 100

print("\n===== Top 10 Most Frequently Used Words =====\n")
for word, count in top_10_words:
    print(f"{word}: {count}")

print(f"\nTop 10 words account for {top_10_percentage}% of the total words in the song.")

#Step 7: Reversing the Lyrics and Saving to a New File

reversed_lyrics = lyrics[::-1]

with open('reversed.txt', 'w', encoding='utf-8') as file:
    file.write(reversed_lyrics)

with open('reversed_song.txt', 'r', encoding='utf-8') as file:
    reversed_content = file.read()

print("\n===== Reversed Content of 'song.txt' =====\n")
print(reversed_lyrics,"\n")

#Step 8: Logging the Output / see above
