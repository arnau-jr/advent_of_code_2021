import numpy as np


def initialize_dots(coord_list,max_x,max_y):
    dots = np.zeros([max_y+1,max_x+1],dtype=np.int)

    for coord in coord_list:
        dots[coord[1],coord[0]] = 1
    return dots

def fold_dots(dots, instruction):
    if(instruction[0]==1):
        cut = instruction[1]
        top_half = dots[0:cut,:]
        bottom_half = dots[cut+1:,:]

        flipped = np.flip(bottom_half,axis=0)

        top_half += flipped
        top_half = np.where(top_half>0,1,0)
        return top_half
    elif(instruction[0]==0):
        cut = instruction[1]
        left_half = dots[:,0:cut]
        right_half = dots[:,cut+1:]

        flipped = np.flip(right_half,axis=1)

        left_half += flipped
        left_half = np.where(left_half>0,1,0)
        return left_half

def main():
    with open("input.txt","r") as file:
        lines = file.readlines()

        max_x = 0
        max_y = 0
        coord_list = []
        for line in lines:
            if(line != "\n"):
                splitted = line.split(",")
                coords = tuple([int(x) for x in splitted])
                if(coords[0]>max_x): max_x = coords[0]
                if(coords[1]>max_y): max_y = coords[1]
                coord_list.append(coords)
            else:
                break

        instructions = []
        for line in lines:
            if(line != "\n"):
                line = line.strip().split()
                if(line[0] == "fold"):
                    fold_coord = line[-1].split("=")[0]
                    fold_pos = int(line[-1].split("=")[1])
                    if(fold_coord=="x"):
                        instruction = (0,fold_pos) #x is 0
                        instructions.append(instruction)
                    elif(fold_coord=="y"):
                        instruction = (1,fold_pos) #y is 1
                        instructions.append(instruction)

        print(f"Maximum paper coordinates: {max_x},{max_y}")
        # print(f"Instructions: {instructions}")

    dots = initialize_dots(coord_list,max_x,max_y)
    for i,instruction in enumerate(instructions):
        dots = fold_dots(dots, instruction)
        if(i==0):
            print(f"Number of visible dots after the first fold: {dots.sum()}")
    print(f"Number of visible dots after all folds: {dots.sum()}")

    with open("output.txt","w") as f:
        for i in range(dots.shape[0]):
            f.write(str(dots[i,:]))
    


if(__name__=="__main__"):
    main()