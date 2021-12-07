import numpy as np

#Uses old method
def old_lanterfish_step(timers):
    timers += -1 #Decrease timers
    new_lanternfish = np.count_nonzero(timers==-1) #Count new fish to be created
    # new_lanternfish = np.where(timers==-1,1,0).sum() #Count new fish to be created
    new_timers = 8*np.ones(new_lanternfish,dtype=np.int)
    timers = np.where(timers==-1,6,timers) #Reset timers
    # timers = np.append(timers,[8 for i in range(new_lanternfish)]) #Add fish
    timers = np.concatenate((timers, new_timers))
    return timers

def lanterfish_step(timer_count):
    resetted_lanternfish = timer_count[0]
    timer_count = np.roll(timer_count, -1)
    timer_count[6] += resetted_lanternfish
    return timer_count

def main():
    # input_timers = np.array([3,4,3,1,2],dtype=np.int)
    # timer_count = np.array([np.count_nonzero(input_timers==i) for i in range(9)])
    with open("input.txt","r") as file:
        timers = file.readline()
        timers = timers.strip().split(",")
        timers = [int(i) for i in timers]
        timers = np.array(timers)
        timer_count = np.array([np.count_nonzero(timers==i) for i in range(9)])
    print(f"Step 0: {timer_count}")

    N_steps = 256
    for step in range(1,N_steps+1):
        timer_count = lanterfish_step(timer_count)
        print(f"Step {step}: {timer_count} | Total fish: {timer_count.sum()}")
    print(f"Final number of fish: {timer_count.sum()}")

if(__name__=="__main__"):
    main()