import numpy as np

def main():
    with open("test.txt","r") as file:
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
    danger_points = height_map[danger_map]

    peak_map = np.where(height_map==height_map.max(),True,False)
    basin_map = danger_map.copy()
    converged = False
    while(not converged):
        old = basin_map.copy()
        for i in range(basin_map.shape[0]):
            for j in range(basin_map.shape[1]):
                if(basin_map[i,j]):
                    if(i == basin_map.shape[0]-1 and j != basin_map.shape[1]-1):
                        if(not peak_map[i-1,j]): basin_map[i-1,j] = True
                        if(not peak_map[i,j+1]): basin_map[i,j+1] = True
                        if(not peak_map[i,j-1]): basin_map[i,j-1] = True
                    elif(i == 0 and j != basin_map.shape[1]-1):
                        if(not peak_map[i+1,j]): basin_map[i+1,j] = True
                        if(not peak_map[i,j+1]): basin_map[i,j+1] = True
                        if(not peak_map[i,j-1]): basin_map[i,j-1] = True
                    elif(i != basin_map.shape[0]-1 and j == basin_map.shape[1]-1):
                        if(not peak_map[i+1,j]): basin_map[i+1,j] = True
                        if(not peak_map[i-1,j]): basin_map[i-1,j] = True
                        if(not peak_map[i,j-1]): basin_map[i,j-1] = True
                    elif(i != basin_map.shape[0]-1 and j == 0):
                        if(not peak_map[i+1,j]): basin_map[i+1,j] = True
                        if(not peak_map[i-1,j]): basin_map[i-1,j] = True
                        if(not peak_map[i,j+1]): basin_map[i,j+1] = True
                    elif(i == 0 and j == 0):
                        if(not peak_map[i+1,j]): basin_map[i+1,j] = True
                        if(not peak_map[i,j+1]): basin_map[i,j+1] = True                
                    elif(i == basin_map.shape[0]-1 and j == basin_map.shape[1]-1):
                        if(not peak_map[i-1,j]): basin_map[i-1,j] = True
                        if(not peak_map[i,j-1]): basin_map[i,j-1] = True
                    else:
                        if(not peak_map[i+1,j]): basin_map[i+1,j] = True
                        if(not peak_map[i-1,j]): basin_map[i-1,j] = True
                        if(not peak_map[i,j+1]): basin_map[i,j+1] = True
                        if(not peak_map[i,j-1]): basin_map[i,j-1] = True
        if(np.all(old==basin_map)):
            converged = True

    print(basin_map)
    basin_sizes = np.zeros([danger_points.size])
    print(danger_points)
    print(f"The sum of risk levels is {(danger_points+1).sum()}")

if(__name__=="__main__"):
    main()