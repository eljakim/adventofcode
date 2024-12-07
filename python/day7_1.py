import sys

equations = []
for line in sys.stdin:
    a = line.split(": ")
    equations.append([int(a[0]),[int(i) for i in a[1].split(" ")]])

def check(target, numbers, current=0):
    if numbers==[]:
        return current==target
    return check(target, numbers[1:], current+numbers[0]) or check(target, numbers[1:], current*numbers[0])

s=0
for target, numbers in equations:
    if check(target, numbers[1:], numbers[0]):
        s+=target

print(s)
