import sys

puzzle=[]

for line in sys.stdin:
    puzzle.append(line.strip())

search = []
search.append("MMASS")
search.append("MSAMS")
search.append("SMASM")
search.append("SSAMM")

correct=0
for x in range(len(puzzle[0])-2):
    for y in range(len(puzzle)-2):
        pattern = ""
        pattern+=puzzle[y][x]
        pattern+=puzzle[y+2][x]
        pattern+=puzzle[y+1][x+1]
        pattern+=puzzle[y][x+2]
        pattern+=puzzle[y+2][x+2]
        if pattern in search:
            correct+=1

print(correct)
