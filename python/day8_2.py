import sys
import itertools

input=[]
for line in sys.stdin.readlines():
    input.append(line.strip())


def gcd(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)

height = len(input)
width=len(input[0])
nodes = {}
for i in range(height):
    for j in range(width):
        if input[i][j]!='.':
            c = input[i][j]
            if c not in nodes:
                nodes[c]=[]
            nodes[c].append((j,i))

antinodes = {}
for c,d in nodes.items():
    antinodes[c]=set()
    pairs = list(itertools.combinations(d,2))
    for p in pairs:
        antis=[]
        dx = p[0][0]-p[1][0]
        dy = p[0][1]-p[1][1]
        g = gcd(dx,dy)
        dx//=g
        dy//=g
        for i in range((1+width)//g):
            antis.append((p[0][0]+i*dx, p[0][1]+i*dy))
            antis.append((p[1][0]-i*dx, p[1][1]-i*dy))

        for x,y in antis:
            if x>=0 and x<width and y>=0 and y<width:
               antinodes[c].add((x,y))

everything = set()
for b in antinodes.values():
    everything|=b

print(len(everything), everything)
