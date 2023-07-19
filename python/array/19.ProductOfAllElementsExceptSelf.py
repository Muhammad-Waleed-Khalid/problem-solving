'''Here is the Code for finding the product of all elements except self in an array. The time complexity is O(n) and the space complexity is O(n).'''
def product_except_self(nums):
	answer = [1]*len(nums)
	left = [1]*len(nums)
	right = [1]*len(nums)
	for i in range(1,len(nums)):
		left[i] = nums[i-1]*left[i-1]
	for i in range(len(nums)-2,-1,-1):
		right[i]=nums[i+1]*right[i+1]
	for i in range(len(nums)):
		answer[i]=left[i]*right[i]
	return answer


def main():	
    inputs = [[1, 2, 3, 4], [-1, 1, 0, -3, 3]]

    for i in range(len(inputs)):
        print(str(i+1) + ". Nums:    " , str(inputs[i]))
        res = product_except_self(inputs[i])
        print("   Product: " , str(res))
        print("----------------------------------------------------------------------------------------------------\n")

if __name__ == '__main__':
    main()