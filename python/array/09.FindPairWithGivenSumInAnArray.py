'''Here is the code for finding a pair with a given sum in an array. The time complexity is O(n) and the space complexity is O(n).'''
def find_sum_of_two(nums, val):
  hashmap = {}
  for i in nums:
    if i in hashmap:
      hashmap[i] += 1
    else:
      hashmap[i] = 1
  for i in range(len(nums)):
    target = val - nums[i]
    count = hashmap.get(target)
    if count != None:
      if target == nums[i] and count > 2:
        return True
      if target != nums[i]:
        return True
  return False


'''Solution for only Sorted Array, The time complexity is O(nlogn) and the space complexity is O(1).'''
def find_sum_of_two_sorted(nums, val):
    nums = sorted(nums)
    low = 0
    high = len(nums) - 1
    while low < high:
        s = nums[low] + nums[high]
        if s == val:
            return True
        elif s < val:
            low += 1
        else:
            high -= 1
    return False

'''Here is the driver code for finding a pair with a given sum in an array. To test the algorithm'''
def main():
    v = [5, 7, 1, 2, 8, 4, 3]
    test = [3, 20, 1, 2, 7]

    for i in range(len(test)):
        output = find_sum_of_two(v, test[i])
        print(str(i + 1) + ". find_sum_of_two(" + str(v) +
              ", " + str(test[i]) + ") = " + str(output))
        print("----------------------------------------------------------------------------------------------------\n")


if __name__ == '__main__':
    main()