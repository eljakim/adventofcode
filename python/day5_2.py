import sys

rules = []
updates = []

line=sys.stdin.readline().strip()
while line !="":
    rules.append(line.strip().split('|'))
    line=sys.stdin.readline().strip()
rules.sort()

for line in sys.stdin:
    updates.append(line.strip().split(','))

def verifyRules(l, rules):
    for r in rules:
        first = r[0]
        second =r[1]
        if first in l and second in l and l.index(first)>l.index(second):
            return False
    return True

new = {}
for a,b in rules:
    if a not in new:
        new[a]=[]
    if b not in new:
        new[b]=[]
for a,b in rules:
    new[b]+=[a]

def flattenRules(new):
    if len(new)==0:
        return []
    a = [b for b,c in new.items() if c==[]][0]
    return [a] + flattenRules({c:[z for z in d if z!=a] for c,d in new.items() if c!=a})

middles =0
for u in updates:
    if not verifyRules(u, rules):
        t = { a:[x for x in b if x in u] for a,b in new.items() if a in u}
        n = [c for c in flattenRules(t) if c in u]
        middles+=int(n[len(n)//2])

print(middles)
