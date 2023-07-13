'''Here is the code to find the low index of a key in a sorted array. The time complexity is O(logn) and the space complexity is O(1).'''
def find_low_index(arr, key):
    low = 0
    high = len(arr) - 1
    mid = high // 2
    while low <= high:
        mid_elem = arr[mid]
        if mid_elem < key:
            low = mid + 1
        else:
            high = mid - 1
        mid = low + (high - low) // 2
    if low < len(arr) and arr[low] == key:
        return low
    return -1

'''Here is the code to find the high index of a key in a sorted array. The time complexity is O(logn) and the space complexity is O(1).'''
def find_high_index(arr, key):
    low = 0
    high = len(arr) - 1
    mid = high // 2
    while low <= high:
        mid_elem = arr[mid]
        if mid_elem <= key:
            low = mid + 1
        else:
            high = mid - 1
        mid = low + (high - low) // 2
    if high == -1:
        return high
    if high < len(arr) and arr[high] == key:
        return high
    return -1
'''Here is the driver code for finding the low and high index of a key in a sorted array. To test the algorithm.'''

def main():
    nums = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3,
            4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
    target_list = [5,-2]
    print("Original List: " + str(nums) + "\n")
    for i in range(len(target_list)):    
        low = find_low_index(nums, target_list[i])
        high = find_high_index(nums, target_list[i])
        print("Low Index of " + str(target_list[i]) + ": " + str(low))
        print("High Index of " + str(target_list[i]) + ": " + str(high) + "\n")

if __name__ == '__main__':
    main()