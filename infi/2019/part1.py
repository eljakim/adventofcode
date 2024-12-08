sample = {
"flats": [[1,4],[3,8],[4,3],[5,7],[7,4],[10,3]],
"sprongen": [[2,0],[0,4],[1,0],[0,0]]
}

productie = {"flats":[[6,6],[7,7],[10,8],[13,9],[16,3],[17,6],[21,7],[26,2],[29,3],[30,4],[33,6],[37,7],[39,8],[43,9],[44,3],[45,6],[47,8],[48,10],[51,4],[53,4],[54,7],[56,10],[57,5],[60,6]],"sprongen":[[0,1],[2,1],[2,1],[2,0],[0,3],[3,1],[4,0],[2,1],[0,1],[2,2],[3,1],[1,1],[0,0],[0,0],[0,3],[1,2],[0,2],[2,0],[1,0],[0,3],[1,3],[0,0],[2,1]]}

uitvoeren = productie

x_pos = uitvoeren['flats'][0][0]
stap=1

flats={}
for f,h in uitvoeren['flats']:
    flats[f]=h

for deltax, deltay in uitvoeren['sprongen']:
    move_to = x_pos+deltax+1
    # print(stap, x_pos, move_to)
    if move_to in flats and flats[move_to]<=flats[x_pos]+deltay:
        stap+=1
        x_pos=move_to
    else: break

print(stap)
