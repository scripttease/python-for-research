# 3.3.2 distanve between 2 points using rowvectors in numpy

import numpy as np

p1 = np.array([1,1])
p2 = np.array([4,4])

p2 - p1
# x1-x2 and y1 - y2
array([3,3])

# x1-x2 and y1 - y2 squared (to power 2)
np.power(p2 -p1, 2)
array([9,9])
# this is the square of the differences between the two points

# this is the sum of the square of the distances:
np.sum(np.array([9,9]))

# sqrt:
np.sqrt(np.sum(np.power(p2- p1, 2)))
# out 4.24264...

# As a function

def distance(p1, p2):
  """Find the distance beteen ponts p1 and p2 """
  import numpy as np
  return np.sqrt(np.sum(np.power(p2 -p1, 2)))
    	
# A majority vote fn starting from a basis of the slow count words fn

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

def majority_vote(votes):
  vote_counts = {}
  for vote in votes:
    if vote in vote_counts:
      vote_counts[vote] += 1
    else:
      vote_counts[vote] = 1
  return vote_counts 

votes = [1,2,3,2,3,1,2,1,2,3,3,2,1,2,3,3,3,2,333,3,1,1,2,3,1]

vote_counts = majority_vote(votes)
# Out[334]: {1: 7, 2: 8, 3: 9, 333: 1}
# and so if we want the max:

max(vote_counts)
# same as 
max(vote_counts.keys())

# max actual counts
max_count = max(vote_counts.values())

# NEITHER of these help us. we want to know that 3 (which has the max number of counts, being 9) is the majority vote...

# for this we need the items method, which returns a dict-item object that looks like a list of tuples containing keys and values of the dict. Eg {dict}.items() -> [(k,v), (k,v), ... (k,v)]

winners = []
max_count = max(vote_counts.values())
for vote, count in vote_counts.items():
  if count == max_count:
    winners.append(vote)

# winners now returns 3 as desired
# nb note that if there are 2 or more 'winners' we can just pick one at random for the sake of kNN. So now the fn becomes:

import random

def majority_vote(votes):
  """ return most common element in votes OR select one of most common at random if tie """
  vote_counts = {}
  for vote in votes:
    if vote in vote_counts:
      vote_counts[vote] += 1
    else:
      vote_counts[vote] = 1

  winners = []
  max_count = max(vote_counts.values())
  for vote, count in vote_counts.items():
    if count == max_count:
      winners.append(vote)

  return random.choice(winners)

# In [350]: votes = [3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7,7,7,7,7,7,7,7,7,7,7
#      ...: ,7,7,7,7,8,12,25]

# In [351]: majority_vote(votes)
# Out[351]: 4

# In [352]: majority_vote(votes)
# Out[352]: 7

# In [353]: majority_vote(votes)
# Out[353]: 7

# In [354]: majority_vote(votes)
# Out[354]: 4

import scipy.stats as ss

def majority_vote_fast(votes):
  """ return first most common element in votes """
  mode, count = ss.mstats.mode(votes)
  return mode

# The problem with this function is that it ALWAYS retuns the first mode, in this case 4 - so you may find that results can be skewed over a large data set when using this

# 3.3.4 psudocode for kNN

# Loop over all exisiting points p 
  # compute disnatce btween new point np and each p
# sort these and return the k nearest (shortest distances) to np

# test data:
points = np.array([[1,1], [1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])

p = np.array([2.5, 2])

# visualise data for points with xcoords being column 0 and y coords being col 1 of each point. these will be red circles and our new point p will be blue

import matplotlib.pyplot as plt

plt.plot(points[:,0], points[:,1], 'ro')
plt.plot(p[0], p[1], 'bo')
plt.show()

# make an empty array that will hold our distances - note that it must be the same shape as a col in points so:

distances = np.zeros(points.shape[0])
for i in range(len(distances)):
  distances[i] = distance(p, points[i])

# does it work? we know that in our points array the two closest points are [2,2] and [3,2]
#they correspond to points[4] and points[7]:

# In [377]: points[4] , points[7]
# Out[377]: (array([2, 2]), array([3, 2]))

# yes it is correct:
# In [378]: distances[4], distances[7]
# Out[378]: (0.5, 0.5)

# we could sort the distances to give us the shortest ones first or last BUT what would be better is an index vector that will sort the array, thus knowing the the first k of the points would be our first k nearest neighbors.

# in numpy this is aclled argsort
ind = np.argsort(distances)
# in [381]: ind
# Out[381]: array([4, 7, 3, 5, 6, 8, 1, 0, 2])
#It has put arguments 4 and 7 at the beginning of the list as we wanted

# so now we can do:
distances[ind]
#Out[382]:
# array([0.5       , 0.5       , 1.11803399, 1.11803399, 1.11803399,
       # 1.11803399, 1.5       , 1.80277564, 1.80277564])

# first 2:
distances[ind[0:2]]

# turn into a function:

def find_nearest_neighbors(p, points, k=5):
  """ find and return indicies of k points nearest to p  """
  distances = np.zeros(points.shape[0])
  for i in range(len(distances)):
    distances[i] = distance(p, points[i])
  ind = np.argsort(distances)
  return ind[0:k] # same as ind[:k]

# example

ind = find_nearest_neighbors(p, points, 2); print(points[ind])
#[[2 2]
# [3 2]]
  
# knn and category psudocode
# categorys or outcomes for our array:
points = np.array([[1,1], [1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])

p = np.array([2.5, 2])

outcomes = np.array([0,0,0,0,1,1,1,1,1])

def knn_predict(p, points, outcomes, k=5):
  # find nearest neighbors
  ind = find_nearest_neighbors(p, points, k)
  # predict class of p based on majority vote:
  return majority_vote(outcomes[ind])

knn_predict(np.array([2.5,2.7]), points, outcomes, k=2)
# output =1
# generate synthetic data (bivariate meaning variable x and y, so 2 variables) using ipstats module

# this set is taking 5 rows and 2 cols at random from a normal dist with mean 0 sd 1

ss.norm(0,1).rvs((5,2))

#now same but mean = 0

ss.norm(1,1).rvs((5,2))

# concat these on axis 0 (rows) giving 10 rows and 2 cols

np.concatenate((ss.norm(0,1).rvs((5,2)), ss.norm(1,1).rvs((5,2))), axis=0)

# fn for generating synthetic data points, x,y with  outcomes either 0 or 1 (here we give the first n points outcome 0 and the second n points putcome 1)

# can gen an array using repeat, first arg is your val and second in n times to repeat:
n = 5
np.repeat(0, n)

# gen (default will be 100 points as n = 50) synthetic xy points with putcomes 0 or 1)

def generate_synthetic_data(n=50):
  """ create 2 sets of points from bivariate normal dist with outcomes 1 or 0"""
  points = np.concatenate((ss.norm(0,1).rvs((n,2)), ss.norm(1,1).rvs((n,2))), axis=0)
  outcomes = np.concatenate((np.repeat(0,n), np.repeat(1,n)))
  return (points, outcomes)

n=20
(points, outcomes) = generate_synthetic_data(n)
plt.figure()
plt.plot(points[:n,0], points[:n,1], 'ro')
plt.plot(points[n:,0], points[n:,1], 'bo')
plt.savefig("bivariate_data.pdf")
plt.show()

# 3.3.6 making a prediction grid

# takes a tuple that corresponds to x min xmax, ymin and ymax

(points, outcomes) = generate_synthetic_data(n)
# nb predictors == points

def make_prediction_grid(predictors, outcomes, limits, h, k):
  """ classify each point on the prediction grid """
  # unpack tuple:
  (x_min, x_max, y_min, y_max) = limits
  xs = np.arange(x_min, x_max, h)
  ys = np.arange(y_min, y_max, h)
  xx, yy = np.meshgrid(xs, ys)

  # can specify datatype as we know its 0 or 1
  prediction_grid = np.zeros(xx.shape, dtype = int)
  for i,x in enumerate(xs):
    for j,y in enumerate(ys):
      p = np.array([x,y])
      prediction_grid[j,i] = knn_predict(p, predictors, outcomes, k)

  return(xx, yy, prediction_grid)

(points, outcomes) = generate_synthetic_data(n)
limits = (0,5,0,6)
h = 1
k = 5
(xx, yy, prediction_grid) = make_prediction_grid(points, outcomes, limits, h, k)
# examples of meshgrid

# x_min = 0

# In [412]: x_max = 5

# In [413]: h = 1

# In [414]: xs = np.arange(x_min, x_max, h)
#      ...:

xs = array([0, 1, 2, 3, 4])

ys = np.arange(0,6,1)

# In [417]: ys
# Out[417]: array([0, 1, 2, 3, 4, 5])

np.meshgrid(xs,ys)
# Out[418]:
# [array([[0, 1, 2, 3, 4],
#         [0, 1, 2, 3, 4],
#         [0, 1, 2, 3, 4],
#         [0, 1, 2, 3, 4],
#         [0, 1, 2, 3, 4],
#         [0, 1, 2, 3, 4]]), array([[0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1],
#         [2, 2, 2, 2, 2],
#         [3, 3, 3, 3, 3],
#         [4, 4, 4, 4, 4],
#         [5, 5, 5, 5, 5]])]

xx, yy = np.meshgrid(xs,ys)

xx
# Out[420]:
# array([[0, 1, 2, 3, 4],
#        [0, 1, 2, 3, 4],
#        [0, 1, 2, 3, 4],
#        [0, 1, 2, 3, 4],
#        [0, 1, 2, 3, 4],
#        [0, 1, 2, 3, 4]])

yy
# Out[421]:
# array([[0, 0, 0, 0, 0],
#        [1, 1, 1, 1, 1],
#        [2, 2, 2, 2, 2],
#        [3, 3, 3, 3, 3],
#        [4, 4, 4, 4, 4],
#        [5, 5, 5, 5, 5]])

# examples of enumerate

seasons = ["spring", "summer", "autumn", "winter"]
list(enumerate(seasons))

# Out[428]: [(0, 'spring'), (1, 'summer'), (2, 'autumn'), (3, 'winter')]

# enumerate retirns a tuple with the index as the first value and the part of the original sequence as the second value

for ind, season in enumerate(seasons):
  print(ind, season)
# 0 spring
# 1 summer
# 2 autumn
# 3 winter

# 3.3.7 plot prediction grid

def plot_prediction_grid (xx, yy, prediction_grid, filename):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    plt.savefig(filename)
    plt.show()

(predictors, outcomes) = generate_synthetic_data()
limits = (0,5,0,6)
h = 1
k = 5
(xx, yy, prediction_grid) = make_prediction_grid(points, outcomes, limits, h, k)
plot_prediction_grid(xx, yy, prediction_grid, "predictionplot.pdf")

plt.show

### putting it all together
(predictors, outcomes) = generate_synthetic_data()

#k = 5
k=5
filename="knn_synth_5_2.pdf"
limits = (-3,4,-3,4)
h = 0.1
(xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k)
plot_prediction_grid(xx, yy, prediction_grid, filename)

#k = 50
k=50
filename="knn_synth_50_2.pdf"
limits = (-3,4,-3,4)
h = 0.1
(xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k)
plot_prediction_grid(xx, yy, prediction_grid, filename)

#3.3.8 applying knn
# import scikitlearn and then your datasets

from sklearn import datasets
iris = datasets.load_iris()
# examine the data:
iris["data"]
iris["target"]

# make a subset of the data (the first two columns which are sepal length and width, and all of the 150 rows) for the predictor:
predictors = iris.data[:, 0:2]
# use another part of data as outcomes
outcomes = iris.target

# plot all of the predictor data where outcome = 0:
plt.plot(predictors[outcomes==0][:,0], predictors[outcomes==0][:,1], "ro")
# plot all of the predictor data where outcome = 1
plt.plot(predictors[outcomes==1][:,0], predictors[outcomes==1][:,1], "go")
# plot all of the predictor data where outcome = 2
plt.plot(predictors[outcomes==2][:,0], predictors[outcomes==2][:,1], "bo")

# xy axis correspond to the value of predictors and colour corresponds to the outcome.
plt.figure()
plt.plot(predictors[outcomes==0][:,0], predictors[outcomes==0][:,1], "ro")
plt.plot(predictors[outcomes==1][:,0], predictors[outcomes==1][:,1], "go")
plt.plot(predictors[outcomes==2][:,0], predictors[outcomes==2][:,1], "bo")
plt.savefig("iris.pdf")

# make a prediction grid for iris data

k=5
filename="iris_grid.pdf"
limits = (4,8,1.5,4.5)
h = 0.1
(xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k)
plot_prediction_grid(xx, yy, prediction_grid, filename)

# comparing the knn method from scipy

# install sklearn first if necessary
from sklearn.neighbors import KNeighborsClassifier
# shorthand for knn with k=5
knn = KNeighborsClassifier(n_neighbors = 5)
#apply knn method
knn.fit(predictors, outcomes)
# predict outcomes
sk_predictions = knn.predict(predictors)

# make prediction data (ie generate outcomes) using my previously made fns.
my_predictions = np.array([knn_predict(p, predictors, outcomes, 5) for p in predictors])

# how do they compare?
sk_predictions == my_predictions
# returns T or F when the agree/disagree

np.mean( sk_predictions == my_predictions)*100
# 96% agreement

# how often do they agree with actual (known) outcomes?
np.mean( sk_predictions == outcomes)*100
np.mean( my_predictions == outcomes)*100

