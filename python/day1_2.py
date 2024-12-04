import sys
from collections import Counter

left = []
right =[]

for line in sys.stdin:
    a,b = [int(i) for i in line.split()]
    left.append(a)
    right.append(b)

left.sort()
right.sort()

r = Counter(right)
s=0
for i in left:
    if i in r:
        s+=i*r[i]

print(s)
