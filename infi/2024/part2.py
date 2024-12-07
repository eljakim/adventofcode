import sys

program = [a.strip() for a in sys.stdin.readlines()]


def simulator(x,y,z):
    global program
    stack = []
    counter=0
    instruction=None

    while instruction!="ret":
        instruction = program[counter].split(" ")
        match instruction[0]:
            case "ret":
                break
            case "push":
                match instruction[1]:
                    case "X":
                        stack.append(x)
                    case "Y":
                        stack.append(y)
                    case "Z":
                        stack.append(z)
                    case _:
                        stack.append(int(instruction[1]))
            case "add":
                stack.append(stack.pop() + stack.pop())
            case "jmpos":
                if stack.pop()>=0:
                    counter+=int(instruction[1])
        counter+=1
    return stack.pop()

sky = {}
for x in range(30):
    for y in range(30):
        for z in range(30):
            if simulator(x,y,z)>0:
                sky[(x,y,z)]=-1
            else:
                sky[(x,y,z)]=0

def markClouds(x,y,z,n):
    global sky
    sky[(x,y,z)]=n
    if x>0 and sky[(x-1,y,z)]==-1:
        markClouds(x-1,y,z,n)
    if y>0 and sky[(x,y-1,z)]==-1:
        markClouds(x,y-1,z,n)
    if z>0 and sky[(x,y,z-1)]==-1:
        markClouds(x,y,z-1,n)
    if x<29 and sky[(x+1,y,z)]==-1:
        markClouds(x+1,y,z,n)
    if y<29 and sky[(x,y+1,z)]==-1:
        markClouds(x,y+1,z,n)
    if z<29 and sky[(x,y,z+1)]==-1:
        markClouds(x,y,z+1,n)

sys.setrecursionlimit(30*30*30)

cloud=0
while -1 in sky.values():
    cloud+=1
    x,y,z = list(sky.keys())[list(sky.values()).index(-1)]
    markClouds(x,y,z,cloud)

print(cloud)
