import sys

def printRobots(positions):
    global width, height
    map=[ ["." for c in range(width)] for i in range(height)]
    for p in positions:
        x=p[0]
        y=p[1]
        if map[y][x]!=".":
            map[y][x]=str(int(map[y][x])+1)
        else:
            map[y][x]="1"
    for m in map:
        print("".join(m))

robots=[]
for l in sys.stdin.readlines():
    parts = l.strip().split(" ")
    p = [int(c) for c in parts[0].split("=")[1].split(",")]
    v= [int(c) for c in parts[1].split("=")[1].split(",")]
    robots.append((p,v))

#robots=[([2,4],[2,-3])]
#robots=[([0,0],[1,1])]

width=101
height=103
cycles = 100
endpositions=[]

for r in robots:
    x =r[0][0]
    y=r[0][1]
    dx=r[1][0]
    dy=r[1][1]
    x = x + cycles * dx
    y = y + cycles * dy
    y%=height
    x%=width
    endpositions.append((x,y))

quadrants={}
for i in range(4):
    quadrants[i]=0

for x,y in endpositions:
    if x<width//2:
        if y<height//2:
            quadrants[0]+=1
        elif y>height//2:
            quadrants[1]+=1
    elif x>width//2:
        if y<height//2:
            quadrants[2]+=1
        elif y>height//2:
            quadrants[3]+=1

p=1
for v in quadrants.values():
    print(v)
    p*=v
print(p)
