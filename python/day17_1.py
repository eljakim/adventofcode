import sys

lines=[l.strip() for l in sys.stdin.readlines()]

registerA=int(lines[0].split(": ")[1])
registerB=int(lines[1].split(": ")[1])
registerC=int(lines[2].split(": ")[1])

program=[int(i) for i in lines[4].split(": ")[1].split(",")]
output=[]
pointer = 0

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

output = run(program, registerA, registerB, registerC)
print(",".join([str(i) for i in output]))
