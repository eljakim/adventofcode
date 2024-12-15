import sys

lines=[l.strip() for l in sys.stdin.readlines()]

map={}
boxes={}
robot_x=0
robot_y=0
for i,x in enumerate(lines[:lines.index("")]):
    m=""
    for b in x:
        if b=="O":
            boxes[len(boxes)]=(len(m),i)
            m+="[]"
        elif b=="#":
            m+="##"
        elif b=="@":
            robot_y=i
            robot_x=len(m)
            m+="@."
        elif b==".":
            m+=".."
    map[i]=list(m)
if robot_x==0 or robot_y==0:
    print("ERROR")
    exit(0)
moves="".join(lines[lines.index("")+1:])
height=len(map)
width=len(map[0])

def printMap(map):
    for m in map.values():
        print("".join(m))

def canMove(m,x,y):
    global map
    match(m):
        case "<":
            for i in range(x):
                if map[y][x-i]=="#":
                    return 0
                if map[y][x-i]==".":
                    return i
        case ">":
            for i in range(width-x):
                if map[y][x+i]=="#":
                    return 0
                if map[y][x+i]==".":
                    return i
        case "^":
            if map[y-1][x]==".":
                return 1
            elif map[y-1][x]=="#":
                return 0
            elif map[y-1][x]=="[":
                return canMove(m,x,y-1) * canMove(m,x+1,y-1)
            elif map[y-1][x]=="]":
                return canMove(m,x-1,y-1) * canMove(m,x,y-1)
        case "v":
            if map[y+1][x]==".":
                return 1
            elif map[y+1][x]=="#":
                return 0
            elif map[y+1][x]=="[":
                return canMove(m,x,y+1) *  canMove(m,x+1,y+1)
            elif map[y+1][x]=="]":
                return canMove(m,x-1,y+1) * canMove(m,x,y+1)
    return 0

def doMove(m,i,x,y):
    global map
    global robot_x, robot_y
    if i==0: return
    cur=map[y][x]
    match(m):
        case "<":
            for j in range(i):
                map[y][x-i+j]=map[y][x-i+j+1]
            map[y][x]="."
            if y==robot_y and x==robot_x:
                robot_x-=1
        case ">":
            for j in range(i):
                map[y][x+i-j]=map[y][x+i-j-1]
            map[y][x]="."
            if y==robot_y and x==robot_x:
                robot_x+=1
        case "^":
            if map[y-1][x]==".":
                map[y-1][x]=map[y][x]
            elif map[y-1][x]=="[":
                doMove("^", i, x,y-1)
                doMove("^", i, x+1, y-1)
            elif map[y-1][x]=="]":
                doMove("^", i, x-1,y-1)
                doMove("^", i, x,y-1)
            map[y][x]="."
            map[y-1][x]=cur
            if y==robot_y and x==robot_x:
                robot_y-=1
        case "v":
            if map[y+1][x]==".":
                map[y+1][x]=map[y][x]
            elif map[y+1][x]=="[":
                doMove("v", i, x,y+1)
                doMove("v", i, x+1, y+1)
            elif map[y+1][x]=="]":
                doMove("v", i, x-1,y+1)
                doMove("v", i, x,y+1)
            map[y][x]="."
            map[y+1][x]=cur
            if y==robot_y and x==robot_x:
                robot_y+=1

def simulateMove(direction, x, y):
    i = canMove(direction,x,y)
    doMove(direction, i, x, y)

#printMap(map)
#print(robot_x, robot_y)
#simulateMove(">", robot_x, robot_y)
#printMap(map)
#simulateMove("v", robot_x, robot_y)
#printMap(map)
#simulateMove("v", robot_x, robot_y)
#simulateMove("<", robot_x, robot_y)
#simulateMove("<", robot_x, robot_y)
#simulateMove("^", robot_x, robot_y)
#print(canMove('^',robot_x, robot_y))
#print(robot_x, robot_y)
#printMap(map)
#print(robot_x, robot_y)
#print(canMove("v", robot_x, robot_y))
#exit(0)

for m in moves:
    #printMap(map)
    #print(f"\nMove {m}")
    simulateMove(m, robot_x, robot_y)
printMap(map)

s=0
for y in range(height):
    for x in range(width):
        if map[y][x]=="[":
            s+=x+100*y
print(s)
# print(lines)
# print(map)
# print(moves)
# print(robot_x, robot_y)
