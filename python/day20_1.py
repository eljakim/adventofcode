import sys

maze = [list(l.strip()) for l in sys.stdin.readlines()]
height=len(maze)
width=len(maze[0])
infinity=1+height*width
start_x=0
start_y=0
end_x=0
end_y=0

distances=[]
for y in range(height):
    d=width*[infinity]
    distances.append(d)
    for x in range(width):
        if maze[y][x]=='S':
            start_x=x
            start_y=y
            maze[y][x]="."
        if maze[y][x]=='E':
            end_x=x
            end_y=y
            maze[y][x]="."

sys.setrecursionlimit(infinity)


def floodfill(x,y,n):
    global distances
    if distances[y][x]<=n:
        return
    distances[y][x]=n
    if maze[y][x-1]==".":
        floodfill(x-1,y,n+1)
    if maze[y][x+1]==".":
        floodfill(x+1,y,n+1)
    if maze[y+1][x]==".":
        floodfill(x,y+1,n+1)
    if maze[y-1][x]==".":
        floodfill(x,y-1,n+1)

floodfill(start_x, start_y,0)
best=distances[end_y][end_x]
print(f"Best without cheating: {best}")
for d in distances:
    print(''.join([f"{x:4}" for x in d]))

cheats={}

for y in range(1,height-1):
    for x in range(1,width-1):
        better=0
        if distances[y][x]==infinity:

            left = distances[y][x-1]
            right = distances[y][x+1]
            top = distances[y-1][x]
            bottom = distances[y+1][x]

            if left!=infinity:
                if top!=infinity:
                    better=max(better, abs(top-left)-2)
                if right!=infinity:
                    better=max(better, abs(left-right)-2)
                if bottom!=infinity:
                    better=max(better, abs(bottom-left)-2)
            if right!=infinity:
                if top!=infinity:
                    better=max(better, abs(right-top)-2)
                if bottom!=infinity:
                    better=max(better, abs(right-bottom)-2)
            if bottom!=infinity:
                if top!=infinity:
                    better=max(better, abs(top-bottom)-2)
            if better>0:
                if better==64: print(x,y)
                cheats.setdefault(better,0)
                cheats[better]+=1

print("---")
s=0
for i in sorted(cheats.keys()):
    if i>=100:
        s+=cheats[i]
        print(i, cheats[i])
print(s)
