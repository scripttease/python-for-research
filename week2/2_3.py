#2.3.1
import matplotlib.pyplot as plt
import numpy as np
plt.plot([0,1,4,7])
plt.show()
help(np.linspace)
In [10]: vector_x = np.linspace(0,10,10)

In [11]: vector_x = y**2
In [13]: vector_y = vector_x**2

In [14]: plt.plot(vector_x, vector_y)
Out[14]: [<matplotlib.lines.Line2D at 0x11543b9e8>]

In [15]: plt.show()

# kw args for what the plot looks like

In [16]: plt.plot(vector_x, vector_y, 'bo-', linewidth=2, markersize=12)
Out[16]: [<matplotlib.lines.Line2D at 0x1165b7518>]

In [17]: plt.show()
#2.3.2
In [25]: plt.plot(vector_x, vector_y, 'bo-', linewidth=2, markersize=12)
Out[25]: [<matplotlib.lines.Line2D at 0x11674aa90>]

In [26]: plt.xlabel("y")
Out[26]: Text(0.5,0,'y')

In [27]: plt.xlabel("x")
Out[27]: Text(0.5,0,'x')

In [28]: plt.ylabel("y")
Out[28]: Text(0,0.5,'y')

In [29]: plt.axis([-0.5,10.5, -0.5,20])
# nb doing plt.show() prints plot thus far but then goes back to nothing so enter all details before doing show
In [34]: vector_y2 = vector_x**1.5

In [35]: plt.plot(vector_x, vector_y, 'bo-', linewidth=2, markersize=12)
Out[35]: [<matplotlib.lines.Line2D at 0x116800898>]

In [36]: plt.plot(vector_x, vector_y2, 'gs-', linewidth=2, markersize=12)
Out[36]: [<matplotlib.lines.Line2D at 0x116807278>]

In [37]: plt.plot(vector_x, vector_y, 'bo-', linewidth=2, markersize=12, label='
    ...: first')
Out[37]: [<matplotlib.lines.Line2D at 0x1168128d0>]

In [38]: plt.plot(vector_x, vector_y2, 'gs-', linewidth=2, markersize=12, label=
    ...: 'second')
Out[38]: [<matplotlib.lines.Line2D at 0x1168078d0>]

In [40]: plt.axis([-0.5,10.5, -0.5,105])
Out[40]: [-0.5, 10.5, -0.5, 105]

In [41]: plt.ylabel("y")
Out[41]: Text(0,0.5,'y')

In [42]: plt.xlabel("x")
Out[42]: Text(0.5,0,'x')

In [43]: plt.legend(loc='upper left')
Out[43]: <matplotlib.legend.Legend at 0x116807b00>

In [44]: plt.savefig('myplot.pdf')

In [45]: plt.show()
# 2.3.3
In [46]: x = np.logspace(-1,1, 40)

In [47]: y1 = x**2.0

In [48]: y2 = x**1.5

In [49]: plt.loglog(x, y1, "bo-", linewidth=2, markersize=12, label='first')
Out[49]: [<matplotlib.lines.Line2D at 0x1168fd9b0>]

In [50]: plt.loglog(x, y2, "gs-", linewidth=2, markersize=12, label='second')
Out[50]: [<matplotlib.lines.Line2D at 0x1168f7ba8>]

In [51]: plt.xlabel("x")
Out[51]: Text(0.5,0,'x')

In [52]: plt.ylabel("y")
Out[52]: Text(0,0.5,'y')

In [53]: plt.axis([-0.5,10.5,-5,105])
/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py:3129: UserWarning: Attempted to set non-positive xlimits for log-scale axis; invalid limits will be ignored.
  'Attempted to set non-positive xlimits for log-scale axis; '
/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py:3449: UserWarning: Attempted to set non-positive ylimits for log-scale axis; invalid limits will be ignored.
  'Attempted to set non-positive ylimits for log-scale axis; '
Out[53]: [-0.5, 10.5, -5, 105]

In [54]: plt.legend(loc='upper left')
Out[54]: <matplotlib.legend.Legend at 0x1168f7080>

In [56]: plt.savefig('myplotlog.pdf')

In [57]: plt.show()
# 2.3.4 histograms and subplots

In [58]: x = np.logspace(0,1,10)

In [59]: y = x**2

In [60]: plt.loglog(x,y,"bo-")
Out[60]: [<matplotlib.lines.Line2D at 0x11671b5f8>]

In [61]: plt.show()

In [63]: import random

In [64]: x = np.random.normal(size=1000)

In [65]: plt.hist(x);

In [66]: plt.show()

In [67]: plt.hist(x, normed=True)

In [68]: plt.show()


In [70]: plt.hist(x, bins=np.linspace(-5,5,21))

In [71]: plt.show()

In [72]: x = np.random.gamma(2,3,100000)

In [92]: plt.figure()
Out[92]: <Figure size 640x480 with 0 Axes>

In [93]: plt.subplot(221)

In [94]: plt.hist(x, bins =30)
In [95]: plt.subplot(222)

In [96]: plt.hist(x, bins =30, normed = True)
In [97]: plt.subplot(223)

In [98]: plt.hist(x, bins =30, normed = True, cumulative=True)
In [99]: plt.subplot(224)

In [100]: plt.hist(x, bins =30, normed = True, cumulative=True, histtype='step')
In [101]: plt.savefig('myplotsubplot.pdf')

In [102]: plt.show()
