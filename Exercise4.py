# Exercise 4

from collections import Counter
import string
import logging
import sys


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

# Step 1: Storing Lyrics in a File

song = """
… So, so you think you can tell heaven from hell? 
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
The same old fears, wish you were here 
"""

with open('song.txt', 'w', encoding='utf-8') as file:
    file.write(song)

# Step 2: Display the Lyrics Content

with open('song.txt', 'r', encoding='utf-8') as file:
    content = file.read()

print("===== Contents of 'song.txt' ===== \n")
print(content,"\n")

# Step 3: Counting Letter Frequencies

letter_counts = Counter(char.lower() for char in song if char.lower() in string.ascii_lowercase)

non_alpha_counts = sum(1 for char in song if char not in string.ascii_letters)

print("==== Letter Frequencies Results ==== \n")
for letter, count in sorted(letter_counts.items()):
    print(f"{letter}: {count}")

print("\nNon-alphabet characters:", non_alpha_counts,"\n")

# Step 4: Identifying Most and Least Frequently Used Characters

most_common_5_char = letter_counts.most_common(5)

least_common_5_char = letter_counts.most_common()[:-6:-1]

unused_letters = [letter for letter in string.ascii_lowercase if letter not in letter_counts]

print("===== Top 5 Least Frequently Used Characters =====\n")
for char, count in sorted(least_common_5_char):
    print(f"{char}: {count}\n")

print("===== Top 5 Least Frequently Used Characters =====\n")
for char, count in sorted(most_common_5_char):
    print(f"{char}: {count}\n")

print("===== Unused Alphabet Characters =====\n")
for letter in unused_letters:
    print(letter)

#Step 5: Counting Words and Unique Word Frequencies

cleaned_song = song.translate(str.maketrans('', '', string.punctuation)).lower()

words = cleaned_song.split()

total_word_count = len(words)

word_frequencies = Counter(words)

word_percentages = {word: (count / total_word_count) for word, count in word_frequencies.items()}

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
    for word2, percent in word_percentages.items():
        if word == word2:
            table.append([word, count, percent])
        else:
            continue

print("===== Word Types and Their Percentage of Total Content ===== \n")

row_format = "{:<10} {:<11} {:<15}"
for row in table:
    print(row_format.format(*row))

# Step 6: Identifying Top 10 Most Frequent Words and Their Percentage of Total

most_common_10_words = word_frequencies.most_common(10)

most_common_10_words_total_count = 0
for word, count in most_common_10_words:
    most_common_10_words_total_count += count

total_most_common_10_wordsword_percentages = most_common_10_words_total_count/total_word_count * 100

print("\n===== Top 10 Most Frequently Used Words =====\n")
for word, count in most_common_10_words:
    print(f"{word}: {count}")

print(f"\nTop 10 words account for {total_most_common_10_wordsword_percentages}% of the total words in the song.")

# Step 7: Storing Lyrics in a File

reversed_song = song[::-1]

with open('reversed_song.txt', 'w', encoding='utf-8') as file:
    file.write(reversed_song)

with open('reversed_song.txt', 'r', encoding='utf-8') as file:
    reversed_content = file.read()

print("\n===== Reversed Content of 'song.txt' =====\n")
print(reversed_content,"\n")


# Step 8: Logging the Output / see above