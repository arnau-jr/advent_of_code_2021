import numpy as np

def get_most_common_bits(data):
    acu = [0 for i in range(len(data[0]))]

    for i in range(len(data)):
        for j in range(len(acu)):
            acu[j] += int(data[i][j])
    most_common_bits = []
    least_common_bits = []
    for j in range(len(acu)):
        if(acu[j]>len(data)/2):
            most_common_bits.append(1)
            least_common_bits.append(0)
        else:
            most_common_bits.append(0)
            least_common_bits.append(1)
    return most_common_bits,least_common_bits

def main():
    with open("input.txt","r") as file:
        lines = file.readlines()
    data = []

    for l in lines:
        data.append(l[:-1])

    gamma_rate_bin,epsilon_rate_bin = get_most_common_bits(data)

    print(gamma_rate_bin,epsilon_rate_bin)

    gamma_rate = 0
    epsilon_rate = 0
    for i in range(0,len(gamma_rate_bin)):
        gamma_rate += gamma_rate_bin[-(i+1)]*2**i
        epsilon_rate += epsilon_rate_bin[-(i+1)]*2**i
    power_consumption = gamma_rate*epsilon_rate

    print(gamma_rate,epsilon_rate)
    print(f"Power consumption is {power_consumption}")
if(__name__=="__main__"):
    main()