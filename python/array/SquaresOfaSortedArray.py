'''Here is the code for sorting an array of integers. The time complexity is O(n) and the space complexity is O(1).'''
def sorted_squares(nums):
  l = 0
  r = len(nums)-1
  result = [0] * (r+1)
  i=r
  while i>=0:
    num = 0
    if abs(nums[r]) > abs(nums[l]):
      num=nums[r]
      r-=1
    else:
      num = nums[l]
      l+=1
    result[i]=num*num
    i-=1
  return result

'''Here is the driver code for sorting an array of integers. To test the algorithm.'''

def main():
    nums = [[-4, -1, 0, 3, 10], [-7, -3, 2, 3, 11], [-100, 100], [-5], [5]]

    for i in range(len(nums)):
        result = sorted_squares(nums[i])
        print(str(i+1) + ".\tInput array:   " + str(nums[i]))
        print("\tSquared array: " + str(result))
        print("---------------------------------------------------------------------------------------------------\n")


if __name__ == "__main__":
    main()