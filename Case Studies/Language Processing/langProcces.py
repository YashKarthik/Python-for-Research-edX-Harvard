from collections import Counter


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

read_book('/Users/Yash/Documents/Code/Course-Python-for-research/Case Studies/Language Processing/Books_EngFr/English/shakespeare/Romeo and Juliet.txt')

# Computing word frequency statistics

def word_stats(word_counts):
    """Returns number unique word"""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

