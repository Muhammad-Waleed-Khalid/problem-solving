def rotate_array(nums, n):
	def reverse_array(nums, s,e):
		while(s<e):
			nums[s],nums[e] = nums[e],nums[s]
			s+=1
			e-=1
		return nums

	l = len(nums)
	n = n%l
	nums = reverse_array(nums,0,l-1)
	nums = reverse_array(nums,0,n-1)
	nums = reverse_array(nums,n,l-1)
	return nums

def main():
    arr = [1, 10, 20, 0, 59, 86, 32, 11, 9, 40]
    print("Array Before Rotation")
    print(arr)

    nums = rotate_array(arr, 2)
    print("Array After 2 Rotations")
    print(nums)
if __name__ == '__main__':
    main()