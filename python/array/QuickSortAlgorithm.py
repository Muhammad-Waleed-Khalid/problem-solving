'''Here is the code for quick sort. The time complexity is O(nlogn) and the space complexity is O(1).'''


def partition(nums, low, high):
    pivot_value = nums[low]
    i = low
    j = high

    
    while i<j:
        while i <= j and nums[i] <= pivot_value:
            i += 1
        while nums[j] > pivot_value:
            j-=1

        if i<j:
            nums[i], nums[j] = nums[j], nums[i]
        
    nums[low], nums[j] = nums[j], pivot_value
    
    return j

def quick_sort_helper(nums, low, high):
    if low < high:
        pivot_index = partition(nums, low, high)
        quick_sort_helper(nums, low, pivot_index-1)
        quick_sort_helper(nums, pivot_index+1, high)

def quick_sort(nums):
    quick_sort_helper(nums, 0, len(nums)-1)

def main():
    nums_list = [[55, 23, 26, 2, 18, 78, 23, 8, 2, 3],
                 [1], [9, 8, 7, 2, 3, 1], [10, 20, 30, -1, -2]]
    for i in range(len(nums_list)):
        print(str(i + 1) + ". Before Sorting")
        print("   " + str(nums_list[i]))

        quick_sort(nums_list[i])

        print("   After Sorting")
        print("   " + str(nums_list[i]))
        print("-"*100)


if __name__ == '__main__':
    main()