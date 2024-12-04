import sys, re


l = sys.stdin.read()
muls =re.findall("(mul\\([0-9]+,[0-9]+\\)|do\\(\\)|don't\\(\\))",l)

s =0

do = True

for m in muls:
    if m=='do()':
        do = True
    elif m=="don't()":
        do = False
    else:
        a,b=m.split(",")
        a=int(a[4:])
        b=int(b[:-1])
        if do:
            s+=a*b

print(s)
