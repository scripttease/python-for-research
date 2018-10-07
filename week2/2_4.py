# 2.4.1 questions (randomness)

# Use random.choice and range to generate a random integer from 0-9.

random.choice(range(0,10))

#What will random.choice(list([1,2,3,4])) produce?
# A value from 1-4 , selected at random. 


#Which of the following lines of code takes the sum of 10 random integers between 0 and 9?
sum(random.choice(range(10)) for i in range(10)) 
In [2]: import random

In [3]: x = random.sample(range(10),10)

In [4]: x
Out[4]: [0, 1, 3, 7, 2, 9, 6, 4, 8, 5]

In [5]: sum(x)
Out[5]: 45


In [22]: random.choice([1,2,3,4,5,6])
Out[22]: 1

In [23]: random.choice([1,2,3,4,5,6])
Out[23]: 6

In [24]: map(list(range(0,100)), random.choice([1,2,3,4,5,6]))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-24-6288aa9e736b> in <module>()
----> 1 map(list(range(0,100)), random.choice([1,2,3,4,5,6]))

TypeError: 'int' object is not iterable

In [25]: for i in range(100):
    ...:     random.choice([1,2,3,4,5,6])
    ...:

In [26]: rolls = []

In [27]: for i in range(100):
    ...:     rolls.append(random.choice([1,2,3,4,5,6]))
    ...:
    ...:

In [8]: plt.hist(rolls, bins=np.linspace(0.5,6.6,7))
Out[8]:
(array([15., 14., 11., 18., 18., 24.]),
 array([0.5       , 1.51666667, 2.53333333, 3.55      , 4.56666667,
        5.58333333, 6.6       ]),
 <a list of 6 Patch objects>)

In [9]: plt.show()

In [10]: for i in range(10000):
    ...:     rolls.append(random.choice([1,2,3,4,5,6]))
    ...:
    ...:

In [11]: plt.hist(rolls, bins=np.linspace(0.5,6.6,7))
Out[11]:
(array([1743., 1659., 1650., 1709., 1623., 1716.]),
 array([0.5       , 1.51666667, 2.53333333, 3.55      , 4.56666667,
        5.58333333, 6.6       ]),
 <a list of 6 Patch objects>)

In [12]: plt.show()


#2.4.2
In [12]: plt.show()

In [13]: y = 0

In [14]: ys = []

In [15]: for i in range(100):
    ...:     y=0
    ...:     for j in range(10):
    ...:         x=random.choice([1,2,3,4,5,6])
    ...:         y = y + x
    ...:     ys.append(y)
    ...:
In [18]: m = min(ys)

In [19]: m
Out[19]: 24

In [20]: x= max(ys)

In [21]: x
Out[21]: 47

In [22]: plt.hist(ys)
Out[22]:
(array([ 5.,  6.,  8., 24., 14., 13., 17.,  6.,  4.,  3.]),
 array([24. , 26.3, 28.6, 30.9, 33.2, 35.5, 37.8, 40.1, 42.4, 44.7, 47. ]),
 <a list of 10 Patch objects>)

In [23]: plt.show()

In [24]: for i in range(10000):
    ...:     y=0
    ...:     for j in range(10):
    ...:         x=random.choice([1,2,3,4,5,6])
    ...:         y = y + x
    ...:     ys.append(y)
    ...:

In [25]: plt.hist(ys)
Out[25]:
(array([  19.,  148.,  691., 1757., 2798., 2638., 1469.,  481.,   88.,
          11.]),
 array([16. , 19.9, 23.8, 27.7, 31.6, 35.5, 39.4, 43.3, 47.2, 51.1, 55. ]),
 <a list of 10 Patch objects>)

In [26]: plt.show()

In [27]: min(ys)
Out[27]: 16

In [28]: max(ys)
Out[28]: 55

#2.4.3
In [32]: np.random.random()
Out[32]: 0.5454664698008773

In [33]: np.random.random(3)
Out[33]: array([0.14140375, 0.33329187, 0.77548808])

In [34]: np.random.random(5)
Out[34]: array([0.95601658, 0.00375417, 0.44060041, 0.55723138, 0.02247995])

In [35]: np.random.random(2,3)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-35-80b6e3664a11> in <module>()
----> 1 np.random.random(2,3)

mtrand.pyx in mtrand.RandomState.random_sample()

TypeError: random_sample() takes at most 1 positional argument (2 given)

In [36]: np.random.random((2,3))
Out[36]:
array([[0.90542318, 0.85158732, 0.43471993],
       [0.83489674, 0.44777654, 0.55901918]])

In [37]: np.random.normal(0,1)
Out[37]: -0.467040858045274

In [38]: np.random.normal(0,1, 5)
Out[38]: array([-1.24915861,  0.37485433,  0.70411747, -1.13294324,  1.09077421])

In [39]: np.random.normal(0,1, (2,5))
Out[39]:
array([[-1.23349885, -0.93796832, -0.45626195,  0.48434507,  0.15696503],
       [-0.05200166,  1.86597417,  0.89629689, -0.41034165,  0.12849763]])

In [40]: x = np.random.randint(1,7,(10,3))

In [41]: x
Out[41]:
array([[5, 6, 6],
       [3, 4, 6],
       [4, 1, 4],
       [5, 3, 3],
       [4, 6, 1],
       [4, 2, 4],
       [4, 4, 6],
       [5, 3, 2],
       [2, 2, 1],
       [5, 2, 2]])

In [42]: np.sum(x)
Out[42]: 109

In [43]: np.sum(x, axis=0)
Out[43]: array([41, 33, 35])

In [44]: np.sum(x, axis=1)
Out[44]: array([17, 13,  9, 11, 11, 10, 14, 10,  5,  9])

In [45]: X = np.random.randint(1,7,(100,10))

In [46]: Y = np.sum(X, axis=1)

In [47]: plt.hist(Y)
Out[47]:
(array([ 4.,  2., 10., 18.,  9., 28., 14., 11.,  2.,  2.]),
 array([21. , 23.8, 26.6, 29.4, 32.2, 35. , 37.8, 40.6, 43.4, 46.2, 49. ]),
 <a list of 10 Patch objects>)

In [48]: plt.show()

In [49]: X = np.random.randint(1,7,(10000,10))

In [50]: Y = np.sum(X, axis=1)

In [51]: plt.hist(Y)
Out[51]:
(array([  36.,  216.,  879., 1464., 2725., 2650., 1248.,  620.,  145.,
          17.]),
 array([17. , 20.7, 24.4, 28.1, 31.8, 35.5, 39.2, 42.9, 46.6, 50.3, 54. ]),
 <a list of 10 Patch objects>)

In [52]: plt.show()

In [53]:

In [58]: numpy.sum(numpy.random.randint(1,7,(100,10)), axis=0)
Out[58]: array([349, 361, 336, 359, 391, 356, 333, 355, 375, 362])

#2.4.4 time
In [59]: import time

In [60]: time.clock()
Out[60]: 7.461823

In [61]: start = time.clock()

In [62]: end = time.clock()

In [63]: end - start
Out[63]: 0.09001400000000004
In [65]: start = time.clock()
    ...: ys=[]
    ...: for rep in range(1000000):
    ...:     y=0
    ...:     for k in range(10):
    ...:         x=random.choice([1,2,3,4,5,6])
    ...:         y = y + x
    ...:     ys.append(y)
    ...: end = time.clock()
    ...: print(end-start)
    ...:
    ...:
12.253754

In [66]: start = time.clock()
    ...: X = np.random.randint(1,7,(1000000,10))
    ...: Y = np.sum(X, axis=1)
    ...: end = time.clock()
    ...: print(end-start)
    ...:
    ...:
0.18728599999999673

In [67]: 12.253754/0.18728599999999673
Out[67]: 65.42802985807917

# the numpy way is 65 times faster
