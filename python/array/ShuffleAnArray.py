import random
import math

class Solution:
    original = None
    n = None

    def __init__(self, nums):
        self.original = nums
        self.n = len(nums)

    def reset(self):
        return self.original
    
    def shuffle(self):
        shuffled = self.original
        l = self.n
        i = l - 1
        while i>=0:
            j = random.randint(0,200000) % l
            temp = shuffled[i]
            shuffled[i] = shuffled[j]
            shuffled[j] = temp
            l -= 1
            i -= 1

        return shuffled

def update_freq_count(shuffled, all_shuffles, shuffle_counts):
    for i in range(len(all_shuffles)):
        if all_shuffles[i] == shuffled:
            shuffle_counts[i] += 1
            return

def calc_frequencies(shuffle_counts, shuffle_frequencies, total_tries):
    for i in range(len(shuffle_frequencies)):
        shuffle_frequencies[i] = shuffle_counts[i] / total_tries

def main():
    nums_to_shuffle = []
    nums_to_shuffle.append(1)
    nums_to_shuffle.append(2)
    nums_to_shuffle.append(3)
    total_tries = 1200
    sol= Solution(nums_to_shuffle)

    all_shuffles = [ [1, 2, 3], 
                    [1, 3, 2], 
                    [2, 1, 3], 
                    [2, 3, 1], 
                    [3, 1, 2], 
                    [3, 2, 1] ]

    shuffle_counts = [0, 0, 0, 0, 0, 0]
    shuffle_frequencies = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    shuffled = []

    for call in range(total_tries):
        shuffled = sol.shuffle()
        update_freq_count(shuffled, all_shuffles, shuffle_counts)

    calc_frequencies(shuffle_counts, shuffle_frequencies, (total_tries*1.0))


    print ("Input array: " + str(nums_to_shuffle) + ", shuffled " + str(total_tries) + " times.\n")

    print ("Permutation | Occurrences | Frequency")

    for i in range(len(all_shuffles)):
        print(all_shuffles[i], end="")
        print( "   |\t" + '{0:3d}'.format(shuffle_counts[i]) + " times | " + str("{:.2f}".format(shuffle_frequencies[i] * 100)) + "%")

if __name__ == "__main__":
    main()