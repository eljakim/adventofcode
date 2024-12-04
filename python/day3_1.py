import sys, re


l = sys.stdin.read()
muls =re.findall("(mul\\([0-9]+,[0-9]+\\))",l)

s =0

for m in muls:
    a,b=m.split(",")
    a=int(a[4:])
    b=int(b[:-1])
    print(m,a,b)
    s+=a*b

print(s)
