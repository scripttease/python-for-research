# Case Study 5 (week 4 hw2)

for exercise 1 I found the answer on [https://www.tutorialspoint.com/python_pandas/python_pandas_groupby.htm](https://www.tutorialspoint.com/python_pandas/python_pandas_groupby.htm) 

under the aggregate section which was really useful as it wasn't covered in the lectures


For exercise two I got this line `pd.Series(timestamps, index = birddata.index)` from the comments on the forum discussion

Note when copying from the online editor and to remove the annoying windows end of like chars that look like ^M see this link:
[https://stackoverflow.com/questions/5843495/what-does-m-character-mean-in-vim](https://stackoverflow.com/questions/5843495/what-does-m-character-mean-in-vim)

which amounts to:
You can remove all the ^M characters by running the following:

:%s/^M//g

Where ^M is entered by holding down Ctrl and typing v followed by m, and then releasing Ctrl. This is sometimes abbreviated as ^V^M, but note that you must enter it as described in the previous sentence, rather than typing it out literally.

This expression will replace all occurrences of ^M with the empty string (i.e. nothing). I use this to get rid of ^M in files copied from Windows to Unix (Solaris, Linux, OSX).

