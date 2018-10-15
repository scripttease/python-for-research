# 4.1.1 panda series and dataframe

import pandas as pd
x = pd.Series([6,3,8,6])
x
# Out[61]:
# 0    6
# 1    3
# 2    8
# 3    6
# dtype: int64

# can explicitly define the index

x = pd.Series([6,3,8,6], index = ["q", "w", "e", "r"])
# In [64]: x
# Out[64]:
# q    6
# w    3
# e    8
# r    6
# dtype: int64

# can now search based on index:
x["w"]
#3

x[["w","r"]]
# Out[66]:
# w    3
# r    6
# dtype: int64

# series using a dict

age = {"Tim":29, "Jim":31, "Pam":27, "Sam":35}
x = pd.Series(age)
# Out[73]:
# Tim    29
# Jim    31
# Pam    27
# Sam    35
# dtype: int64

# note that in the lecture series he says that the Series sorts the output but for me it certainly doesn't

# dataframes
# provide 2 args, data and colums

data = {'name' : ['Tim', 'Jim', 'Pam', 'Sam'],
        'age' : [29,31,27,35],
        'ZIP' : ['02115', '02130', '67700', '00100']}

x = pd.DataFrame(data, columns = ['name', 'age', 'ZIP'])
  # name  age    ZIP
# 0  Tim   29  02115
# 1  Jim   31  02130
# 2  Pam   27  67700
# 3  Sam   35  00100

x = pd.DataFrame(data, columns = ['name', 'ZIP', 'age'])
# it knows which col is which.
# Out[79]:
#   name    ZIP  age
# 0  Tim  02115   29
# 1  Jim  02130   31
# 2  Pam  67700   27
# 3  Sam  00100   35

x = pd.DataFrame(data, columns = ['name', 'age', 'code'])
# you have to get names right
# Out[81]:
#   name  age code
# 0  Tim   29  NaN
# 1  Jim   31  NaN
# 2  Pam   27  NaN
# 3  Sam   35  NaN

# retrieving data using column name
x["age"]
# Out[82]:
# 0    29
# 1    31
# 2    27
# 3    35
# Name: age, dtype: int64

x.name
# retrieve data using dot notation
# Out[83]:
# 0    Tim
# 1    Jim
# 2    Pam
# 3    Sam
# Name: name, dtype: object

# series and dataframe reindexing

x = pd.Series([6,3,8,6], index = ["q", "w", "e", "r"])

x.index
# Out[84]: Index(['q', 'w', 'e', 'r'], dtype='object')

s = sorted(x.index)

x.reindex(s)
# Out[86]:
# e    8
# q    6
# r    6
# w    3
# dtype: int64

#arithmetic on pandas:

x = pd.Series([6,3,8,6], index = ["q", "w", "e", "r"])
y = pd.Series([7,3,5,2], index = ["e", "q", "r", "t"])
# Out[88]:
# e    15.0
# q     9.0
# r    11.0
# t     NaN
# w     NaN
# dtype: float64

#4.1.2 loading and inspecting data

pwd
# can do pwd in ipython and cd!
'/Users/al/projects/edx'

import numpy as np

import pandas as pd

pwd
'/Users/al/projects/edx'

cd python-for-research/week4
/Users/al/projects/edx/python-for-research/week4

whisky = pd.read_csv("whiskies.txt")

whisky["Region"] = pd.read_csv("regions.txt")

# examine data
whisky.columns

Index(['RowID', 'Distillery', 'Body', 'Sweetness', 'Smoky', 'Medicinal',
       'Tobacco', 'Honey', 'Spicy', 'Winey', 'Nutty', 'Malty', 'Fruity',
       'Floral', 'Postcode', ' Latitude', ' Longitude', 'Region'],
      dtype='object')

# examine just the flavors

# all rows but only cols 2 to 13:

flavors = whisky.iloc[:, 2:14]

flavors

    Body  Sweetness  Smoky  Medicinal   ...    Nutty  Malty  Fruity  Floral
0      2          2      2          0   ...        2      2       2       2
1      3          3      1          0   ...        2      3       3       2
...
...

#4.1.3 exploring correlations
## Compute pairwise the corerlation of columns in the flavors dataframe
## Assign output tp a variable called corr_flavors
corr_flavors = pd.DataFrame.corr(flavors)

import matplotlib.pyplot as plt


plt.figure(figsize=(10,10))
<Figure size 1000x1000 with 0 Axes>

# use psudocolor (pcolor) fn to plot the correlation matrix

plt.pcolor(corr_flavors)
<matplotlib.collections.PolyCollection at 0x1102dceb8>

plt.colorbar()
<matplotlib.colorbar.Colorbar at 0x11032a358>

plt.savefig("corr.pdf")

plt.show
<function matplotlib.pyplot.show(*args, **kw)>

plt.show()

# see a correlation between 3 and 4, 0 and 3, looking at

In [121]: flavors.columns
Out[121]:
Index(['Body', 'Sweetness', 'Smoky', 'Medicinal', 'Tobacco', 'Honey', 'Spicy',
       'Winey', 'Nutty', 'Malty', 'Fruity', 'Floral'],
      dtype='object'

# we see that body correlates stongly with smoky, medicinal and winey but inversely with floral.
# Again we see that floral and medicinal have a very strong negative corelation

# to look at corellations among whiskies across flavors we need to transponse out table - think of it as a corelation netween distillery and flavor profile

corr_whisky = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize = (10,10))
plt.pcolor(corr_whisky)
plt.axis("tight")
plt.colorbar()
plt.savefig("corr_whisky.pdf")

# this would gives a 90x90 plot BUT we only have 86 data points so there is some white space which we fix above with plot axis tight

# you can see that we are getting corelations in the data but they are hard to decipher.

#4.1.4 Clustering whiskies by Flavour profile
