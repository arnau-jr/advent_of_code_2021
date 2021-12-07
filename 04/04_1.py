import numpy as np

class board():
    def __init__(self,init_nums = np.zeros([5,5],dtype=np.int),dimensions=5):
        self.dimensions = dimensions
        self.numbers = init_nums
        self.marked = np.zeros_like(self.numbers)


    def mark_number(self,num):
        mask = np.where(self.numbers == num,1,0)
        self.marked = self.marked + mask
        
    def is_winner(self):
        rows_sum = self.marked.sum(0)
        columns_sum = self.marked.sum(1)

        if(np.any(rows_sum==5) or np.any(columns_sum==5)):
            return True
        else:
            return False

    def sum_of_unmarked(self):
        mask = np.where(self.marked==0,1,0)
        return np.sum(mask*self.numbers)

    def final_score(self,winner_num):
        return self.sum_of_unmarked()*winner_num


def main():
    with open("input.txt","r") as file:
        drawn_numbers = file.readline()
        drawn_numbers = drawn_numbers.split(",")
        drawn_numbers = [int(i) for i in drawn_numbers]
        file.readline()

        boards = []
        j = 0
        while(True):
            try:
                numbers = np.zeros([5,5],dtype=np.int)
                for i in range(5):
                    line = file.readline()
                    line = line.strip().split(" ")
                    line = [i for i in line if i]
                    for l in range(5):
                        numbers[i,l] = int(line[l])
            except IndexError:
                break

            newboard = board(init_nums=numbers)
            boards.append(newboard)

            for i in range(boards[j].dimensions):
                print(boards[j].numbers[i,:])

            print("")
            file.readline()
            j += 1
    
    print(drawn_numbers)
    print("Turn ",0)
    for j in range(len(boards)):
        print("Board ",j+1)
        for i in range(boards[j].dimensions):
            print(boards[j].numbers[i,:])
        print("")

    for num in drawn_numbers:
        print("Turn ",num)
        for j in range(len(boards)):
            boards[j].mark_number(num)
            if(boards[j].is_winner()):
                print(f"Board {j+1} won with {boards[j].final_score(num)} points.")
                return
            print("Board ",j+1)
            for i in range(boards[j].dimensions):
                print(boards[j].marked[i,:])
            print("")
    print("")
if(__name__=="__main__"):
    main()