
# 4.2.1 GPS tracking of birds
In [44]: import pandas as pd

In [45]: birddata = pd.read_csv("bird_tracking.csv")

# 4.2.2 simple data vis
# get indicies just for bird called eric
ix = birddata.bird_name == "Eric"

# get x and y data using the indicies that are erics
x, y = birddata.longitude[ix], birddata.latitude[ix]

# plot these:
plt.figure(figsize=(7,7))
# plot using blue dots "."
plt.plot(x,y,".")


