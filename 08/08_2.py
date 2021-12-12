import numpy as np

def get_mapping(patt,l_patt):
    order = np.argsort(l_patt)
    print(l_patt[order])
    print(patt[order])
    patt = patt[order]
    print(patt[1][1] in patt[0])
    mapping = ['x' for i in range(7)]
    for i in range(3):
        if(not patt[1][i] in patt[0]):
            mapping[0] = patt[1][i]

    return

def main():
    patterns = []
    output = []
    with open("input.txt","r") as file:
        lines = file.readlines()
        for l in lines:
            l = l.strip().split("|")
            patt = l[0].strip().split(" ")
            out = l[1].strip().split(" ")
            patterns.append(patt)
            output.append(out)
        patterns = np.array(patterns)
        output = np.array(output)

    get_mapping(patterns[0], np.array([len(val) for val in patterns[0]]))

if(__name__=="__main__"):
    main()