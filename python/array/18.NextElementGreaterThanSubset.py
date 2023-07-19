# import stack
def next_greater_element(nums1, nums2):
    
    stack = []
    map = {}
    for num in nums2:
        while stack and stack[-1] < num:
            map[stack.pop()] = num
        stack.append(num)
        
    for i in range(len(nums1)):
        nums1[i] = map.get(nums1[i], -1)


    return nums1

def main():
    # Driver code

    # Example 1
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print("1. Input arrays:  ")
    print("  ", nums1)
    print("  ", nums2)
    print("   Output:  ")
    print("  ", next_greater_element(nums1, nums2))
    print("-----------------------------------------------------------------------------------------------------\n")

    # Example 2
    nums1 = [4, 1, 2, 3]
    nums2 = [1, 3, 4, 2, 5]
    print("2. Input arrays:  ")
    print("  ", nums1)
    print("  ", nums2)
    print("   Output:  ")
    print("  ", next_greater_element(nums1, nums2))
    print("-----------------------------------------------------------------------------------------------------\n")

    # Example 3
    nums1 = [3, 4, 5]
    nums2 = [5, 4, 3, 2, 1]
    print("3. Input arrays:  ")
    print("  ", nums1)
    print("  ", nums2)
    print("   Output:  ")
    print("  ", next_greater_element(nums1, nums2))
    print("-----------------------------------------------------------------------------------------------------")


if __name__ == '__main__':
    main()