''' Here is the code for binary search on a sorted array. The time complexity is O(logn) and the space complexity is O(1).'''


def binary_search(nums, target):
	low = 0
	high = len(nums) - 1
	while low <= high:
		mid = low + ((high - low) // 2)
		if nums[mid] == target:
			return mid
		elif target < nums[mid]:
			high = mid - 1
		elif target > nums[mid]:
			low = mid + 1
	return -1

''' Here is the recursive code for binary search on sorted array. The time complexity is O(logn) and the space complexity is O(logn).'''
def binary_search_rec(nums, target, low, high):
	if low > high:
		return -1

	mid = (low + high) // 2
	if target == nums[mid]:
		return mid
	return binary_search_rec(nums, target, low if nums[mid]>target  else mid+1 ,
	 mid-1 if nums[mid]>target else high)

def binary_search_rec_driver(nums, target):
  	return binary_search_rec(nums, target, 0, len(nums) - 1)


'''Here is the driver code for binary search on a sorted array. To test the algorithm, we have 5 test cases.'''


def main():
	nums_lists = [[], [0,1], [1,2,3], [-1,0,3,5,9,12], [-1,0,3,5,9,12]]
	target_list = [12, 1, 3, 9, 2]
	for i in range(len(nums_lists)):
		nums = nums_lists[i]
		target = target_list[i]
		index = binary_search(nums, target)
		print(str(i+1) + ". Array to search: " + str(nums))
		print("   Target: " + str(target))
		if index != -1:
			print("   " + str(target) + " exists in the array at index", index)
		else:
			print("   " + str(target) + " does not exist in the array so the return value is", index)
		print("----------------------------------------------------------------------------------------------------\n")

if __name__ == '__main__':
		main()