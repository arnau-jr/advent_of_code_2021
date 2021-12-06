import numpy as np

def bin_to_float(binary):
    num = 0
    for i in range(len(binary)):
        num += int(binary[-(i+1)])*2**i
    return num

def get_most_common_bits(data):
    acu = [0 for i in range(len(data[0]))]

    for i in range(len(data)):
        for j in range(len(acu)):
            acu[j] += int(data[i][j])
    most_common_bits = []
    least_common_bits = []
    for j in range(len(acu)):
        if(acu[j] >= len(data)/2):
            most_common_bits.append(1)
            least_common_bits.append(0)
        else:
            most_common_bits.append(0)
            least_common_bits.append(1)
    return most_common_bits,least_common_bits

def get_oxygen_gen_rating(data,j=0):
    mcb,lcb = get_most_common_bits(data)
    new_data = []
    for i in range(len(data)):
        if(int(data[i][j]) == mcb[j]):
            new_data.append(data[i])

    if(len(new_data)==1):
        oxygen_rating = new_data[0]
        return oxygen_rating
    else:
        j += 1
        oxygen_rating = get_oxygen_gen_rating(new_data,j)
        return oxygen_rating


def get_co2_scrub_rating(data,j=0):
    mcb,lcb = get_most_common_bits(data)
    new_data = []
    for i in range(len(data)):
        if(int(data[i][j]) == lcb[j]):
            new_data.append(data[i])

    if(len(new_data)==1):
        co2_rating = new_data[0]
        return co2_rating
    else:
        j += 1
        co2_rating = get_co2_scrub_rating(new_data,j)
        return co2_rating

def main():
    with open("input.txt","r") as file:
        lines = file.readlines()
    data = []

    for l in lines:
        data.append(l[:-1])

    oxygen_rating = bin_to_float(get_oxygen_gen_rating(data))
    co2_rating = bin_to_float(get_co2_scrub_rating(data))
    print(oxygen_rating,co2_rating)
    print(f"Life support rating is {oxygen_rating*co2_rating}")
if(__name__=="__main__"):
    main()