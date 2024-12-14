import sys
import itertools

def ranges(i):
    for a, b in itertools.groupby(enumerate(i), lambda pair: pair[1] - pair[0]):
        b = list(b)
        yield b[0][1], b[-1][1]


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
#width=11
#height=7
cycles = 100
endpositions=[]

def robotsperline():
    global height
    global robots
    lines={}
    for p in [c[0] for c in robots]:
        x=p[0]
        y=p[1]
        if y not in lines:
            lines[y]=[]
        lines[y].append(x)
    consecutive=0
    for i in lines.keys():
        lines[i].sort()
        for a,b in ranges(lines[i]):
            consecutive=max(1+b-a, consecutive)
    return consecutive

    return max([len(i) for i in lines.values()])

def runCycle():
    global robots
    for r in robots:
        r[0][0]+=r[1][0]
        r[0][0]%=width
        r[0][1]+=r[1][1]
        r[0][1]%=height


m=0
runs={}
c=0
i=0

while i<6577:
    runCycle()
#    if i in [6576, 16979, 27382, 37785, 48188, 58591, 68994, 79397, 89800]:
#        print(f"<cycles count={i}>")
#        printRobots([c[0] for c in robots])
#        print("</cycles>")
#    z = robotsperline()
#    if z not in runs:
#        runs[z]=[]
#    runs[z].append(i)
#    m=max(m,z)
    i+=1
printRobots([c[0] for c in robots])
#print(m, runs[m])
#print(robotsperline())
