'''Here is the code for moving all zeros to the beginning of the array. The time complexity is O(n) and the space complexity is O(1).'''
def move_zeros_to_left(nums):
  i = len(nums) - 1
  j = i
  while i >= 0:
    if nums[i]:
      nums[j]=nums[i]
      j-=1
    i-=1
  while j>=0:
    nums[j] = 0
    j-=1
  return nums

'''Here is the driver code for moving all zeros to the beginning of the array. To test the algorithm'''
def main():
    nums_list = [[1, 10, 20, 0, 59, 63, 0, 88, 0], [
        1, 0, 2, 3, 0], [0], [-1, 0, 0, -2, 9], [1, 2, 3, 4, 5], [2]]

    for i in range(len(nums_list)):
        print(str(i + 1) + ". Before list:\t", nums_list[i])
        move_zeros_to_left(nums_list[i])
        print("   After list:\t", nums_list[i])
        print("----------------------------------------------------------------------------------------------------\n")


if __name__ == '__main__':
    main()