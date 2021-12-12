import numpy as np


def main():
    patterns = []
    output_values = []
    with open("input.txt","r") as file:
        lines = file.readlines()
        for l in lines:
            l = l.strip().split("|")
            patt = l[0].strip().split(" ")
            out = l[1].strip().split(" ")
            for p in patt: patterns.append(p)
            for o in out: output_values.append(o)
        print(output_values)
    lenght_of_outputs = np.array([len(val) for val in output_values])
    print(lenght_of_outputs)
    unique_count = 0    
    for l in lenght_of_outputs:
        if(l==2 or l==3 or l==4 or l==7):
            unique_count += 1
    
    print(f"Number of unique segment count: {unique_count}")

if(__name__=="__main__"):
    main()