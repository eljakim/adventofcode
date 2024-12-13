import sys

lines = sys.stdin.readlines()

def findPrize(btnA, btnB, prize):
    aX, aY= [int(c.split("+")[1]) for c in btnA.split(", ")]
    bX, bY= [int(c.split("+")[1]) for c in btnB.split(", ")]
    pX, pY= [int(c.split("=")[1]) for c in prize.split(", ")]

    possibles = []
    mA = 1+max(pX//aX, pY//aY)
    mB = 1+max(pX//bX, pY//bY)

    for a in range(mA):
        for b in range(mB):
            if a*aX + b*bX == pX and a*aY+b*bY==pY:
                possibles.append((a,b))
    tokens=0
    if possibles:
        tokens=min([3*p[0] + p[1] for p in possibles])
    return tokens
    #print(tokens, possibles)

#findPrize("X+17, Y+86", "X+84, Y+37", "X=7870, Y=6450")

tokens=0
for l in lines:
    a = l.strip().split(":")
    if a[0]=='Button A':
        buttonA = a[1]
    if a[0]=='Button B':
        buttonB = a[1]
    if a[0]=='Prize':
        tokens+=findPrize(buttonA, buttonB, a[1])
print(tokens)
