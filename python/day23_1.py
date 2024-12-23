import sys
from itertools import combinations

lines = [l.strip() for l in sys.stdin.readlines()]

map=set()
nodes=set()
tnodes=set()
nontnodes=set()

for l in lines:
    a,b=l.split("-")
    nodes.add(a)
    nodes.add(b)
    map.add((a,b))
    map.add((b,a))

for n in nodes:
    if n.startswith("t"):
        tnodes.add(n)
    else:
        nontnodes.add(n)

s=0
# 3x tnode
for t1,t2,t3 in combinations(tnodes,3):
    if (t1,t2) in map and (t2,t3) in map and (t1,t3) in map:
        s+=1

# 2x tnodes
for t1,t2 in combinations(tnodes,2):
    for t3 in nontnodes:
        if (t1,t2) in map and (t2,t3) in map and (t1,t3) in map:
            s+=1

# 1x tnodes
for t1 in tnodes:
    for t2,t3 in combinations(nontnodes,2):
        if (t1,t2) in map and (t2,t3) in map and (t1,t3) in map:
            s+=1

print(s)
