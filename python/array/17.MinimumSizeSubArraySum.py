def min_sub_array_len(target, nums):
	left = 0
	sum1 = 0
	result = float('inf')
	for i in range(len(nums)):
		sum1 += nums[i]
		while sum1>= target:
			result = min(result,(i+1) - left)
			sum1 -= nums[left]
			left+=1
	if result == float('inf'):
		return 0
	return result

def main():
    s_list = [7, 4, 11]
    nums_list = [[2,3,1,2,4,3], [1,4,4], [1,1,1,1,1,1,1,1]]
    for i in range(len(nums_list)):
        result = min_sub_array_len(s_list[i], nums_list[i])
        print(str(i+1) + ". min_sub_array_len(" + str(s_list[i]) + ", " + str(nums_list[i]) + "): " + str(result))
        print("-------------------------------------------------------------------------------------------------\n");

if __name__ == "__main__":
    main()