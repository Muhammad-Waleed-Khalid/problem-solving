'''Here is the code for finding the first missing positive integer in an array. The time complexity is O(nlogn) and the space complexity is O(1).'''
def first_missing_positive(nums):
    i = 0
    while i < len(nums):
        if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        else:
            i += 1
    i = 0
    while i < len(nums):
        if nums[i] != i+1:
            return i+1
        else:
            i += 1
    return len(nums)+1

'''Here is code for finding the first missing positive integer in an array. The time complexity is O(n) and the space complexity is O(1).'''
def first_missing_positive_without_sorting(nums):
    n = len(nums)
    i = 0
    while i<n:
        if nums[i]>0 and nums[i]<=n and nums[nums[i]-1]!=nums[i]:
            nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
        else:
            i+=1
    for i in range(n):
        if nums[i]!=i+1:
            return i+1
    return n+1

# Driver Code
def main():
    nums_list = [[5, 8, 2, 7, 1, 6, 3], [0, 5, 1, 3, 2, 4]]
    for i in range(len(nums_list)):
        print(str(i+1) + ". The smallest missing positive integer in", nums_list[i],"is: ", end = "")
        print(first_missing_positive(nums_list[i]))
        print("---------------------------------------------------------------------------------------------------\n")

if __name__ == '__main__':
    main()