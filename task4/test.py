import networkx as nx
import matplotlib.pyplot as plt

g=nx.Graph()

g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(1,4)
g.add_edge(1,5)
g.add_edge(5,6)
g.add_edge(5,7)
g.add_edge(4,8)
g.add_edge(3,8)

g=nx.cubical_graph()

plt.subplot(122)

nx.draw(g, pos=nx.circular_layout(g), node_color='r', edge_color='b')

plt.savefig('test.png')