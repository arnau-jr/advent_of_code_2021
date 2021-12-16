import numpy as np

def octopus_step(levels):
    levels += 1 #Increase all levels by one
    flashed = []
    someone_flashed = True
    Nflashes = 0

    while(someone_flashed):
        oldNflashes = Nflashes
        flashing = np.where(levels>9)
        for i,j in zip(flashing[0],flashing[1]):
            if((i,j) not in flashed):
                levels = flash(levels,i,j)
                flashed.append((i,j))
                Nflashes +=1
        if(oldNflashes==Nflashes):
            someone_flashed = False

    flashing = np.where(levels>9)
    levels[flashing] = 0
    return levels,Nflashes

def flash(levels,i,j):
    for k in range(-1,2):
        for l in range(-1,2):
            if(not(k==0 and l==0) \
                and not(i+k < 0) and not(j+l < 0)\
                and i+k!=levels.shape[0] and j+l!=levels.shape[1]):
                try:
                    levels[i+k,j+l] += 1
                except IndexError:
                    pass

    return levels

def main():
    levels = np.zeros([10,10],dtype=np.int)
    # levels = np.zeros([5,5],dtype=np.int)
    with open("input.txt","r") as file:
        lines = file.readlines()
        for i,line in enumerate(lines):
            row = [int(l) for l in line.strip()]
            levels[i,:] = np.array(row)
    print("Initial Conditions")
    print(levels)

    totalflashes = 0
    Nsteps = 500
    for i in range(Nsteps):
        levels,Nflashes = octopus_step(levels)
        totalflashes += Nflashes
        print(f"Step {i+1}, {totalflashes} flashes so far")
        if(Nflashes == levels.size): print("Simultaneous Flash!"); break

        # print(levels)

if(__name__=="__main__"):
    main()