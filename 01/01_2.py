import numpy as np

with open("input_1.txt","r") as file:
    lines = file.readlines()
    readings = [int(l) for l in lines]

readings = np.array(readings)
sums = []
for i in range(0,readings.size-2):
    sums.append(readings[i]+readings[i+1] + readings[i+2])

sums = np.array(sums)
increased = np.where(np.roll(sums,+1)<sums,1,0)
increased[0] = 0
print("The readings increased ", increased.sum()," times")