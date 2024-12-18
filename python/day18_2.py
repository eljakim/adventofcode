from re import S
import sys

lines = [c.strip().split(",") for c in sys.stdin.readlines()]

height=71
width=71

def startup(f):
    global possibles
    global map
    global distances
    possibles={}
    distances={}
    distances[(0,0)]=0
    for y in range(height):
        for x in range(width):
            possibles[(x,y)]=width*height+10

    for x,y in lines[:f]:
        if (int(x), int(y)) in possibles:
            del(possibles[(int(x),int(y))])

def floodfill():
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
        if newmin==height*width+10:
            break
        removal=[]
        for (x,y),z in possibles.items():
            if z==newmin:
                removal.append((x,y))
        for (x,y) in removal:
            del(possibles[(x,y)])
            distances[(x,y)]=newmin
    if (height-1, width-1) in distances:
        return distances[(height-1, width-1)]
    else:
        return height*width+10


# hahah,, binary search met de hand gedaan...
# oplossing is een na laatste regel van de output
for i in range(2940, len(lines)):
    startup(i)
    x = floodfill()
    print(i,x, lines[i])
    if x==height*width+10:
        break
