

def driehoek(n):
    return n*(n+1)//2

def vierkant(n):
    return n*n

def achthoek(n):
    return 4*driehoek(n-1)+5*vierkant(n)

size=1
t = achthoek(size)
while t<=17474944:
    size+=1
    t=achthoek(size)

print(size, achthoek(size))
