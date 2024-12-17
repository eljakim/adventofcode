import sys

lines=[l.strip() for l in sys.stdin.readlines()]

registerA=int(lines[0].split(": ")[1])
registerB=int(lines[1].split(": ")[1])
registerC=int(lines[2].split(": ")[1])

program=[int(i) for i in lines[4].split(": ")[1].split(",")]

def prettyPrint(program):
    counter=0
    print("regA = ", registerA)
    print("regB = ", registerB)
    print("regC = ", registerC)
    while counter<len(program)-1:
        opcode, operand = program[counter:counter+2]
        match(operand):
            case 0:
                value="0"
            case 1:
                value="1"
            case 2:
                value="2"
            case 3:
                value="3"
            case 4:
                value="regA"
            case 5:
                value="regB"
            case 6:
                value="regC"
            case 7:
                print("THIS SHOULD NOT HAPPEN")
        match(opcode):
            case 0:
                print(f"regA = regA//2**{value}")
            case 1:
                print(f"regB = regB ^ {operand}")
            case 2:
                print(f"regB = {value} % 8")
            case 3:
                print(f"jnz {operand}")
            case 4:
                print(f"regB = regB ^ regC")
            case 5:
                print(f"print({value})")
            case 6:
                print(f"regB = regA//2**{value}")
            case 7:
                print(f"regC = regA//2**{value}")
        counter+=2


def printOpcodes(program):
    counter=0
    while counter<len(program)-1:
        opcode, operand = program[counter:counter+2]
        match(operand):
            case 0:
                value="0"
            case 1:
                value="1"
            case 2:
                value="2"
            case 3:
                value="3"
            case 4:
                value="regA"
            case 5:
                value="regB"
            case 6:
                value="regC"
            case 7:
                print("THIS SHOULD NOT HAPPEN")
        match(opcode):
            case 0:
                print(f"adv {value}")
            case 1:
                print(f"bxl {operand}")
            case 2:
                print(f"bst {value}")
            case 3:
                print(f"jnz {operand}")
            case 4:
                print(f"bxc ")
            case 5:
                print(f"out {value}")
            case 6:
                print(f"bdv {value}")
            case 7:
                print(f"cdv {value}")
        counter+=2


printOpcodes(program)
prettyPrint(program)
