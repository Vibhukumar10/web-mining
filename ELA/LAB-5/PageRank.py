import networkx as nx
import pylab as plt

Graph=nx.DiGraph()

Graph.add_weighted_edges_from([('A','D',1),('A','C',2),('B','A',1),('B','D',1),
                               ('B','E',2),('C','A',3),('C','E',2),('D','B',2),
                               ('D','E',3),('E','C',2),('E','A',2),('E','D',2)])

nx.draw(Graph, with_labels=True)
plt.show()

print(nx.pagerank(Graph))