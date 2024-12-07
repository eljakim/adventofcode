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

s=0
for x in range(30):
    for y in range(30):
        for z in range(30):
            s+=simulator(x,y,z)

print(s)
