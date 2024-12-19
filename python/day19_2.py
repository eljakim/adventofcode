import sys

lines = [l.strip() for l in sys.stdin.readlines()]

dictionary = lines[0].split(", ")
sentences = lines[2:]

class Node:

    def addWord(self, w):
        if w=="":
            self.end = True
        else:
            if w[0] not in self.next:
                self.next[w[0]]=Node()
            self.next[w[0]].addWord(w[1:])

    def checkWord(self, w):
        if w=="":
            return self.end
        else:
            if w[0] not in self.next:
                return False
            else:
                return self.next[w[0]].checkWord(w[1:])

    def __init__(self):
        self.end=False
        self.next={}

cache={}
def wordCache(w):
    global cache
    global start
    if not w in cache:
        cache[w]=start.checkWord(w)
    return cache[w]

start = Node()
for w in dictionary:
    start.addWord(w)

def canbuild(sentence):
    global start
    explode=[start]
    for l in sentence:
        mynext=[]
        w=False
        for e in explode:
            if l in e.next:
                mynext.append(e.next[l])
                if e.next[l].end:
                    mynext.append(start)
                    w=True
        explode=list(set(mynext))
    return w

def buildwise(sentence):
    build={}
    build[0]=1

    for i in range(1,len(sentence)+1):
        w=0
        for j in range(1, i+1):
            test =sentence[i-j:i]
            if wordCache(test):
                w+=build[i-j]
        build[i]=w
    return build[len(build)-1]

ok=0
ways=0
for s in sentences:
    if canbuild(s):
        ok+=1
        ways+=buildwise(s)

print(ways)
