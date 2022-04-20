# import networkx as nx
# import pandas as pd
# import matplotlib.pyplot as plt

# g=nx.Graph()
# # g.add_node(1)
# # g.add_node(2)
# # g.add_node(3)
# # g.add_node(4)

# g.add_nodes_from([1, 2, 3, 4 ])
# g.add_edge(1, 2)
# g.add_edge(2,3,{'weight':3.1415})
# g.add_edge(3, 4)
# g.add_edge(4, 1)
# # g.add_edge(1, 1, {'weight': 10})
# plt.subplot(122)
# nx.draw(g)
# plt.savefig("trying.png")

# import matplotlib.pyplot as plt
# import networkx as nx

# G = nx.Graph()

# G.add_edge("a", "b", weight=0.6)
# G.add_edge("a", "c", weight=0.2)
# G.add_edge("c", "d", weight=0.1)
# G.add_edge("c", "e", weight=0.7)
# G.add_edge("c", "f", weight=0.9)
# G.add_edge("a", "d", weight=0.3)

# elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
# esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

# pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

# # nodes
# nx.draw_networkx_nodes(G, pos, node_size=700)

# # edges
# nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
# nx.draw_networkx_edges(
#     G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
# )

# # labels
# nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

# ax = plt.gca()
# ax.margins(0.08)
# plt.axis("off")
# plt.tight_layout()
# plt.show()

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

G=nx.DiGraph()
# g.add_node(1)
# g.add_nodes_from([2,3,4])
# g.add_edges_from([(1, 2), (1, 3)])



plt.subplot(122)
nx.draw(G)
plt.show()