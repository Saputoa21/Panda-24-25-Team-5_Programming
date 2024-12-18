#Exercise: Text Analysis and Manipulation on Song Lyrics

from collections import Counter
import string
import logging

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

print("\nTotal Word Count:", total_words)
print("\nWord Frequencies:")
for word, freq in word_frequencies.items():
    print(f"{word}: {freq} ({word_percentages[word]:.2f}%)")

#Step 6: Identifying Top 10 Most Frequent Words and Their Percentage of Total

top_10_words = word_frequencies.most_common(10)
top_10_total = sum(freq for _, freq in top_10_words)
top_10_percentage = (top_10_total / total_words) * 100

print("\nTop 10 Most Frequent Words:")
for word, freq in top_10_words:
    print(f"{word}: {freq}")

print(f"\nTop 10 words comprise {top_10_percentage:.2f}% of the total word count.")

#Step 7: Reversing the Lyrics and Saving to a New File

reversed_lyrics = lyrics[::-1]

with open('reversed.txt', 'w', encoding='utf-8') as file:
    file.write(reversed_lyrics)


print("\nReversed Lyrics:", reversed_lyrics)

#Step 8: Logging the Output

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('execution_log.txt', encoding='utf-8')
    ]
)
logger = logging.getLogger()
