import sys
import string
import itertools

lines = []
regions=[]
regioncoors={}

for l in sys.stdin.readlines():
    lines.append(l.strip())
    regions.append(len(l.strip())*[-1])

height=len(lines)
width=len(lines[0])

regioncount=0

def ranges(i):
    for a, b in itertools.groupby(enumerate(i), lambda pair: pair[1] - pair[0]):
        b = list(b)
        yield b[0][1], b[-1][1]

def floodfill(x,y,marker):
    global regions
    global regioncoors
    regions[y][x]=marker
    if marker not in regioncoors:
        regioncoors[marker]=[]
    regioncoors[marker].append((x,y))
    if x>0 and regions[y][x-1]==-1 and lines[y][x]==lines[y][x-1]:
        floodfill(x-1,y,marker)
    if x<width-1 and regions[y][x+1]==-1 and lines[y][x]==lines[y][x+1]:
        floodfill(x+1, y, marker)
    if y>0 and regions[y-1][x]==-1 and lines[y][x]==lines[y-1][x]:
        floodfill(x,y-1,marker)
    if y<height-1 and regions[y+1][x]==-1 and lines[y][x]==lines[y+1][x]:
        floodfill(x,y+1,marker)

def calculatePerimeter(r):
    p = 0
    for cell in r:
        x = cell[0]
        y = cell[1]
        if x==0 or x==width-1:
            p+=1
        if x>0 and (x-1, y) not in r:
            p+=1
        if x<width-1 and (x+1,y) not in r:
            p+=1
        if y==0 or y==height-1:
            p+=1
        if y>0 and (x, y-1) not in r:
            p+=1
        if y<height-1 and (x,y+1) not in r:
            p+=1
    return p

def calculateSides(r):
    #print("SHAPE",r)
    verticals=[]
    horizontals=[]
    for cell in r:
        x = cell[0]
        y = cell[1]
        if x==0:
            verticals.append(('L',x,y))
        if x==width-1:
            verticals.append(('R', x+1,y))
        if x>0 and (x-1, y) not in r:
            verticals.append(('L', x,y))
        if x<width-1 and (x+1,y) not in r:
            verticals.append(('R',x+1,y))
        if y==0:
            horizontals.append(('T',x,y))
        if y==height-1:
            horizontals.append(('B',x,y+1))
        if y>0 and (x, y-1) not in r:
            horizontals.append(('T',x,y))
        if y<height-1 and (x,y+1) not in r:
            horizontals.append(('B',x,y+1))

    hrange={}
    vrange={}
    for d,x,y in horizontals:
        if y not in hrange:
            hrange[y]={}
        if d not in hrange[y]:
            hrange[y][d]=[]
        hrange[y][d].append(x)
        hrange[y][d].sort()
    for d, x,y in verticals:
        if x not in vrange:
            vrange[x]={}
        if d not in vrange[x]:
            vrange[x][d]=[]
        vrange[x][d].append(y)
        vrange[x][d].sort()

    sidecount=0
    for x in hrange:
        for d, sides in hrange[x].items():
            sidecount+=len(list(ranges(sides)))
        #print(x,list(ranges(sides)))
    for y in vrange:
        for d, sides in vrange[y].items():
            sidecount+=len(list(ranges(sides)))
        #print(y, list(ranges(sides)))
    print(sidecount)
    return sidecount


for y in range(height):
    for x in range(width):
        if regions[y][x]==-1:
            floodfill(x,y,regioncount)
            regioncount+=1

res=0
for r in range(regioncount):
    area = len(regioncoors[r])
    perimeter = calculatePerimeter(regioncoors[r])
    sides = calculateSides(regioncoors[r])
    res+=area*sides

print(res)
