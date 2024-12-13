import sys
import numpy as np

lines = sys.stdin.readlines()

def lcm(a, b):
    return abs(a*b)


def findPrize(btnA, btnB, prize):
    aX, aY= [int(c.split("+")[1]) for c in btnA.split(", ")]
    bX, bY= [int(c.split("+")[1]) for c in btnB.split(", ")]
    pX, pY= [int(c.split("=")[1]) for c in prize.split(", ")]
    pX+=10000000000000
    pY+=10000000000000
    A = np.array([[aX, bX],[aY, bY]])
    B = np.array([pX, pY])
    Solutions = np.linalg.lstsq(A,B)
    found=[]
    for S in Solutions:
        if len(S)!=2: break
        S = np.round(S).astype(int)
        a=S[0]
        b=S[1]

        if a*aX+b*bX==pX and a*aY+b*bY==pY:
            found.append((a,b))
    if found:
        tokens = min([3*a+b for a,b in found])
    else:
        tokens=0
    return tokens

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
