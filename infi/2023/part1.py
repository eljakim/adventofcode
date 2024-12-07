import sys
import math

coordinates=[]

def splitLine(l):
    res = []
    for i in l[1:-1].split("), ("):
        x,y = [int(c) for c in i.split(", ")]
        res.append((x,y))
    return res


coors = splitLine("(55, -72), (-58, -37), (-54, 21), (41, -95)")
coors = splitLine("(0, 4), (3, -2), (-1, -2), (-2, 0)")

m=0
for line in sys.stdin.readlines():
    coors = splitLine(line.strip())
    m+=max([((a*a+b*b)**0.5) for a,b in coors])

print(m)
