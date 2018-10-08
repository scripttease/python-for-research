#Exercise 1
#In this case study, we will find and visualize summary statistics of the text of different translations of Hamlet. For this case study, functions count_words_fast, read_book, and word_stats are already defined as in the Case 2 Videos (Videos 3.2.x).

#book_titles is a nested dictionary, containing book titles within authors within languages, all of which are strings. These books are all stored online, and are accessed throughout this case study. In this exercise, we will first read in and store each translation of Hamlet.

#Define hamlets as a pandas dataframe with columns language and text.
#Add an if statement to check if the title is equal to 'Hamlet'.
#Store the results from read_book(inputfile) to text.
#Consider: How many translations are there? Which languages are they translated into?

# Sample code
hamlets = 1## Enter code here! ##
book_dir = "Books"
title_num = 1
for language in book_titles:
    for author in book_titles[language]:
        for title in book_titles[language][author]:
          if 1:## Enter code here! ##:
                inputfile = data_filepath+"Books/"+language+"/"+author+"/"+title+".txt"
                text = 1## Enter code here! ##
                hamlets.loc[title_num] = language, text
                title_num += 1


# solution:
import pandas as pd
hamlets = pd.DataFrame(columns= ('language', 'text'))
# This only works in the code HW env because 'Books' is defined there
book_dir = "Books"
title_num = 1
for language in book_titles:
    for author in book_titles[language]:
        for title in book_titles[language][author]:
            if title == 'Hamlet':
                inputfile = data_filepath+"Books/"+language+"/"+author+"/"+title+".txt"
                text = read_book(inputfile)
                hamlets.loc[title_num] = language, text
                title_num += 1

hamlets

#Exercise 2
#In this case study, we will find and visualize summary statistics of the text of different translations of Hamlet. For this case study, functions count_words_fast, read_book, and word_stats are already defined as in the Case 2 Videos (Videos 3.2.x)

#In this exercise, we will summarize the text for a single translation of Hamlet in a pandas dataframe. The language and text of the first translation of Hamlet in hamlets is given in the code section.
#Find the dictionary of word frequency in text by calling count_words_fast(). Store this as counted_text.
#Create a pandas dataframe named data.
#Using counted_text, define two columns in data:
#word, consisting of each unique word in text.
#count, consisting of the number of times each word in word is included in the text.
import pandas as pd

language, text = hamlets.iloc[0]

counted_text = count_words_fast(text)

data = pd.DataFrame(columns=('word', 'text'))
word_num = 1
for word in counted_text:
    unique = word
    print(word)
    counts = counted_text[word]
    print(counts)
    data.loc[word_num] = unique, count
    # this works but only gives one row in dat
word_num = 1
for word in counted_text:
    unique = word
    print(word)
    counts = counted_text[word]
    print(counts)
    data.loc[word_num] = unique, count
    word_num += 1
# thsi times out :( !!!
# Louis way:
# turn the dict into 2 lists
words = []
counts = []
for word in counted_text:
    words.append(word)
    counts.append(counted_text[word])
    
data = pd.DataFrame(data={'word': words, 'count': counts})

## official code from next section is this:
# note this works cos in Python3.6 onwards, dicts are ordered
data = pd.DataFrame({
    "word": list(counted_text.keys()),
    "count": list(counted_text.values())
})
#Exercise 3
#In this case study, we will find and visualize summary statistics of the text of different translations of Hamlet. For this case study, functions count_words_fast, read_book, and word_stats are already defined as in the Case 2 Videos (Videos 3.2.x)

#In this exercise, we will continue to define summary statistics for a single translation of Hamlet. The solution code from the previous section is already included here.

#Add a column to data named length, defined as the length of each word.
#Add another column named frequency, which is defined as follows for each word in data:
#If count > 10, frequency is frequent.
#If 1 < count <= 10, frequency is infrequent.
#If count == 1, frequency is unique

language, text = hamlets.iloc[0]

counted_text = count_words_fast(text)

data = pd.DataFrame({
    "word": list(counted_text.keys()),
    "count": list(counted_text.values())
})
# Add a column to data named length, defined as the length of each word.
words = list(counted_text.keys())
word_len = []
for word in words:
    length = len(word)
    word_len.append(length)
#print(word_len)
data['length'] = word_len
data.head()

# Add column frequency:
freq = []
counts = list(counted_text.values())
for count in counts:
    if count == 1:
        freq.append('unique')
    elif count <= 10:
        freq.append('infrequent')
    else:
        freq.append('frequent')

data['frequency'] = freq
data.head()
