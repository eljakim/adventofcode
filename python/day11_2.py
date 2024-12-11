import sys

lines={}
line = [int(i) for i in sys.stdin.readline().strip().split(" ")]

lines[0]={}
for i in line:
    lines[0][i]=1

explode={}
def getexplode(n):
    global explode
    if n not in explode:
        if n==0:
            explode[n]=[1]
        elif len(str(n))%2==0:
            s = str(n)
            explode[n]=[int(s[:len(s)//2]), int(s[len(s)//2:])]
        else:
            explode[n]=[n*2024]
    return explode[n]




epoch=0
while epoch<75:
    #print(lines[epoch])
    target=epoch+1
    lines[target]={}
    for stone, cnt in lines[epoch].items():
        for a in getexplode(stone):
            if a not in lines[target]:
                lines[target][a]=cnt
            else:
                lines[target][a]+=cnt
    print(target, lines[target])
    epoch+=1

s=0
for k,v in lines[epoch].items():
    s+=v
print(s)
