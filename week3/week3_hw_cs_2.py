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

## Note there is a better way to add a new column based on manipulating a prev column:
data["length"] = data["word"].apply(len)

data.loc[data["count"] > 10,  "frequency"] = "frequent"
data.loc[data["count"] <= 10, "frequency"] = "infrequent"
data.loc[data["count"] == 1,  "frequency"] = "unique"

#Exercise 4
#In this case study, we will find and visualize summary statistics of the text of different translations of Hamlet. For this case study, functions count_words_fast, read_book, and word_stats are already defined as in the Case 2 Videos (Videos 3.2.x)

#In this exercise, we will summarize the statistics in data into a smaller pandas dataframe. The solution code from the previous section is already included here.


#Create a pandas dataframe named sub_data including the following columns:
#language, which is the language of the text.
#frequency, which is a list containing the strings "frequent", "infrequent", and "unique".
#mean_word_length, which is the mean word length of each value in frequency.
#num_words, which is the total number of words in each frequency category.

language, text = hamlets.iloc[0]

counted_text = count_words_fast(text)

data = pd.DataFrame({
    "word": list(counted_text.keys()),
    "count": list(counted_text.values())
})

data["length"] = data["word"].apply(len)

data.loc[data["count"] > 10,  "frequency"] = "frequent"
data.loc[data["count"] <= 10, "frequency"] = "infrequent"
data.loc[data["count"] == 1,  "frequency"] = "unique"
#

freq = data[data.frequency == 'frequent']
infreq = data[data.frequency == 'infrequent']
unique = data[data.frequency == 'unique']

num_freq = len(freq)
num_infreq = len(infreq)
num_unique = len(unique)

freq_length = data.loc[data["frequency"] == "frequent"]["length"]

mean_freq_length = (sum(freq_length))/(len(freq_length))

infreq_length = data.loc[data["frequency"] == "infrequent"]["length"]

mean_infreq_length = (sum(infreq_length))/(len(infreq_length))

unique_length = data.loc[data["frequency"] == "unique"]["length"]

mean_unique_length = (sum(unique_length))/(len(unique_length))

sub_data = pd.DataFrame({
    "language": language,
    "frequency": ["frequent", "infrequent", "unique"],
    "mean_word_length": [mean_freq_length, mean_infreq_length, mean_unique_length],
    "num_words": [num_freq, num_infreq, num_unique]
})

# returns
# In [21]: sub_data.head()
# Out[21]: 
#     frequency    language  mean_word_length  num_words
# 0    frequent  Portuguese          4.417625        261
# 1  infrequent  Portuguese          6.497870       1643
# 2      unique  Portuguese          8.669778       5357

# This works fine but was not accepted because they want you to use groupby which makes the indexes strings see below!!!

language, text = hamlets.iloc[0]

counted_text = count_words_fast(text)

data = pd.DataFrame({
    "word": list(counted_text.keys()),
    "count": list(counted_text.values())
})

data["length"] = data["word"].apply(len)

data.loc[data["count"] > 10,  "frequency"] = "frequent"

data.loc[data["count"] <= 10, "frequency"] = "infrequent"
data.loc[data["count"] == 1,  "frequency"] = "unique"

# supplied code above, answer code below

sub_data = pd.DataFrame({
    "language": language,
    "frequency": ["frequent", "infrequent", "unique"],
    "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
    "num_words": data.groupby(by = "frequency")["length"].sum()
})
# In [4]: sub_data
# Out[4]: 
#              frequency language  mean_word_length  num_words
# frequency                                                   
# frequent      frequent   German          4.528053       1372
# infrequent  infrequent   German          6.481830      10345
# unique          unique   German          9.006987      50277

# still not accepted. Giving up!
# ok answer was:
sub_data = pd.DataFrame({
    "language": language,
    "frequency": ["frequent", "infrequent", "unique"],
    "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
    "num_words": data.groupby(by = "frequency")["length"].size()
})
# .apply(len) should also work I believe

# In [2]: sub_data
# Out[2]: 
#              frequency language  mean_word_length  num_words
# frequency                                                   
# frequent      frequent   German          4.528053        303
# infrequent  infrequent   German          6.481830       1596
# unique          unique   German          9.006987       5582

# ooooops I had summed the word lengths instead of counting word numbers in this case

#Exercise 5
#In this case study, we will find and visualize summary statistics of the text of different translations of Hamlet. For this case study, functions count_words_fast, read_book, and word_stats are already defined as in the Case 2 Videos (Videos 3.2.x)

#In this exercise, we will join all the data summaries for text Hamlet translation.

#The previous code for summarizing a particular translation of Hamlet is consolidated into a single function called summarize_text. Create a pandas dataframe grouped_data consisting of the results of summarize_text for translation of Hamlet in hamlets.
#Use a for loop across the row indices of hamlets to assign each translation to a new row.
#Obtain the ith row of hamlets to variables using the .iloc method, and assign the output to variables language and text.
#Call summarize_text using language and text, and assign the output to sub_data.
#Use the pandas .append() function to append to pandas dataframes row-wise to grouped_data.

#given code
def summarize_text(language, text):
    counted_text = count_words_fast(text)

    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })
    
    data.loc[data["count"] > 10,  "frequency"] = "frequent"
    data.loc[data["count"] <= 10, "frequency"] = "infrequent"
    data.loc[data["count"] == 1,  "frequency"] = "unique"
    
    data["length"] = data["word"].apply(len)
    
    sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent","infrequent","unique"],
        "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
        "num_words": data.groupby(by = "frequency").size()
    })
    
    return(sub_data)
    
# Enter your code here.
# my attempts:

language, text = hamlets.iloc[0]
summarize_text(language, text)

grouped_data = pd.DataFrame(columns=("language", "text"))
#len(hamlets)

#for i in len(hamlets)
#for index, row in df.iterrows():
#   print row['c1'], row['c2']
for index, row in hamlets.iterrows():
  language, text = hamlets.iloc[index] 
  summarize_text(language, text)

language, text = hamlets.iloc[0]
summarize_text(language, text)

grouped_data = pd.DataFrame(columns=("language", "text"))
#len(hamlets)

#for i in len(hamlets)
#for index, row in df.iterrows():
#   print row['c1'], row['c2']

for index, row in hamlets.iterrows():
   #print(row)
   #print(index)
   for index, row in hamlets.iterrows():
       language, text = hamlets.iloc[index-1]
       print(language)
       grouped_data.append(summarize_text(language, text))

  ###
for i in range(grouped_data.shape[0]):
    row = grouped_data.iloc[i]

###
grouped_data = pd.DataFrame(columns=("language", "frequency", "mean_word_length", "num_words"))

for i in range(hamlets.shape[0]):
    language, text = hamlets.iloc[i]
    sub_data = summarize_text(language, text)
    grouped_data.append(sub_data)
    ###
    grouped_data = pd.DataFrame(columns=("language", "frequency", "mean_word_length", "num_words"))

for i in range(hamlets.shape[0]):
    language, text = hamlets.iloc[i]
    sub_data = summarize_text(language, text)
    grouped_data.append(sub_data)


###
grouped_data = pd.DataFrame(columns=("frequency","language", "mean_word_length", "num_words"))

for i in range(hamlets.shape[0]):
  language, text = hamlets.iloc[i]
  sub_data = summarize_text(language, text)
  print(sub_data)
  grouped_data.append(sub_data)

### I gave up and took the hint - it docked me 30 xp AND There was no fucking hint. it literally said sorry no hint on this one. I . Am. FUMING

# Exercise 6
# In this case study, we will find and visualize summary statistics of the text of different translations of Hamlet. For this case study, functions count_words_fast, read_book, and word_stats are already defined as in the Case 2 Videos (Videos 3.2.x)

# In this exercise, we will plot our results and look for differences across each translation.
# Plot the word statistics of each translations on a single plot. Note that we have already done most of the work for you.
# Consider: do the word statistics differ by translation?

colors = {"Portuguese": "green", "English": "blue", "German": "red"}
markers = {"frequent": "o","infrequent": "s", "unique": "^"}
import matplotlib.pyplot as plt
for i in range(grouped_data.shape[0]):
    row = grouped_data.iloc[i]
    plt.plot(row.mean_word_length, row.num_words,
        marker=markers[row.frequency],
        color = colors[row.language],
        markersize = 10
    )

color_legend = []
marker_legend = []
for color in colors:
    color_legend.append(
        plt.plot([], [],
        color=colors[color],
        marker="o",
        label = color, markersize = 10, linestyle="None")
    )
for marker in markers:
    marker_legend.append(
        plt.plot([], [],
        color="k",
        marker=markers[marker],
        label = marker, markersize = 10, linestyle="None")
    )
plt.legend(numpoints=1, loc = "upper left")

plt.xlabel("Mean Word Length")
plt.ylabel("Number of Words")
plt.show()

# I literally only had to type plt.show() for this to pass. Sigh
