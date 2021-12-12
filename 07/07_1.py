import numpy as np


def get_fuel_cost(crabs,pos):
    diff = np.abs(crabs - pos)
    return diff.sum()

def main():
    # crabs = np.array([16,1,2,0,4,2,7,1,2,14],dtype=np.int)
    with open("input.txt","r") as file:
        crabs = file.readline()
        crabs = crabs.split(",")
        crabs = [int(i) for i in crabs]
        crabs = np.array(crabs)
        
    costs = []
    for i in range(crabs.min(),crabs.max()+1):
        costs.append(get_fuel_cost(crabs,i))
    costs = np.array(costs)

    print(f"Minimum fuel cost is {costs.min()} for position {np.where(costs == np.amin(costs))[0][0]}")




if(__name__=="__main__"):
    main()