import sys

input = sys.stdin.readline().strip()
filemap={}
empties=[]

fileno=0
position=0
readfile=True
for i in str(input):
    i=int(i)
    if readfile:
        fill=fileno
        fileno+=1
    else:
        fill=-1
    for p in range(i):
        filemap[position+p]=fill
        if not readfile:
            empties.append(position+p)
    position=max(filemap.keys())+1
    readfile = not readfile

for j in reversed(range(position)):
    if filemap[j]!=-1:
        if empties and empties[0]<j:
            # print(f"move {filemap[j]} from {j} to {empties[0]}")
            filemap[empties[0]]=filemap[j]
            filemap[j]=-1
            empties=empties[1:]

chksum=0
for i in range(position):
    if filemap[i]>0:
        chksum+=i*filemap[i]

print(chksum)

#print(",".join([str(c) for c in filemap.values()]))
