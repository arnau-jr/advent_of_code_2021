import numpy as np

with open("input.txt","r") as file:
    lines = file.readlines()
    readings = [int(l) for l in lines]

readings = np.array(readings)
increased = np.where(np.roll(readings,+1)<readings,1,0)
increased[0] = 0

print("The readings increased ", increased.sum()," times")
