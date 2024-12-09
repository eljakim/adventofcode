import sys

input = sys.stdin.readline().strip()
filemap={}
empties=[]
files={}
gaps={}

fileno=0
gapno=0
position=0
readfile=True
for i in str(input):
    i=int(i)

    if readfile:
        files[fileno]=(position,i)
        fill=fileno
        fileno+=1
    else:
        gaps[gapno]=(position,i)
        gapno+=1
        fill=-1
    for p in range(i):
        filemap[position+p]=fill
    position=max(filemap.keys())+1
    readfile = not readfile

#print(files)
#print(gaps)
#print(fileno)
#print(",".join([str(c) for c in filemap.values()]))

for j in reversed(range(fileno)):
    file_pos = files[j][0]
    file_length = files[j][1]
    for gapno,gap in gaps.items():
        gap_pos=gap[0]
        gap_length=gap[1]
        if file_length<=gap_length and gap_pos<file_pos:
            gaps[gapno]=(gap_pos+file_length, gap_length-file_length)
            for p in range(file_length):
                filemap[gap_pos+p]=j
                filemap[file_pos+p]=-1
            #print(f"move {j}", filemap)
            break

chksum=0
for i in range(position):
    if filemap[i]>0:
        chksum+=i*filemap[i]

print(chksum)

#print(",".join([str(c) for c in filemap.values()]))
