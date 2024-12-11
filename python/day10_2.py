import sys

map=[]
trailheads={}

for line in sys.stdin.readlines():
    map.append(line.strip())

height=len(map)
width=len(map[0])
for y in range(height):
    for x in range(width):
        if map[y][x]=='0':
            trailheads[(x,y)]=[]

def search(x,y, trailhead):
    h = int(map[y][x])
    if h==9:
        trailheads[trailhead].append((x,y))
        return
    if x>0 and int(map[y][x-1])==h+1:
        search(x-1,y,trailhead)
    if x<width-1 and int(map[y][x+1])==h+1:
        search(x+1,y, trailhead)
    if y>0 and int(map[y-1][x])==h+1:
        search(x,y-1,trailhead)
    if y<height-1 and int(map[y+1][x])==h+1:
        search(x,y+1,trailhead)

for x,y in trailheads:
    search(x,y,(x,y))

s=0
for i in trailheads.values():
    print(i, len(i))
    s+=len(i)
print(s)
