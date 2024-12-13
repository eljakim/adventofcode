from re import L
import sys
import string

lines = []
regions=[]
regioncoors={}

for l in sys.stdin.readlines():
    lines.append(l.strip())
    regions.append(len(l.strip())*[-1])

height=len(lines)
width=len(lines[0])

regioncount=0

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




for y in range(height):
    for x in range(width):
        if regions[y][x]==-1:
            floodfill(x,y,regioncount)
            regioncount+=1

res=0
for r in range(regioncount):
    area = len(regioncoors[r])
    perimeter = calculatePerimeter(regioncoors[r])
    res+=area*perimeter

print(res)
