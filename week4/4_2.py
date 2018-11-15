
# 4.2.1 GPS tracking of birds

import pandas as pd
import matplotlib.pyplot as plt

birddata = pd.read_csv("bird_tracking.csv")

# 4.2.2 simple data vis
# get indicies just for bird called eric
ix = birddata.bird_name == "Eric"

# get x and y data using the indicies that are erics
x, y = birddata.longitude[ix], birddata.latitude[ix]

# plot these:
plt.figure(figsize=(7,7))
# plot using blue dots "."
plt.plot(x,y,".")
# Plot for all three birds

# extract names uniquely:
bird_names = pd.unique(birddata.bird_name)
# loop over 3 names to get same data as before

# dot_col = ['r.','y.','b.']

plt.figure(figsize=(7,7))
for bird in bird_names:
  # col_ix = 0
  # col = dot_col[col_ix]
  ix = birddata.bird_name == bird
  x, y = birddata.longitude[ix], birddata.latitude[ix]
  # col_ix +=1
  # plt.plot(x,y,col)
  plt.plot(x,y,'.', label=bird)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.savefig('3trajectct.pdf')

# NB IT AUTOMATICALLY changes the "."colour with each iteration of the loop but how would i do this otherwie?
# tried above see commenys but did NOT work
#TODO

# 4.2.3 examining flight speed

In [5]: plt.show()

In [6]: ix = birddata.bird_name == 'Eric'

In [7]: speed = birddata.speed_2d[ix]

In [8]: plt.hist(speed)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-8-5148c32c13be> in <module>()
----> 1 plt.hist(speed)
...

# looks like some nan numbers
In [13]: sum(np.isnan(speed))
Out[13]: 85

In [14]: sum(np.isnan(speed[:10]))
Out[14]: 0

# another way
np.isnan(speed).any()
#true

# remove nans
ix_nan = np.isnan(speed)

plt.hist(speed[~ix_nan])

plt.savefig("hist.pdf")

# improved plot
plt.figure(figsize=(8,4))
speed = birddata.speed_2d[birddata.bird_name == 'Eric'] 
ix_nan = np.isnan(speed)
plt.hist(speed[~ix_nan], bins=np.linspace(0,30,20), normed=True)
plt.xlabel("2D speed (m/s)")
plt.ylabel("Frequency")
plt.savefig("hist.pdf")

# plotting a hist with pandas

import pandas as pd

# plot as a method of a datafram instance
# plenty of other keyword args for this ;ike range etc
# PANDAS DEALS WITH THe NANs for us !!!
birddata.speed_2d.plot(kind='hist', range=[0, 30])
<matplotlib.axes._subplots.AxesSubplot at 0x106666a58>

plt.xlabel("2D speed")
Text(0.5,0,'2D speed')

plt.savefig("pd_hist.pdf")

plt.show()

# 4.2.4 using datetime (and timestamps)
birddata.columns

# Index(['altitude', 'date_time', 'device_info_serial', 'direction', 'latitude',
#       'longitude', 'speed_2d', 'bird_name'],
#      dtype='object')

# these are strings that need to be converted to dattetime objs

import datetime

datetime.datetime.today()
datetime.datetime(2018, 10, 19, 0, 22, 34, 362086)

t1 = datetime.datetime.today()

t2 = datetime.datetime.today()

t2 - t1
datetime.timedelta(0, 7, 303466)

t2 = datetime.datetime.today()

t2 - t1
datetime.timedelta(0, 41, 452341)

# the timedelta obj format is mins, seconds and ?? 41 seconds elapsed

help(datetime.timedelta)


# actually apparently they are days seconds and microseconds....

# microsecond is a millionth of a second so 999999 is max for this field

# to convert our birddata timestamp into a datetime need to decipher it


In [46]: birddata.date_time[0:3]
Out[46]:
0    2013-08-15 00:18:08+00
1    2013-08-15 00:48:07+00
2    2013-08-15 01:17:58+00
Name: date_time, dtype: object

# there is a date, hoyrs:minutes:seconds and an offset in utc which is hours and in this case always 0.
In [48]: date_string = birddata.date_time[0]

In [49]: type(date_string)
Out[49]: str

In [50]: date_string
Out[50]: '2013-08-15 00:18:08+00'

In [51]: date_string[:-3]
Out[51]: '2013-08-15 00:18:08'

In [52]: # removes last 3 chars which are the +00 offset
# can use a strptime fn to extract the data from the string:
In [56]: datetime.datetime.strptime(date_string[:-3], "%Y-%m-%d %H:%M:%S")
Out[56]: datetime.datetime(2013, 8, 15, 0, 18, 8)

# do this for all the data
In [58]: timestamps = []

In [59]: for k in range(len(birddata)):
    ...:     timestamps.append(datetime.datetime.strptime(birddata.date_time.ilo
    ...: c[k][:-3], "%Y-%m-%d %H:%M:%S"))
    ...:

In [60]: timestamps[0:3]
Out[60]:
[datetime.datetime(2013, 8, 15, 0, 18, 8),
 datetime.datetime(2013, 8, 15, 0, 48, 7),
 datetime.datetime(2013, 8, 15, 1, 17, 58)]

# construct a pandas series odject of these so that they can de appended to the dataframe

# can use the timestapms list that I just made
In [61]: birddata["timestamp"] = pd.Series(timestamps, index = birddata.index)

In [62]: birddata.head()
Out[62]:
   altitude         ...                   timestamp
0        71         ...         2013-08-15 00:18:08
1        68         ...         2013-08-15 00:48:07
2        68         ...         2013-08-15 01:17:58
3        73         ...         2013-08-15 01:47:51
4        69         ...         2013-08-15 02:17:42

[5 rows x 9 columns]

# can see we are getting data but can we get a timedelta object?

In [63]: birddata.timestamp[4] - birddata.timestamp[3]

Out[63]: Timedelta('0 days 00:29:51')

# how much time elapsed since start of data collection?
In [64]: times = birddata.timestamp[birddata.bird_name == 'Eric']

In [65]: elapsed_time = [time - times[0] for time in times]

# so entry 0 is obvs 0 time since beginning... but then it accumulates so now can have a time axis if we want
In [67]: elapsed_time[0:5]
Out[67]:
[Timedelta('0 days 00:00:00'),
 Timedelta('0 days 00:29:59'),
 Timedelta('0 days 00:59:50'),
 Timedelta('0 days 01:29:43'),
 Timedelta('0 days 01:59:34')]

In [68]: elapsed_time[1000]
Out[68]: Timedelta('12 days 02:02:00')

# convert this to simpler units ie hours
# do this by dividing by a timedelta obj such as hours or days
In [68]: elapsed_time[1000]
Out[68]: Timedelta('12 days 02:02:00')

In [69]: elapsed_time[1000] / datetime.timedelta(days=1)
Out[69]: 12.084722222222222

In [70]: elapsed_time[1000] / datetime.timedelta(hours=1)
Out[70]: 290.03333333333336


# now we can plot say observations with tome to see if the observations were regularly spaced in time:

In [71]: plt.plot(np.array(elapsed_time) / datetime.timedelta(days=1))
Out[71]: [<matplotlib.lines.Line2D at 0x10670aac8>]

In [72]: plt.xlabel("Observation")
Out[72]: Text(0.5,0,'Observation')

In [73]: plt.ylabel("Elapsed time (days)")
Out[73]: Text(0,0.5,'Elapsed time (days)')

In [74]: # note syntax for plot is like a division - like how we calculated it

In [75]: plt.savefig("timeplot.pdf")

In [76]: plt.show()

# its nearly a straight line - the bumps mean that not all observations were completely evenly spaced but almost

##########
# calculating daily mean speed

# we wannt mean daily speed on y and time day on x axis
# this means that we want to take the first few observations and as soon as we hit day 1, compute the mean speed for the previous observations (so day 0) and so on

# so basically we aggregate the indicies for each day
# we start at day 0 and the next day is day 1...

# for each observation we will want to check, is it the next day yet?

# for each observation put it in a list, say called inds, basically collecting all the indicies so far until you hit day 1

# when you hit day one, calculate the mean of the velocity for the observations in indices, save that in a new list say daily mean speed and then increment next day by 1 and start indicies again

# we will use enumerate so that we can have both the index of the observation (from enumerate) AND the sctual value which in this case is the time

# remember that enumerate gives a tuple in this case it will be index and time

In [84]: eric_data = birddata[birddata.bird_name == 'Eric']

In [85]: time = eric_data.timestamp

In [86]: elapsed_time = [time - times[0] for time in times]

In [87]: elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)

In [88]: next_day = 1

In [89]: inds = []

In [90]: daily_mean_speed = []

In [91]: for (i, t) in enumerate(elapsed_days):
    ...:     if t < next_day:
    ...:         inds.append(i)
    ...:     else:
    ...:         # compute mean speed
    ...:         dd = np.mean(eric_data.speed_2d[inds])
    ...:         daily_mean_speed.append(dd)
    ...:         next_day += 1
    ...:         inds = []


# looking at the 2 periods when he flies substantially more than 2 m/s on average a day we can estimate when he does his migration.

# NOW we want to see where he actually migrates to

# questions: Sanne's flight times:

 In [98]: sanne_data = birddata[birddata.bird_name == "Sanne"]

In [99]: sanne_data.head()
Out[99]:
       altitude         ...                   timestamp
40916        55         ...         2013-08-15 00:01:08
40917        54         ...         2013-08-15 00:31:00
40918        55         ...         2013-08-15 01:01:19
40919        56         ...         2013-08-15 01:31:38
40920        55         ...         2013-08-15 02:01:24

[5 rows x 9 columns] 


#############
# 4.2.6 cartopy library
# lib for maps etc that you can import prjections from etc

# we will be using a standard projection for long lat data called mercator
In [101]: import cartopy.crs as ccrs

In [102]: import cartopy.feature as cfeature

# This is a standard projection from the cartopy library

In [103]: proj = ccrs.Mercator()

# next loop over all birds and plot their trajectories but with mercator applied

# remember this is how we seperated the birdname column into the three unique names

bird_names = pd.unique(birddata.bird_name)

plt.figure(figsize=(10,10))
# Axes normally found by trial and error but given in this lecture
ax = plt.axes(projection = proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
# adding features to the plot:
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
for name in bird_names:
  ix = birddata['bird_name'] == name
  x, y = birddata.longitude[ix], birddata.latitude[ix]
  ax.plot(x, y, '_', transform=ccrs.Geodetic(), label=name)

plt.legend(loc = "upper left")
plt.savefig("map.pdf")

