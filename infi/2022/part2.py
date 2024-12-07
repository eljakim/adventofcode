import sys
from PIL import Image, ImageDraw


instructions = [a.strip() for a in sys.stdin.readlines()]

x=0
y=0
max_x=0
max_y=0
richting=0
sporen=[]

def beweeg(richting, d):
    global x,y, max_x, max_y
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
    if x>max_x: max_x=x
    if y>max_y: max_y=y

for i in instructions:
    cmd, param = i.split(" ")
    param = int(param)
    match cmd:
        case "draai":
            richting+=param
            richting%=360
        case "loop":
            o_x=x
            o_y=y
            beweeg(richting, param)
            sporen.append([(o_x,o_y),(x,y)])
        case "spring":
            beweeg(richting, param)

scale=10
border=5
img = Image.new("RGBA", (2*border + scale*max_x,2*border + scale*max_y), "white")

lines = []
for van, naar in sporen:
    x_1, y_1 = van
    x_2, y_2 = naar
    x_1=border+scale*x_1
    y_1=border+ scale*max_y - scale*y_1
    x_2=border+scale*x_2
    y_2=border+scale * max_y - scale*y_2
    lines.append([(x_1,y_1),(x_2,y_2)])

draw=ImageDraw.Draw(img)

for l in lines:
    draw.line(l, fill="red", width=2)

img=img.convert("RGB")
img.save('answer.jpg', 'JPEG')
