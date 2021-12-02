
def perform_instruction(instruction,pos,depth,aim):
    #Kind of dirty, also taking advantage that there is no "back" isntruction
    if(instruction[0]=="forward"):
        pos += instruction[1]
        depth += aim*instruction[1]
    elif(instruction[0]=="down"):
        aim += instruction[1]
    else:
        aim += -instruction[1]

    return pos,depth,aim

def main():
    position = 0
    depth = 0
    aim = 0
    with open("input.txt","r") as file:
        lines = file.readlines()

    instructions = []
    for l in lines:
        splitted = l.split()
        instructions.append((splitted[0],int(splitted[1])))
    for ins in instructions:
        position,depth,aim = perform_instruction(ins, position, depth, aim)
    
    print(f"Final position is: {position}")
    print(f"Final depth    is: {depth}")
    print(f"Product          : {depth*position}")



if(__name__=="__main__"):
    main()