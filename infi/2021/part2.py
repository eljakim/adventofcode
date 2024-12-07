import sys
import collections

missend = int(sys.stdin.readline().split(" ")[0])

recepten = {}
for recept in sys.stdin.readlines():
    doel, parts = recept.split(":")
    parts = parts.strip().split(", ")
    parts=[(int(p.split(" ")[0]), p.split(" ")[1]) for p in parts]
    recepten[doel] = parts

onderdelen = {}

# onderdelen tellen
def berekenOnderdelen(a):
    global recepten, onderdelen
    parts = recepten[a]

    if a in onderdelen:
        return onderdelen[a]
    totals =0
    for n,p in parts:
        if p not in recepten:
            totals+=n
        else:
            totals+=n*berekenOnderdelen(p)
    onderdelen[a]=totals
    return totals

# bepalen wat speelgoed is
speelgoed=list(recepten.keys())
for a in recepten.keys():
    onderdelen[a] = berekenOnderdelen(a)
    for i,j in recepten[a]:
        if j in speelgoed:
            speelgoed.remove(j)

# dynamic programming om een manier te vinden om speelgoed te laten optellen tot missend
doable = {}
doable[0] = "root"
for i in range(1,1+missend):
    doable[i]=None
    for j in speelgoed:
        if onderdelen[j]<=i and doable[i-onderdelen[j]]:
            doable[i]=j
            break

# print(speelgoed)
# for s in speelgoed:
#    print(s, onderdelen[s])
# print(missend)
antwoord = []
j = missend
while j>0:
    antwoord.append(doable[j])
    j-=onderdelen[doable[j]]

# c=collections.Counter(antwoord)
# print(c)
print("".join(sorted([c[0] for c in antwoord])))
