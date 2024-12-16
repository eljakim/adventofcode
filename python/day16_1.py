import sys
import copy

from numpy._typing import _16Bit

lines=[l.strip() for l in sys.stdin.readlines()]

height=len(lines)
width=len(lines[0])
bests=[]

start_x=0
start_y=0
end_x=0
end_y=0
direction=0
for y in range(height):
    l = []
    for x in range(width):
        if lines[y][x]=='S':
            start_x=x
            start_y=y
        if lines[y][x]=='E':
            end_x=x
            end_y=y
        l.append([-1,-1,-1,-1])
    bests.append(l)

if end_x==0:
    print("ERROR")
    exit(0)

bests[start_y][start_x]=[0,-1,-1,-1]
current=[(start_x, start_y,0)]

def expand():
    global current
    result=[]
    for x,y,dir in current:
        future_x=x
        future_y=y
        match(dir):
            case(0): future_x=x+1
            case(1): future_y=y-1
            case(2): future_x=x-1
            case(3): future_y=y+1
        if lines[future_y][future_x]=='.' or lines[future_y][future_x]=='E':
            if bests[future_y][future_x][dir] == -1 or bests[future_y][future_x][dir]>bests[y][x][dir]+1:
                bests[future_y][future_x][dir]=bests[y][x][dir]+1
                result.append((future_x, future_y,dir))
        future_dirs=[((dir+1)%4,1000), ((dir+3)%4,1000), ((dir+2)%4,2000)]
        for future_dir, penalty in future_dirs:
            if bests[y][x][future_dir]==-1 or bests[y][x][future_dir]>bests[y][x][dir]+penalty:
                bests[y][x][future_dir]=bests[y][x][dir]+penalty
                result.append((x,y,future_dir))
    return result

while current:
    current = expand()

print(min(bests[end_y][end_x]))
