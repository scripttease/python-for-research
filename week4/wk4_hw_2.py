# Case study 5, wk 4 hw 2

# Exercise 1
# In this case study, we will continue taking a look at patterns of flight for each of the three birds in our dataset. We will group the flight patterns by bird and date, and plot the mean altitude for these groupings.

# pandas makes it easy to perform basic operations on groups within a dataframe without needing to loop through each value in the dataframe. In this exercise, we will group the dataframe by birdname and then find the average speed_2d for each bird.

# Fill in the code to find the mean altitudes of each bird.

# Provided code

# First, use `groupby()` to group the data by "bird_name".
grouped_birds =

# Now calculate the mean of `speed_2d` using the `mean()` function.
mean_speeds = 

# Use the `head()` method prints the first 5 lines of each bird.


# Find the mean `altitude` for each bird.
mean_altitudes = 
# My submission (incorrect)

# First, use `groupby()` to group the data by "bird_name".

grouped_birds = birddata.groupby("bird_name")
print(grouped_birds)
# Now calculate the mean of `speed_2d` using the `mean()` function.
mean_speeds = grouped_birds["speed_2d"].mean()
#print(mean_speeds)

# Use the `head()` method prints the first 5 lines of each bird.
for name in grouped_birds:
    print(name[1].head())

# Find the mean `altitude` for each bird.
mean_altitudes = grouped_birds["altitude"].mean()
#print(mean_altitudes)

# First, use `groupby()` to group the data by "bird_name".

grouped_birds = birddata.groupby("bird_name")
#print(grouped_birds)
# Now calculate the mean of `speed_2d` using the `mean()` function.
#mean_speeds = grouped_birds["speed_2d"].mean()

for name in grouped_birds:
    mean_speeds = name[1]["speed_2d"].mean()
    print(mean_speeds)

# Use the `head()` method prints the first 5 lines of each bird.
for name in grouped_birds:
    print(name[0], name[1].head())


# Find the mean `altitude` for each bird.
for name in grouped_birds:
    mean_altitudes = name[1]["altitude"].mean()
    print(mean_altitudes)


# This defines mean altitudes as a dict

# First, use `groupby()` to group the data by "bird_name".
bird_names = pd.unique(birddata.bird_name)
grouped_birds = birddata.groupby("bird_name")

# Use the `head()` method prints the first 5 lines of each bird.
print(grouped_birds.head())

# Now calculate the mean of `speed_2d` using the `mean()` function.
mean_speeds = {}
for name in bird_names:
    inds = birddata.bird_name == name
    mean_speed = birddata.speed_2d[inds].mean()
    mean_speeds[name] = mean_speed
print(mean_speeds)
   

# Find the mean `altitude` for each bird.
mean_altitudes = {}
for name in bird_names:
    inds = birddata.bird_name == name
    mean_alt = birddata.altitude[inds].mean()
    mean_altitudes[name] = mean_alt
print(mean_altitudes)


# I think actually it wants me to use pandas to calculate this not python

# First, use `groupby()` to group the data by "bird_name".
bird_names = pd.unique(birddata.bird_name)
grouped_birds = birddata.groupby("bird_name")

# Use the `head()` method prints the first 5 lines of each bird.
print(grouped_birds.head())

# Now calculate the mean of `speed_2d` using the `mean()` function.
mean_speeds = grouped_birds['speed_2d'].agg(np.mean)
print(mean_speeds)
   

# Find the mean `altitude` for each bird.
mean_altitudes = grouped_birds['altitude'].agg(np.mean)
print(mean_altitudes)


# Exercise 2
# In this case study, we will continue taking a look at patterns of flight for each of the three birds in our dataset. We will group the flight patterns by bird and date, and plot the mean altitude for these groupings.

# In this exercise, we will group the flight times by date and calculate the mean altitude within that day.

# Convert birddata.date_time to the pd.datetime format, and store as birddata["date"].
# Fill in the code to find the mean altitudes for each day.

# Given code

# Convert birddata.date_time to the `pd.datetime` format.
birddata.date_time = 

# Create a new column of day of observation
birddata["date"] = 

# Check the head of the column.


# Use `groupby()` to group the data by date.
grouped_bydates = 

# Find the mean `altitude` for each date.
mean_altitudes_perday =

# submitted code

    # Convert birddata.date_time to the `pd.datetime` format.
import datetime
timestamps = []
for i in range(len(birddata)):
        timestamps.append(datetime.datetime.strptime(birddata.date_time.iloc[i][:-3], "%Y-%m-%d %H:%M:%S"))
    #print(birddata.date_time.head())
    #print(timestamps[0:3])
    
birddata.date_time = pd.Series(timestamps, index = birddata.index)
    
    # Create a new column of day of observation
birddata["date"] = birddata.date_time.dt.date
    
birddata.date.head()
    
    # Check the head of the column.
    
    
    # Use `groupby()` to group the data by date.
   
    #unique-dates = pd.unique(birddata.dates)
grouped_bydates = birddata.groupby('date')
    
    # Find the mean `altitude` for each date.
mean_altitudes_perday = grouped_bydates['altitude'].agg(np.mean)
#print(mean_altitudes_perday)

# Exercise 3
# In this case study, we will continue taking a look at patterns of flight for each of the three birds in our dataset. We will group the flight patterns by bird and date, and plot the mean altitude for these groupings.

# In this exercise, we will group the flight times by both bird and date, and calculate the mean altitude for each.

# birddata already contains the date column. To find the average speed for each bird and day, create a new grouped dataframe called grouped_birdday that groups the data by both bird_name and date.

# Provided code:
# Use `groupby()` to group the data by bird and date.
# grouped_birdday = 

# Find the mean `altitude` for each bird and date.
# mean_altitudes_perday =

# look at the head of `mean_altitudes_perday`.

# Answer
# Use `groupby()` to group the data by bird and date.
grouped_birdday = birddata.groupby(['bird_name', 'date'])

# Find the mean `altitude` for each bird and date.
mean_altitudes_perday = grouped_birdday['altitude'].agg(np.mean)

# look at the head of `mean_altitudes_perday`.
mean_altitudes_perday.head()

# Exercise 4

# Great! Now find the average speed for each bird and day.
# Store these are three pandas Series objects – one for each bird.
# Use the plotting code provided to plot the average speeds for each bird.

# eric_daily_speed  = # Enter your code here.
# sanne_daily_speed = # Enter your code here.
# nico_daily_speed  = # Enter your code here.
# 
# eric_daily_speed.plot(label="Eric")
# sanne_daily_speed.plot(label="Sanne")
# nico_daily_speed.plot(label="Nico")
# plt.legend(loc="upper left")
# plt.show()

# Answer:

eric_data = birddata[birddata.bird_name == 'Eric']
grouped_eric_day = eric_data.groupby('date')
eric_daily_speed  = grouped_eric_day['speed_2d'].agg(np.mean)
#eric_daily_speed.head()
sanne_daily_speed = birddata[birddata.bird_name == 'Sanne'].groupby('date')['speed_2d'].agg(np.mean)
#sanne_daily_speed.head()
nico_daily_speed  = birddata[birddata.bird_name == 'Nico'].groupby('date')['speed_2d'].agg(np.mean)
nico_daily_speed.head()


eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.show()

