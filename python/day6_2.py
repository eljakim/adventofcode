import sys

lines = []
visited = []

obstacles = []


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

start = (guard_x, guard_y)

#lines = ['....#.....', '.........#', '..........', '..#.......', '.......#..', '..........', '.#........', '.......##.', '#.........', '......#...']

while guard_x>=0 and guard_y>=0 and guard_x<len(lines[0]) and guard_y<len(lines):
    l = list(visited[guard_y])
    l[guard_x]="X"
    l="".join(l)
    visited[guard_y]=l

    position=(guard_x, guard_y)
    obstacles.append(position)

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



def search(lines, guard_x, guard_y):
    global start
    guard_direction='up'
    beenthere=[]
    width=len(lines[0])
    height=len(lines)
    while guard_x>=0 and guard_y>=0 and guard_x<width and guard_y<height:
        position=(guard_x, guard_y, guard_direction)

        if position in beenthere:
            return True
        beenthere.append(position)

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
    return False


while start in obstacles:
    obstacles.remove(start)
obstacles=list(set(obstacles))

s=0
i=0
for o in obstacles:
    replacement=list(lines[o[1]])
    replacement[o[0]]='#'
    new = lines.copy()
    new[o[1]]="".join(replacement)
    if search(new, start[0], start[1]):
        s+=1
    i+=1

print(s)
