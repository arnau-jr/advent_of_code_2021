import numpy as np

def main():
    with open("input.txt","r") as file:
        lines = file.readlines()
        height_map = np.zeros([len(lines),len(lines[0].strip())],dtype=np.int)
        for i,l in enumerate(lines):
            height_map[i,:] = [int(num) for num in l.strip()]
    
    print(height_map)
    padded_map = np.pad(height_map,1,constant_values=height_map.max()+1)
    print(padded_map)
    shift_up    = np.roll(padded_map,+1,axis=0)
    shift_down  = np.roll(padded_map,-1,axis=0)
    shift_right = np.roll(padded_map,+1,axis=1)
    shift_left  = np.roll(padded_map,-1,axis=1)

    danger_map = np.where(np.logical_and(\
        np.logical_and(padded_map < shift_up, padded_map < shift_down) \
        ,np.logical_and(padded_map < shift_left, padded_map < shift_right)),True,False)
    danger_map = danger_map[1:-1,1:-1]
    print(danger_map)
    danger_points = height_map[danger_map]
    print(danger_points)
    print(f"The sum of risk levels is {(danger_points+1).sum()}")

if(__name__=="__main__"):
    main()