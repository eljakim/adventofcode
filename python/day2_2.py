import sys

levels = []

for line in sys.stdin:
    level = [int(i) for i in line.split()]
    levels.append(level)

safe=0

def is_safe(l):
    # nice way of finding the diff between successive numbers
    diffs = [t-s for s,t in zip(l, l[1:])]
    if(max(diffs)<0):
        if min(diffs)>=-3 and max(diffs)>=-3:
            return True
    if(min(diffs)>0):
        if max(diffs)<=3 and min(diffs)<=3:
            return True
    return False

for l in levels:
    levelOK=False
    # you could also check the original list without removing any items,
    # but if the original list is okay, it should still be okay if you remove
    # the very first item, so this is still correct.
    if len(l)>1:
        for i in range(1, len(l)+1):
            dampened = l[:i-1]+l[i:]
            if is_safe(dampened):
                levelOK=True
                # break automatically jumps out of the closest for-loop, so as soon
                # as you know the level is OK, stop searching for that line
                break
    else:
        # if the level has only a single number, it's always fine.
        levelOK=True
    if levelOK:
        safe+=1

print(safe)
