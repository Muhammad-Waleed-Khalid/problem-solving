'''Here is the code for finding a pair with a given sum in an array. The time complexity is O(n) and the space complexity is O(n).'''
def find_sum_of_two(A, val):
  hash_map = {}
  for i in range(len(A)):
    if A[i] in hash_map:
      return True
    else:
      hash_map[val - A[i]] = A[i]
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