import sys

left = []
right =[]

for line in sys.stdin:
    a,b = [int(i) for i in line.split()]
    left.append(a)
    right.append(b)

left.sort()
right.sort()

diff = sum([abs(i[0]-i[1]) for i in zip(left, right)])

print(diff)
