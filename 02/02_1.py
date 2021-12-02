
def perform_instruction(instruction,pos,depth):
    #Kind of dirty, also taking advantage that there is no "back" isntruction
    if(instruction[0]=="forward"):
        pos += instruction[1]
    elif(instruction[0]=="down"):
        depth += instruction[1]
    else:
        depth += -instruction[1]

    return pos,depth

def main():
    position = 0
    depth = 0
    with open("input.txt","r") as file:
        lines = file.readlines()

    instructions = []
    for l in lines:
        splitted = l.split()
        instructions.append((splitted[0],int(splitted[1])))
    for ins in instructions:
        position,depth = perform_instruction(ins, position, depth)
    
    print(f"Final position is: {position}")
    print(f"Final depth    is: {depth}")
    print(f"Product          : {depth*position}")



if(__name__=="__main__"):
    main()