

def driehoek(n):
    return n*(n+1)//2

def vierkant(n):
    return n*n

def achthoek(n):
    return 4*driehoek(n-1)+5*vierkant(n)

def zaksize(inwoners):
    size=1
    t = achthoek(size)
    while t<=inwoners:
        size+=1
        t=achthoek(size)
    return size

def zakstof(size):
    return 8*size

continenten = {"Azië": 4541396896, "Afrika": 1340812277, "Europa": 747701769, "Zuid-Amerika": 430855650, "Noord-Amerika": 368995941, "Oceanië": 42712683}

stof=0
for a,b in continenten.items():
    size = zaksize(b)
    stof+=zakstof(size)
    print(a, size, zakstof(size))

print(stof)
