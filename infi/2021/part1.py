import sys

missend = sys.stdin.readline()

recepten = {}
for recept in sys.stdin.readlines():
    doel, parts = recept.split(":")
    parts = parts.strip().split(", ")
    parts=[(int(p.split(" ")[0]), p.split(" ")[1]) for p in parts]
    recepten[doel] = parts

onderdelen = {}
print(recepten)

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
    return totals

for a in recepten.keys():
    print(berekenOnderdelen(a),a)
