from collections import Counter
import os
import pandas as pd
import matplotlib.pyplot as plt 


book_dir = 'Language Processing/Books'
test_str = 'This is just a test string to keep things manageable...'

def count_words(text):
    """Counts the number of occurences of each word in given text."""

    text = text.lower()
    skips = [',','.',';',':','""',"''"]
    for char in skips:
        text = text.replace(char, '')
    word_counts = {}
    for word in text.split(' '):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

# Function using Counter method

def fast_count(text):
    """Counts the occurences of each word omitting 
    punctuation"""
    text = text.lower()
    skips = [',','.',';',':','""',"''"]
    for char in skips:
        text = text.replace(char, '')

    word_counts = Counter(text.split(" "))
    return word_counts


# Reading from a book

def read_book(title_path):
    """Reads a book from the given path and returns it as a string"""

    with open(title_path, 'r', encoding='utf8') as currentfile:
        text = currentfile.read()
        text = text.replace('\n', '').replace('\r', '')
        return text

# Computing word frequency statistics

def word_stats(word_counts):
    """Returns number unique word"""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

stats = pd.DataFrame(columns=('Language', 'Author', 'Title', 'Length', 'Unique'))
title_num = 1



for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + '/' + language):
        for title in os.listdir(book_dir + '/' + language + '/' + author):
            inputfile = book_dir + '/' + language + '/' + author + '/' + title
            print(inputfile)
            text = read_book(inputfile)
            num_unique = word_stats(count_words(text))
            stats.loc[title_num]= language,author.capitalize(),title.replace(".txt",""),sum(word_stats.counts),num_unique
            title_num += 1

# Plot

plt.figure(figsize = (10, 10))
subset = stats[stats.language == "English"]
plt.loglog(subset.length,  subset.unique, "o", label = "English", color = "crimson");

subset = stats[stats.language == "French"]
plt.loglog(subset.length,  subset.unique, "o", label = "French", color = "forestgreen");

subset = stats[stats.language == "German"]
plt.loglog(subset.length,  subset.unique, "o", label = "German", color = "orange");

subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length,  subset.unique, "o", label = "Portuguese", color = "blueviolet");

plt.legend()
plt.xlabel("Book length")
plt.ylabel("Number of unique words")
plt.savefig("lang_plot.pdf")