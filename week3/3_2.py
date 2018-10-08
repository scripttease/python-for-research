#3.2.2 Counting words
## test string
text = "This is my test text. We're keeping this text short to keep things manageable"
# count words function
def count_words(text):
  # empty dictionary that we will build up
  word_counts = {}
  # split text into words (delim is ' ' if empty)
  for word in text.split():
    # see a word weve seen before and increment it
    if word in word_counts:
      word_counts[word] += 1
    # see a new word and add it as a key with val = 1
    else:
      word_counts[word] = 1
  return word_counts 

# Problems:
## text. is counted differently from text and so are capitalised words...

# text to lowercase
text = text.lower
# all punctuation skipped: (replace with '')
skips = [".", ",", ";", ":", "'", '"']

def count_words(text):
  text = text.lower()
  skips = [".", ",", ";", ":", "'", '"']
  for punct in skips:
    text = text.replace(punct, '')
  word_counts = {}
  for word in text.split():
    if word in word_counts:
      word_counts[word] += 1
    else:
      word_counts[word] = 1
  return word_counts 

# Note that this now has chaged we're to were which isnt ideal...
# we can also use Counter...
from collections import Counter

def count_words_fast(text):
  text = text.lower()
  skips = [".", ",", ";", ":", "'", '"']
  for punct in skips:
    text = text.replace(punct, '')

  word_counts = Counter(text.split(" "))
  return word_counts 

# note that although they look like they are different types, counter is actually a kind of dict so the two methods return identical results:

a = count_words(text)
b = count_words_fast(text)
a == b
# returns true

### 3.2.3 reading in a book

def read_book(title_path):
  """ This fn will read in a book and return it as a string   """
  with open(title_path, 'r', encoding='utf8') as current_file:
    text = current_file.read()
    text = text.replace('\n', '').replace('\r','')
  return text

text = read_book("./Books_EngFr/English/shakespeare/Romeo and Juliet.txt")
len(text)
# returns 169275
# But is it the right book

index_of_quote = text.find("What's in a name?")
index_of_quote 
# returns 42757

sample = text[42757:42800]
sample
# returns "What's in a name? That which we call a rose"

### 3.2.4 computing word frequency statistics

# calc number of unique words and the word count frequencies

def word_stats(word_counts):
  """return number of unique words and word frequenvies """
  num_unique_words = len(word_counts)
  counts = word_counts.values()
  return (num_unique_words, counts)

  
word_stats_text = word_stats(count_words_fast(text))
(num_unique, counts) = word_stats(count_words_fast(text))
num_unique
#returns 5118
sum(counts)
# returns 40776

#### compare with the german translation
text_ger = read_book('./Books_GerPort/German/shakespeare/Romeo und Julia.txt')
word_counts = count_words(text_ger)
(num_unique, counts) = word_stats(count_words_fast(text_ger))
print(num_unique, sum(counts))
# returns7527 20311

#### 3.2.5 Reading multiple files
# for reading directories
import os
# store a folder
book_dir = './Books'
os.listdir(book_dir)
# returns ['.DS_Store', 'German', 'English', 'Portuguese', 'French']

# Read in all books from their subdirs:

for language in os.listdir(book_dir):
  for author in os.listdir(book_dir + "/" + language):
    for title in os.listdir(book_dir + "/" + language + '/' + author):
      inputfile = book_dir + "/" + language + '/' + author + '/' + title
      print(inputfile)
      text = read_book(inputfile)
      (num_unique, counts) = word_stats(count_words(text))

# This works for the lecturer but I have a mac so I have a .ds store file. Modified code:
# make a fn that removes DS_Store if there is one:
def listdir(path):
  # listdir = os.listdir(path)
  # try:
  #   listdir.remove('.DS_Store')
  # except ValueError:
  #   pass
  # return listdir
  return filter(
      lambda x: x != ".DS_Store", 
      os.listdir(path)
      )
  # refactored version uses filter which returns all that matches lambda condition

# now code from lecture works...
for language in listdir(book_dir):
  for author in listdir(book_dir + "/" + language):
    for title in listdir(book_dir + "/" + language + '/' + author):
      inputfile = book_dir + "/" + language + '/' + author + '/' + title
      print(inputfile)
      text = read_book(inputfile)
      (num_unique, counts) = word_stats(count_words(text))

### vv Louis refactors everything vv ###

def process(inputfile):
  print(inputfile)
  text = read_book(inputfile)
  (num_unique, counts) = word_stats(count_words(text))
  return (num_unique, counts) 

files = [
    process(book_dir + "/" + language + "/" + author + "/" + title)
    for language in listdir(book_dir)
    for author in listdir(book_dir + "/" + language)
    for title in listdir(book_dir + "/" + language + "/" + author)
    ]

import itertools

# Library functions

def path_join(path, child):
  return path + "/" + child

def flat_map(mapper, iterable):
  return itertools.chain.from_iterable(map(mapper, iterable))

# Business logic

def expand_path(path):
  return map(lambda child: path_join(path, child), listdir(path))

def expand_paths(paths):
  return flat_map(expand_path, paths)

paths = expand_paths(expand_paths(expand_paths([book_dir])))

print(list(paths))

### ^Louis refactors everything^ ###

# using pandas library

import pandas as pd

# create a table using DataFrame with 2 columns, name and age
table = pd.DataFrame(columns = ("name", "age"))
# add data based on the location of the entry to be added
table.loc[1] = "James", 22
table.loc[2] = "Jess", 32

table
#Out[285]:
    # name age
# 1  James  22
# 2   Jess  32

table.columns
# Returns: Index(['name', 'age'], dtype='object')

#### Stats for our word counts for all the books with DataFrame and pandas
import os
import pandas as pd

stats = pd.DataFrame(columns = ("language", 'author', 'title', 'length', 'unique'))

def listdir(path):
  return filter(
      lambda x: x != ".DS_Store", 
      os.listdir(path)
      )

book_dir = './Books'
title_num = 1

for language in listdir(book_dir):
  for author in listdir(book_dir + "/" + language):
    for title in listdir(book_dir + "/" + language + '/' + author):
      inputfile = book_dir + "/" + language + '/' + author + '/' + title
      print(inputfile)
      text = read_book(inputfile)
      (num_unique, counts) = word_stats(count_words(text))
      stats.loc[title_num] = language, author, title, sum(counts), num_unique
      title_num += 1

stats
# returns whole table
# first 5 rows
stats.head()
# Out[292]:
#   language    author  ...   length unique
# 1   German  schiller  ...    13302   4378
# 2   German  schiller  ...    22349   6654
# 3   German  schiller  ...    18515   6158
# 4   German  schiller  ...    28042  10370
# 5   German  schiller  ...    28433   9968

# [5 rows x 5 columns]


# last 5 rows
stats.tail()
# returns last 5 rows

##### Problems
# 1 capitalise author name
# 2 get rid of .txt in book title

for language in listdir(book_dir):
  for author in listdir(book_dir + "/" + language):
    for title in listdir(book_dir + "/" + language + '/' + author):
      inputfile = book_dir + "/" + language + '/' + author + '/' + title
      print(inputfile)
      text = read_book(inputfile)
      (num_unique, counts) = word_stats(count_words(text))
      # make changes here:
      stats.loc[title_num] = language, author.capitalize(), title.replace('.txt', ''), sum(counts), num_unique
      title_num += 1

###### 3.2.6 plotting book stats

stats.length
# returns the loc and the length column

stats.author.head()
# Out[304]:
# 1    schiller
# 2    schiller
# 3    schiller
# 4    schiller
# 5    schiller
# Name: author, dtype: object

## plotting
import matplotlib.pyplot as plt

# simple scatter:

plt.plot(stats.length, stats.unique, 'bo')
plt.show()

# log scales
plt.loglog(stats.length, stats.unique, 'bo')
plt.show()

# stratify data with pandas
stats[stats.language == "English"]
stats[stats.language == "French"]

#use diff colours for diff langs
plt.figure(figsize = (10,10))
subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, 'o', label = 'English', color = 'crimson')

subset = stats[stats.language == "French"]
plt.loglog(subset.length, subset.unique, 'o', label = 'French', color = 'forestgreen')

subset = stats[stats.language == "German"]
plt.loglog(subset.length, subset.unique, 'o', label = 'German', color = 'orange')

subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length, subset.unique, 'o', label = 'Portuguese', color = 'blueviolet')
plt.legend()
plt.xlabel("Book length")
plt.ylabel('Number of Unique words')
plt.savefig('lang_plot.pdf')
plt.show()

#### nb can also access dataframe using this syntax
stats["unique"]
