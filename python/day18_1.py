import sys

lines = [c.strip().split(",") for c in sys.stdin.readlines()]

height=71
width=71
first=1024

lines=lines[:first]

map=[]
possibles={}
for y in range(height):
    row=[]
    for x in range(width):
        row+=["."]
        possibles[(x,y)]=width*height+10
    map.append(row)

for x,y in lines:
    map[int(y)][int(x)]="#"
    if (int(x), int(y)) in possibles:
        del(possibles[(int(x),int(y))])

distances={}
distances[(0,0)]=0

for y in range(height):
    for x in range(width):
        if (x,y) in distances:
            print(f"{distances[x,y]:5}", end="")
        elif (x,y) in possibles:
            print("     ", end="")
        else:
            print("XXXXX", end="")
    print()

while (width-1,height-1) not in distances:
    for (x,y),d in distances.items():
        if (x-1,y) in possibles and possibles[(x-1,y)]>d+1:
            possibles[(x-1,y)]=d+1
        if (x+1,y) in possibles and possibles[(x+1,y)]>d+1:
            possibles[(x+1,y)]=d+1
        if (x,y-1) in possibles and possibles[(x,y-1)]>d+1:
            possibles[(x,y-1)]=d+1
        if (x,y+1) in possibles and possibles[(x,y+1)]>d+1:
            possibles[(x,y+1)]=d+1
    newmin = min(possibles.values())
    removal=[]
    for (x,y),z in possibles.items():
        if z==newmin:
            removal.append((x,y))
    for (x,y) in removal:
        del(possibles[(x,y)])
        distances[(x,y)]=newmin

for y in range(height):
    for x in range(width):
        if (x,y) in distances:
            print(f"{distances[x,y]:5}", end="")
        elif (x,y) in possibles:
            print("     ")
        else:
            print("XXXXX")
    print()
print(distances)
print(distances[(width-1,height-1)])
