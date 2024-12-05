import itertools
import sys

rules = []
updates = []

line=sys.stdin.readline().strip()
while line !="":
    rules.append(line.strip().split('|'))
    line=sys.stdin.readline().strip()

for line in sys.stdin:
    updates.append(line.strip().split(','))

def verifyRules(l, rules):
    for r in rules:
        first = r[0]
        second =r[1]
        if first in l and second in l and l.index(first)>l.index(second):
            return False
    return True

# print(rules)
#print(updates)

middles =0
for u in updates:
    if  verifyRules(u, rules):
        middles+=int(u[len(u)//2])

print(middles)
