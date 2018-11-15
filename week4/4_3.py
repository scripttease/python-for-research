# 4.3
## 4.3.1 Intro to network analysis

import networkx as nx

# create an undirected graph

G = nx.Graph()

# add node:

G.add_node(1)

G.add_nodes_from([2,3])

G.add_nodes_from(['u','v'])

# view nodes
G.nodes()
NodeView((1, 2, 3, 'u', 'v'))

# adding edges takes 2 args, the nodes

G.add_edge(1,2)

G.add_edge('u','v')

# you can add edges from nodes that dont exist - Networkx adds those nodes

G.add_edges_from([(1,3),(1,4),(1,5),(1,6)])

G.add_edge('u','w')

G.edges()
EdgeView([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), ('u', 'v'), ('u', 'w')])

# removing nodes

G.remove_node(2)

G.nodes()
NodeView((1, 3, 'u', 'v', 4, 5, 6, 'w'))

G.remove_nodes_from([4,5])

G.nodes()
NodeView((1, 3, 'u', 'v', 6, 'w'))

# removing edges

G.remove_edge(1,3)

G.edges()
EdgeView([(1, 6), ('u', 'v'), ('u', 'w')])

G.remove_edges_from([(1,2), ('u','v')])

G.edges()
EdgeView([(1, 6), ('u', 'w')])

G.nodes()
NodeView((1, 3, 'u', 'v', 6, 'w'))

# get number of nodes or edges

G.number_of_nodes()
6

G.number_of_edges()
2

## 4.3.3 Graph Visualistaion with NetworkX
## using a built in data set called Karate Club graph


G = nx.karate_club_graph()

# to visualise, import matplot

import matplotlib.pyplot as plt

nx.draw(G)

nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')

plt.show()

nx.show()
-----------------------------------------------------------------
rror                            Traceback (most recent call last)
nput-142-4f04236f4dc5> in <module>()
.show()

rror: module 'networkx' has no attribute 'show'

nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')

plt.savefig('karate_graph.pdf')

plt.show()

# Nx stores degrees of nodes in a dict where keys are node IDs and vals are degrees
G.degree()
DegreeView({0: 16, 1: 9, 2: 10, 3: 6, 4: 3, 5: 4, 6: 4, 7: 4, 8: 5, 9: 2, 10: 3, 11: 1, 12: 2, 13: 5, 14: 2, 15: 2, 16: 2, 17: 2, 18: 2, 19: 3, 20: 2, 21: 2, 22: 2, 23: 5, 24: 3, 25: 3, 26: 2, 27: 4, 28: 3, 29: 4, 30: 4, 31: 6, 32: 12, 33: 17})



# to find specific nodes degrees:

G.degree()[33]
17

# or using this notation where the arg is the node:

G.degree(33)
17

# note this fn degree is different and distinguished by the interpreter by the way it is called

# the first degree has no args, the second 1 ard

### 4.3.4 Random Graphs
# simplest random graph model for network is the Erdos-Renyi or the ER graph model

# there are two parameters for a random graph model, N and p.
# N is the number of nodes and p is the probability for any two nodes to be connected by an edge
# so to implement you would go through every possible pair of nodes and with probabiliyt p insert an edge between them.
# consider eaxh pair of nodes once, independently of any other pair and, for example, flip a coin to see if they are connected.
# If the value of p is small typical graphs tend to be sparse having few edges
# large values of p mean the graph is densely connected
# the Nx lib includes an ER graph generator but we will write our own.
# The we would be able to implement a more complex network model of the kind not included in the Nx lib
# to implement the coin flip part we will import a fn from scipy stats

### pseudocode for the random graph generator
#number of nodes, N = 20
#probability of edge, p = 0.2

#create empty graph
#add all nodes in the graph
#loop over all pairs of nodes
          # add edge with probability p

N = 20
p = 0.2
G = nx. Graph()
G.add_nodes_from(range(N))
for node1 in G.nodes():
  for node2 in G.nodes():
    # True == 1 
    #if bernoulli.rvs(p=p) == True: is the same as:
    if bernoulli.rvs(p=p):
      G.add_edge(node1, node2)


G.nodes()
NodeView((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))

G.number_of_nodes()
20

G.number_of_edges()
72

# Edges seems v high when probability is only 0.2

nx.draw(G)

plt.savefig("random_nx_1")

plt.show
<function matplotlib.pyplot.show(*args, **kw)>

plt.show()

# yep has far to many edges - why?

# We have considered each pair twice - because we consider node1 being 10 and
#node2 being 1 BUT ALSO node1 being 1 and node2 being 10.

G = nx. Graph()
G.add_nodes_from(range(N))
for node1 in G.nodes():
  for node2 in G.nodes():
    # will also work if use >
    if node1 < node2 and bernoulli.rvs(p=p):
      G.add_edge(node1, node2)

nx.draw(G)

plt.savefig('random_nx_2')

plt.show()

G.number_of_nodes()
20

G.number_of_edges()
37

# turn into fn:

def er_graph(N, p):
  """ Generate a random ER Network Graph """
  G = nx. Graph()
  G.add_nodes_from(range(N))
  for node1 in G.nodes():
    for node2 in G.nodes():
      if node1 < node2 and bernoulli.rvs(p=p):
        G.add_edge(node1, node2)
  return G

# Test by calling directly from nx.draw:

nx.draw(er_graph(50, 0.08))
nx.draw(er_graph(50, 0.08), node_size=40, node_color='gray')
plt.savefig('er_final')
plt.show()

