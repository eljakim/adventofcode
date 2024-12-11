import sys

lines={}
lines[0] = [int(i) for i in sys.stdin.readline().strip().split(" ")]

epoch=0
target=0
source=1
while epoch<25:
    source=target
    target=1-target
    lines[target]=[]
    for i in lines[source]:
        if i==0:
            lines[target].append(1)
        elif len(str(i))%2==0:
            s = str(i)
            lines[target].append(int(s[:len(s)//2]))
            lines[target].append(int(s[len(s)//2:]))
        else:
            lines[target].append(i * 2024)
    print(epoch, lines[target])
    epoch+=1

print(len(lines[target]))
