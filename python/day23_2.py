import sys
import networkx

lines = [l.strip() for l in sys.stdin.readlines()]
graph = networkx.Graph()

for l in lines:
    a,b=l.split("-")
    graph.add_edge(a,b)

cliques = networkx.find_cliques(graph)

c = sorted(cliques, key=len, reverse=True)[0]
print(",".join(sorted(c)))
