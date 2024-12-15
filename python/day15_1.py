import sys

lines=[l.strip() for l in sys.stdin.readlines()]

map={}
for i,x in enumerate(lines[:lines.index("")]):
    map[i]=list(x)
moves="".join(lines[lines.index("")+1:])
height=len(map)
width=len(map[0])

robot_x=0
robot_y=0
for robot_y in range(height):
    if '@' in map[robot_y]:
        robot_x=map[robot_y].index("@")
        break

def printMap(map):
    for m in map.values():
        print("".join(m))

def simulateMove(m, map, robot_x, robot_y):
    match(m):
        case '^':
            canMove = False
            for i in range(robot_y):
                if map[robot_y-i][robot_x]==".":
                    canMove=True
                    break
                if map[robot_y-i][robot_x]=="#":
                    break
            if canMove:
                for y in range(i):
                    map[robot_y-i+y][robot_x]=map[robot_y-i+y+1][robot_x]
                map[robot_y][robot_x]="."
                robot_y-=1
        case 'v':
            canMove = False
            for i in range(height-robot_y):
                if map[robot_y+i][robot_x]==".":
                    canMove=True
                    break
                if map[robot_y+i][robot_x]=="#":
                    break
            if canMove:
                for y in range(i):
                    map[robot_y+i-y][robot_x]=map[robot_y+i-y-1][robot_x]
                map[robot_y][robot_x]="."
                robot_y+=1
        case '<':
            canMove = False
            for i in range(robot_x):
                if map[robot_y][robot_x-i]==".":
                    canMove=True
                    break
                if map[robot_y][robot_x-i]=="#":
                    break
            if canMove:
                for x in range(i):
                    map[robot_y][robot_x-i+x]=map[robot_y][robot_x-i+x+1]
                map[robot_y][robot_x]="."
                robot_x-=1
        case '>':
            canMove = False
            for i in range(width-robot_x):
                if map[robot_y][robot_x+i]==".":
                    canMove=True
                    break
                if map[robot_y][robot_x+i]=="#":
                    break
            if canMove:
                for x in range(i):
                    map[robot_y][robot_x+i-x]=map[robot_y][robot_x+i-x-1]
                map[robot_y][robot_x]="."
                robot_x+=1
    return (map, robot_x, robot_y)



for m in moves:
    #printMap(map)
    #print(f"\nMove {m}")
    map, robot_x, robot_y = simulateMove(m, map, robot_x, robot_y)
printMap(map)

s=0
for y in range(height):
    for x in range(width):
        if map[y][x]=="O":
            s+=x+100*y
print(s)
# print(lines)
# print(map)
# print(moves)
# print(robot_x, robot_y)
