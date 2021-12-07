import numpy as np
def gen_line(r0,r1):
    r = r0.copy()
    points = []
    points.append(r0)
    while(r != r1):
        if(r[0] < r1[0]):
            r[0] += 1
        elif(r[0] > r1[0]):
            r[0] += -1
        elif(r[1] < r1[1]):
            r[1] += 1
        elif(r[1] > r1[1]):
            r[1] += -1
        else:
            print("Error")
        points.append(r.copy())
    return points

def mark_vents(vents,points):
    for p in points:
        vents[p[1],p[0]] += 1
    return vents

def main():

    with open("input.txt","r") as file:
        lines = file.readlines()

    # First index is vertical pos, second is horizontal pos
    vents = np.zeros([1000,1000],dtype=np.int)
    for l in lines:
        # l = l.strip().split("->")
        l = l.strip().split("-&gt;")
        r0 = l[0].split(",")
        r0 = [int(i) for i in r0]
        r1 = l[1].split(",")
        r1 = [int(i) for i in r1]
        print(l,r0,r1)
        if(r0[0]==r1[0] or r0[1]==r1[1]):
            points = np.array(gen_line(r0,r1))
            vents = mark_vents(vents, points)
    print(vents)
    danger_vents = np.where(vents>1,1,0)
    print(f"Total number of dangerous points is {danger_vents.sum()}")

if(__name__=="__main__"):
    main()