'''Here is the code for binary search on a rotated array. The time complexity is O(logn) and the space complexity is O(1).'''
def binary_search_rotated(nums, target):
  low = 0
  high = len(nums)-1
  if low>=high:
    return -1
  while low < high:
    mid = low + (high-low)//2
    if target == nums[mid]:
      return mid
    if nums[low] <= nums[mid]:
      if target < nums[mid] and target >= nums[low]:
        high = mid - 1
      else:
        low = mid + 1
    else:
      if target < nums[mid] and target <= nums[high]:
        low = mid - 1
      else:
        high = mid + 1
  return -1

'''Here is the driver code for binary search on a rotated array. To test the algorithm, we have 5 test cases.'''
def main():
    target_list = [3, 6, 3, 6,7]
    nums_list = [[6, 7, 1, 2, 3, 4, 5], [6, 7, 1, 2, 3, 4, 5],
                 [4, 5, 6, 1, 2, 3], [4, 5, 6, 1, 2, 3], [4, 5, 6, 1, 2, 3]]

    for i in range(len(target_list)):
        print(str(i + 1) + ". Rotated array: ", nums_list[i])
        print("   target", target_list[i],  "found at index " +
              str(binary_search_rotated(nums_list[i], target_list[i])))
        print("-"*100)

if __name__ == '__main__':
    main()