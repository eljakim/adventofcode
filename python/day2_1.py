import sys

levels = []

for line in sys.stdin:
    level = [int(i) for i in line.split()]
    levels.append(level)

safe=0

for l in levels:
    diffs = [t-s for s,t in zip(l, l[1:])]
    if(max(diffs)<0):
        if min(diffs)>=-3 and max(diffs)>=-3:
            safe+=1
    if(min(diffs)>0):
        if max(diffs)<=3 and min(diffs)<=3:
            safe+=1


print(safe)
