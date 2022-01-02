import numpy as np

def extend_chain(chain,rules):
    new_chain = chain
    offset = 0
    for i in range(0,len(chain)-1):
        segment = chain[i:i+2]
        new_element = rules[segment]
        new_chain = add_to_string(new_chain, new_element, i+1+offset)
        offset += 1
    return new_chain

def add_to_string(s,a,pos):
    s = s[:pos]+a+s[pos:]
    return s

def count_elements(chain):
    counts = {}

    for c in chain:
        counts[c] = chain.count(c)
    return counts

def main():
    with open("input.txt","r") as file:
        lines = file.readlines()

        chain = lines[0].strip()
        chain_rules = {}
        for line in lines[2:]:
            # line = line.strip().split("->")
            line = line.strip().split("-&gt;")
            chain_rules[line[0].strip()] = line[1].strip()
    
    print(f"Template: {chain}")
    N_steps = 40
    for i in range(N_steps):
        chain = extend_chain(chain, chain_rules)
        # print(f"Step {i+1}: {chain}")
        print(f"Step {i+1}")
    counts = count_elements(chain)
    print(counts)
    c_values = np.array(list(counts.values()))
    print(f"Maximum ocurrence is {c_values.max()}")
    print(f"Minimum ocurrence is {c_values.min()}")
    print(f"Difference: {c_values.max()- c_values.min()}")

if(__name__=="__main__"):
    main()