import sys
from collections import Counter
robot1_buttons=['0','1','2','3','4','5','6','7','8','9','A']
robot1_moves={}
robot1_touch={}
for i in robot1_buttons:
    robot1_touch[i]={}
    robot1_moves[i]={}
    for j in robot1_buttons:
        robot1_moves[i][j]=[]

robot1_touch['A']['0']='<'
robot1_touch['A']['3']='^'
robot1_touch['0']['2']='^'
robot1_touch['0']['A']='>'
robot1_touch['1']['2']='>'
robot1_touch['1']['4']='^'
robot1_touch['2']['0']='v'
robot1_touch['2']['1']='<'
robot1_touch['2']['3']='>'
robot1_touch['2']['5']='^'
robot1_touch['3']['A']='v'
robot1_touch['3']['2']='<'
robot1_touch['3']['6']='^'
robot1_touch['4']['1']='v'
robot1_touch['4']['5']='>'
robot1_touch['4']['7']='^'
robot1_touch['5']['2']='v'
robot1_touch['5']['4']='<'
robot1_touch['5']['6']='>'
robot1_touch['5']['8']='^'
robot1_touch['6']['3']='v'
robot1_touch['6']['5']='<'
robot1_touch['6']['9']='^'
robot1_touch['7']['4']='v'
robot1_touch['7']['8']='>'
robot1_touch['8']['5']='v'
robot1_touch['8']['7']='<'
robot1_touch['8']['9']='>'
robot1_touch['9']['6']='v'
robot1_touch['9']['8']='<'

def getRobot1Touches(path):
    p=""
    for i,j in zip(path,path[1:]):
        p+=robot1_touch[i][j]
    return p + "A"

def findRobot1Moves(a,b,visited=[]):
    global robot1_moves
    if not visited:
        visited=[a]
    last = visited[-1]
    if last==b:
        robot1_moves[a][b].append(getRobot1Touches(visited))
    else:
        for c in robot1_touch[last]:
            if c not in visited:
                findRobot1Moves(a,b,visited+[c])

for i in robot1_buttons:
    for j in robot1_buttons:
        findRobot1Moves(i,j)
        minl = min([len(c) for c in robot1_moves[i][j]])
        robot1_moves[i][j]=[s for s in robot1_moves[i][j] if len(s)==minl]



robot2_buttons=['<','v','>','^','A']
robot2_moves={}
robot2_touch={}
for i in robot2_buttons:
    robot2_touch[i]={}
    robot2_moves[i]={}
    for j in robot2_buttons:
        robot2_moves[i][j]=[]

robot2_touch['<']['v']='>'
robot2_touch['v']['<']='<'
robot2_touch['v']['^']='^'
robot2_touch['v']['>']='>'
robot2_touch['>']['v']='<'
robot2_touch['>']['A']='^'
robot2_touch['^']['v']='v'
robot2_touch['^']['A']='>'
robot2_touch['A']['^']='<'
robot2_touch['A']['>']='v'


def getRobot2Touches(path):
    p=""
    for i,j in zip(path,path[1:]):
        p+=robot2_touch[i][j]
    return p + "A"

def findRobot2Moves(a,b,visited=[]):
    global robot2_moves
    if not visited:
        visited=[a]
    last = visited[-1]
    if last==b:
        robot2_moves[a][b].append(getRobot2Touches(visited))
    else:
        for c in robot2_touch[last]:
            if c not in visited:
                findRobot2Moves(a,b,visited+[c])

for i in robot2_buttons:
    for j in robot2_buttons:
        findRobot2Moves(i,j)
        minl = min([len(c) for c in robot2_moves[i][j]])
        robot2_moves[i][j]=[s for s in robot2_moves[i][j] if len(s)==minl]

def robot1_solve(code):
    pushes=[robot1_moves[a][b] for a,b in list(zip('A'+code,code))]
    result=pushes[0]
    for p in pushes[1:]:
        new=[]
        for x in result:
            for y in p:
                new.append(x+y)
        result=new
    return result

def robot2_solve(code):
    pushes=[robot2_moves[a][b] for a,b in list(zip('A'+code,code))]
    result=pushes[0]
    for p in pushes[1:]:
        new=[]
        for x in result:
            for y in p:
                new.append(x+y)
        result=new
    return result

sort={}
sort["^"]=0
sort[">"]=1
sort["v"]=2
sort["<"]=3

def optimizeOne(l):
    res=[]
    for p in l.split("A"):
        res.append("".join(sorted(p, key=lambda v:sort[v])))
    return "A".join(res)

def optimizeAll(batch):
    a = min([len(b) for b in batch])
    #return [b for b in batch if len(b)==a]
    return list(set([optimizeOne(w) for w in batch]))


#a_s = robot1_solve("379A")
#b_s=[]
#c_s=[]
#for a in a_s:
#    b_s+=robot2_solve(a)
#b_s=optimizeAll(b_s)
#for b in b_s:
#    c_s+=robot2_solve(b)


codes=[line.strip() for line in sys.stdin.readlines()]
results={}
parts=[]
depth=2
for code in codes:
    results[code]=[]
    print(code)
    bs=[]
    current = robot1_solve(code)
    for i in range(depth):
        new=[]
        for c in current:
            new+=robot2_solve(c)
        current=optimizeAll(new)
    results[code]=current

s = 0
for k,v in results.items():

    minl = min([len(x) for x in v])
    value = int(k[:-1])
    print(k,minl,value)
    s+=minl*value

print(s)
