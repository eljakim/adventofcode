import sys

puzzle=[]

for line in sys.stdin:
    puzzle.append(line.strip())

def findWord(word, line):
    count=0
    revword=word[::-1]
    for j in range(1+len(line)-len(word)):
        print(line[j:j+len(word)])
        if line[j:j+len(word)]==word or line[j:j+len(word)]==revword:
            count+=1
    return count

def getDiagonals(p):
    lines = []
    rowlength = len(p[0])
    puzzlelength=len(p)
    for y in range(puzzlelength):
        w1=""
        w2=""
        for j in range(rowlength):
            if y+j<puzzlelength and j<rowlength:
                w1+=p[y+j][j]
                w2+=p[puzzlelength-y-j-1][j]

        lines.append(w1)
        lines.append(w2)
    for x in range(1,rowlength):
        w1=""
        w2=""
        for j in range(rowlength):
            if x+j<rowlength and j<puzzlelength:
                w1+=p[j][x+j]
                w2+=p[puzzlelength-j-1][x+j]
        lines.append(w1)
        lines.append(w2)
    return lines

def getVerticals(p):
    puzzlelength=len(p)
    words=[]
    for x in range(len(p[0])):
        w=""
        for y in range(puzzlelength):
            w+=p[y][x]
        words.append(w)
    return words

all = puzzle + getVerticals(puzzle) + getDiagonals(puzzle)

print(sum([findWord("XMAS",l) for l in all]))

# print("XMASAMX")
# print(findWord("XMAS", "XMASAMX"))

exit(0)

for l in all:
    print(l, findWord("XMAS",l))
