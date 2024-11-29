# Exercise 4

from collections import Counter
import string

#Step 1

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

# Step 2:

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

word_percentages_modulo = {word: (count % total_word_count) for word, count in word_frequencies.items()}

print(" ===== Word Frequency Results =====\n")
unique_words = set()
for word, frequency in word_percentages_modulo.items():
    print(f"{word}: {frequency}")
    unique_words.add(word)

print("\nTotal unique words found in the lyrics: ", len(unique_words),"\n")

# Step 6: Identifying Top 10 Most Frequent Words and Their Percentage of Total

most_common_10_words = word_frequencies.most_common(10)

word_percentages_rounded = {word: (count / total_word_count) for word, count in word_frequencies.items()}

print(most_common_10_words)

print(word_percentages_rounded)

print("===== Word Types and Their Percentage of Total Content ===== \n")

table = []

for word, count in most_common_10_words.items():
    for word, percent in word_percentages_rounded.items():
        if word in most_common_10_words.keys() == word in word_percentages_rounded.keys():
            table.append([word, count, percent])

print(table)


# for row in table:
#     print("{:<10} {:<5} {:<12}".format(*row))
#
# . Display the 10 most frequently used words.
# 2. Calculate and display what percentage these top 10 words comprise of the total word
# count.
# l) Hint
#  Use most_common(10) on the Counter of words to find the top 10 words.
#  Calculate the total count of these top words, and divide by the total word count to find the
# percentage.