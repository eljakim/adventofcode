import sys

lines = []
visited = []

for line in sys.stdin:
    lines.append(line.strip())
    visited.append(line.strip())

guard_x=-1
guard_y=-1
guard_direction='up'
for y in range(len(lines)):
    if "^" in lines[y]:
        guard_y=y
        guard_x=lines[y].index("^")
        lines[y]=lines[y].replace("^",".")

while guard_x>=0 and guard_y>=0 and guard_x<len(lines[0]) and guard_y<len(lines):
    l = list(visited[guard_y])
    l[guard_x]="X"
    l="".join(l)
    visited[guard_y]=l

    if guard_direction=='up':
        if guard_y>0:
            if lines[guard_y-1][guard_x]=='.':

                guard_y-=1
            else:
                guard_direction="right"
        else:
            guard_y-=1

    if guard_direction=="right":
        if guard_x<len(lines[0])-1:
            if lines[guard_y][guard_x+1]=='.':
                guard_x+=1
            else:
                guard_direction="down"
        else:
            guard_x+=1

    if guard_direction=="down":
        if guard_y<len(lines)-1:
            if lines[guard_y+1][guard_x]=='.':
                guard_y+=1
            else:
                guard_direction="left"
        else:
            guard_y+=1

    if guard_direction=="left":
        if guard_x>0:
            if lines[guard_y][guard_x-1]=='.':
                guard_x-=1
            else:
                guard_direction="up"
        else:
            guard_x-=1

print("\n".join(visited))

v = 0
for l in visited:
    v+=l.count("X")

print(v)
