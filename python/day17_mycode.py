
def run(program, A, B, C):
    output=[]
    pointer=0
    registerA=A
    registerB=B
    registerC=C
    while pointer<len(program)-1:
        opcode = program[pointer]
        operand = program[pointer+1]
        value=0
        jump=-1
        match(operand):
            case 0:
                value=0
            case 1:
                value=1
            case 2:
                value=2
            case 3:
                value=3
            case 4:
                value=registerA
            case 5:
                value=registerB
            case 6:
                value=registerC
            case 7:
                print("THIS SHOULD NOT HAPPEN")
        match(opcode):
            case 0: # adv
                denominator=2**value
                registerA=registerA//denominator
            case 1: # bxl
                registerB=registerB ^ operand
            case 2: # bst
                registerB=value%8
            case 3: # jnz
                if registerA!=0:
                    jump=operand
            case 4: # bxc
                registerB=registerB ^ registerC
            case 5: # out
                output.append(value % 8)
            case 6: # bdv
                denominator=2**value
                registerB = registerA//denominator
            case 7: # cdv
                denominator=2**value
                registerC = registerA//denominator
        if jump>=0:
            pointer=jump
        else:
            pointer+=2
    return output



def sim2(A):
    regA = A
    regB = 0
    regC = 0
    regB = regA & 7
    regB = regB ^ 1
    regC = regA>>regB
    regA = regA>>3
    regB = regB ^ 4
    regB = regB ^ regC
    return regB%8,regA

prev=0
baseline={}
for i in range(10):
    baseline[i]=[]

for i in range(1024):
    r,a = sim2(i)
    baseline[r].append(i)

program =[2,4,1,1,7,5,0,3,1,4,4,4,5,5,3,0]

build = program[::-1]
#print(build)

def addToChain(result, digit):
    workwith=result<<3
    workwith=result%1024
    print(workwith)
    for j in range(8):
        if workwith+j in baseline[digit]:
            return result<<3+j

for j in range(2048):
    if run(program,j,0,0)==[0]:
        print("{:20b}".format(j), j)

for j in range(2048):
    if run(program,j,0,0)==[3,0]:
        print("{:20b}".format(j), j)

for j in range(2048):
    if run(program,j,0,0)==[5,3,0]:
        print("{:20b}".format(j), j)

for j in range(10000):
    if run(program,j,0,0)==[5,5,3,0]:
        print("{:20b}".format(j), j)


def binprint(n):
    print("{:20b}".format(n), n)

print("---")
print(run(program,5,0,0))
print("---")
result=[5]
for b in range(2, len(build)+1):
    new = []
    for r in result:
        for j in range(8):
            x = run(program, (r<<3)+j,0,0)
            if x == program[-b:]:
                new.append((r<<3)+j)
    result=new

result.sort()
print(result)
