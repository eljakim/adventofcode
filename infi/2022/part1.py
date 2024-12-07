import sys

instructions = [a.strip() for a in sys.stdin.readlines()]

x=0
y=0
richting=0

def beweeg(richting, d):
    global x,y
    match richting:
        case 0:
            y+=d
        case 45:
            x+=d
            y+=d
        case 90:
            x+=d
        case 135:
            x+=d
            y-=d
        case 180:
            y-=d
        case 225:
            x-=d
            y-=d
        case 270:
            x-=d
        case 315:
            x-=d
            y+=d

for i in instructions:
    cmd, param = i.split(" ")
    param = int(param)
    match cmd:
        case "draai":
            richting+=param
            richting%=360
        case "loop":
            beweeg(richting, param)
        case "spring":
            beweeg(richting, param)

print(x,y,x+y)
