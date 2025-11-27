"""Contains the PageRank algorithm itself.
   take the adjacency list from graph_loader.py"""


"""run the iterative PageRank loop (“redistribute score along links”)
handle:
--> damping factor (random jump, usually 0.85)
--> dangling nodes (pages with no outgoing links)
--> convergence stopping (when scores stop changing)
--> return a list/array of scores (one per node)"""


import json
import networkx as nx
import numpy as np

# Load graph
with open("graph.json") as f:
    graph = json.load(f)


G = nx.DiGraph()
for src, targets in graph.items():
    for dst in targets:
        G.add_edge(src, dst)


pr = nx.pagerank(G, alpha=0.85)

# sort pagernk 
sorted_pr = sorted(pr.items(), key=lambda x: x[1], reverse=True)

# print top pages 
for page, score in sorted_pr[:100]:
    print(f"{score:.5f}  →  {page}")
