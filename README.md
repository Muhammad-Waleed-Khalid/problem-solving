<h1> Problem Solving </h1>

Top Problems must be revised before interview
<h2> Table of Contents</h2>

- [Array](#array)
  - [Binary Search On Sorted Array](#binary-search-on-sorted-array)
    - [Iterative Solution Of Binary Search](#iterative-solution-of-binary-search)
      - [Code](#code)
    - [Time Complexity](#time-complexity)
    - [Space Complexity](#space-complexity)
    - [Recursive Solution of Binary Search](#recursive-solution-of-binary-search)
      - [Code](#code-1)
    - [Time Complexity](#time-complexity-1)
    - [Space Complexity](#space-complexity-1)
  - [Rotate An Array By N Elements](#rotate-an-array-by-n-elements)
    - [Problem Statement](#problem-statement)
    - [Example](#example)
    - [Solution](#solution)
    - [Code](#code-2)
    - [Time Complexity](#time-complexity-2)
    - [Space Complexity](#space-complexity-2)
  - [Rotated Binary Search](#rotated-binary-search)
    - [Problem Statement](#problem-statement-1)
    - [Example](#example-1)
    - [Sample Input](#sample-input)
    - [Expected Output](#expected-output)
    - [Solution](#solution-1)
    - [Code](#code-3)
    - [Time Complexity](#time-complexity-3)
    - [Space Complexity](#space-complexity-3)
  - [Smallest Common Number Between Three Arrays](#smallest-common-number-between-three-arrays)
    - [Problem Statement](#problem-statement-2)
    - [Example](#example-2)
    - [Solution](#solution-2)
    - [Code](#code-4)
    - [Time Complexity](#time-complexity-4)
    - [Space Complexity](#space-complexity-4)
  - [Find Low and High Index of a key in sorted array](#find-low-and-high-index-of-a-key-in-sorted-array)
    - [Problem Statement](#problem-statement-3)
    - [Example](#example-3)
    - [Solution](#solution-3)
    - [Code](#code-5)
    - [Time Complexity](#time-complexity-5)
    - [Space Complexity](#space-complexity-5)
  - [Move all Zeros to the beging of the Array](#move-all-zeros-to-the-beging-of-the-array)
    - [Problem Statement](#problem-statement-4)
    - [Example](#example-4)
    - [Solution](#solution-4)
    - [Code](#code-6)
    - [Time Complexity](#time-complexity-6)
    - [Space Complexity](#space-complexity-6)
  - [Best Time to Buy and Sell Stock to Maximize Profit](#best-time-to-buy-and-sell-stock-to-maximize-profit)
    - [Problem Statement](#problem-statement-5)
    - [Example](#example-5)
    - [Solution](#solution-5)
    - [Code](#code-7)
    - [Time Complexity](#time-complexity-7)
    - [Space Complexity](#space-complexity-7)
  - [Merge An Array with Overlapping Intervals](#merge-an-array-with-overlapping-intervals)
    - [Problem Statement](#problem-statement-6)
    - [Example](#example-6)
    - [Solution](#solution-6)
    - [Code](#code-8)
    - [Time Complexity](#time-complexity-8)
    - [Space Complexity](#space-complexity-8)
  - [Find Pair With Given Sum in Array](#find-pair-with-given-sum-in-array)
    - [Problem Statement](#problem-statement-7)
    - [Example](#example-7)
    - [Solution](#solution-7)
    - [Code](#code-9)
    - [Time Complexity](#time-complexity-9)
    - [Space Complexity](#space-complexity-9)
  - [Squares Of a Sorted Array](#squares-of-a-sorted-array)
    - [Problem Statement](#problem-statement-8)
    - [Example](#example-8)
    - [Solution](#solution-8)
    - [Code](#code-10)
    - [Time Complexity](#time-complexity-10)
    - [Space Complexity](#space-complexity-10)
  - [Container With Most Water](#container-with-most-water)
    - [Problem Statement](#problem-statement-9)
    - [Example](#example-9)
    - [Solution](#solution-9)
    - [Code](#code-11)
    - [Time Complexity](#time-complexity-11)
    - [Space Complexity](#space-complexity-11)
  - [Quick Sort Algorithm](#quick-sort-algorithm)
    - [Problem Statement](#problem-statement-10)
    - [Example](#example-10)
    - [Solution](#solution-10)
    - [Code](#code-12)
    - [Time Complexity](#time-complexity-12)
    - [Space Complexity](#space-complexity-12)
  - [Sort Colors](#sort-colors)
    - [Problem Statement](#problem-statement-11)
    - [Example](#example-11)
    - [Solution](#solution-11)
    - [Code](#code-13)
    - [Time Complexity](#time-complexity-13)
    - [Space Complexity](#space-complexity-13)
  - [Arrange The Largest Number](#arrange-the-largest-number)
    - [Problem Statement](#problem-statement-12)
    - [Example](#example-12)
    - [Solution](#solution-12)
    - [Code](#code-14)
    - [Time Complexity](#time-complexity-14)
    - [Space Complexity](#space-complexity-14)
  - [Shuffle Array](#shuffle-array)
    - [~~Incomplete~~](#incomplete)
  - [First Missing Positive Integer](#first-missing-positive-integer)
    - [Problem Statement](#problem-statement-13)
    - [Example](#example-13)
    - [Solution](#solution-13)
    - [Code](#code-15)
    - [Time Complexity](#time-complexity-15)
    - [Space Complexity](#space-complexity-15)
  - [Minimum Size Subarray Sum](#minimum-size-subarray-sum)
    - [Problem Statement](#problem-statement-14)
    - [Example](#example-14)
    - [Solution](#solution-14)
    - [Code](#code-16)
    - [Time Complexity](#time-complexity-16)
    - [Space Complexity](#space-complexity-16)
  - [Next Element Greater Than Subset](#next-element-greater-than-subset)
    - [Problem Statement](#problem-statement-15)
    - [Example](#example-15)
    - [Solution](#solution-15)
    - [Code](#code-17)
    - [Time Complexity](#time-complexity-17)
    - [Space Complexity](#space-complexity-17)
  - [Product of All Elements Except Itself in an Array](#product-of-all-elements-except-itself-in-an-array)
    - [Problem Statement](#problem-statement-16)
    - [Example](#example-16)
    - [Solution](#solution-16)
    - [Code](#code-18)
    - [Time Complexity](#time-complexity-18)
    - [Space Complexity](#space-complexity-18)
- [Linked-List](#linked-list)
- [Math-\&-Stats](#math--stats)
- [Strings](#strings)
- [Trees](#trees)
- [Stack-\&-Queues](#stack--queues)
- [Graph](#graph)
- [Back-Tracking](#back-tracking)
- [Dynamic-Programming](#dynamic-programming)
- [Miscellaneous](#miscellaneous)

## Array 
### Binary Search On Sorted Array
  Binary Search is the most efficient way to search in Sorted array.  
  **Time Complexity :** O(*log*n)  
  **Space Complexity :** O(1) (iterative Solution), O(*log*n) recursive Solution
  #### Iterative Solution Of Binary Search
  1. first initialize two variables (low,high) with 0 and length of array
  2. start a loop which ends when low becomes equal or greater than high
     1. initialize a variable mid which will be the mid value of low and high, you can get using (low+mid)/2 but a better way to avoid overflow or underflow we should low + (high-low)/2
     2. than check if nums[mid] is equal to our target value 
     3. [true] return with the mid index
     4. [false]else if than check if nums[mid] is greater than target
     5. [true] set high variable with mid -1
     6. [false] else if than check if nums[mid] is smaller than target
     7. [true] set low variable with mid + 1
  3. return -1 index  ***it means element is not present in array***  
  
  ##### Code
  ```
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
  ```
#### Time Complexity
    O(*log*n) where n is the length of array
 #### Space Complexity
    O(1) no extra space is used
  #### Recursive Solution of Binary Search
  
  1. check base case (low is greater or equal to high)  if true return -1 // it means target is not present in array
  2. calculate mid index of low and high use **mid = low+high/2** or **mid = low+(high-low)/2**
  3. check if nums[mid] equal to target
  4. [true] **HURRAH!** (we found the element in array) return mid
  5. [False] check if nums[mid] smaller to target
  ##### Code
  ```
    def binary_search_rec(nums,target,low, high):
        if low>=high:
            return -1
        mid = low + (high-low)/2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return binary_search_rec(nums,target, low, mid-1)
        else:
            return binary_search_rec(nums,target, mid+1, low)
  ```
#### Time Complexity
    O(*log*n) where n is the length of array
#### Space Complexity
    O(*log*n) recursive stack space is used
### Rotate An Array By N Elements
#### Problem Statement
We’re given an array of integers, nums. Rotate the array by n elements, where n is an integer:  
  
- For positive values of n, perform a right rotation.
- For negative values of n, perform a left rotation.
Make sure we make changes to the original array.
#### Example 
**Original Array**
<table border=1>
<tr> <td>0 </td><td>  1 </td><td>  2 </td><td>  3 </td><td>  4 </td><td>  5 </td><td>  6 </td><td>  7 </td><td>  8 </td><td>  9</td></tr>
<tr> <td>1 </td><td>  10 </td><td> 20 </td><td> 0  </td><td> 59 </td><td> 86 </td><td> 32 </td><td> 11 </td><td> 9  </td><td> 40</td></tr>
</table>

**After Rotation if N=3**
<table border=1>
<tr> <td>0 </td><td>  1 </td><td>  2 </td><td>  3 </td><td>  4 </td><td>  5 </td><td>  6 </td><td>  7 </td><td>  8 </td><td>  9</td></tr>
<tr> <td> 11 </td><td> 9  </td><td> 40</td><td>1 </td><td>  10 </td><td> 20 </td><td> 0  </td><td> 59 </td><td> 86 </td><td> 32 </td></tr>
</table>

**After Rotation from Original if N= -2**
<table border=1>
<tr> <td>0 </td><td>  1 </td><td>  2 </td><td>  3 </td><td>  4 </td><td>  5 </td><td>  6 </td><td>  7 </td><td>  8 </td><td>  9</td></tr>
<tr> <td>20 </td><td> 0  </td><td> 59 </td><td> 86 </td><td> 32 </td><td> 11 </td><td> 9  </td><td> 40</td><td>1 </td><td>  10 </td></tr>
</table>

***Sample Input***
```
nums = [2, 13, 15, 1, 0, 4]
n = 2
```

***Expected Output***  
``` 
[0, 4 ,2, 13, 15, 1] 
```

#### Solution
 1. Write a function to reverse Array from a index to b index
 2. get length of array ```l```
 3. normalize ```N``` by taking modulus by length ```N=N%l```
 4. reverse array nums from 0 index to l-1  complete reverse
 5. reverse array nums from 0 index to n-1
 6. reverse array nums from n index to l-1
 7. return nums

#### Code
```    
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
```
#### Time Complexity
    O(n) where n is length of array
#### Space Complexity
    O(1) no extra space is used

### Rotated Binary Search

#### Problem Statement
We’re given a sorted integer array, ```array``` and an integer value, ```key```. The array is rotated by some arbitrary number. Search the ```target``` in this array. If the target does not exist then return -1.

#### Example
<table border=1>
<tr> <td>0 </td><td>  1 </td><td>  2 </td><td>  3 </td><td>  4 </td><td>  5 </td><td>  6 </td><td>  7 </td><td>  8 </td><td>  9</td></tr>
<tr> <td>13</td><td>  14</td><td>  20</td><td> 0  </td><td> 2 </td><td> 3 </td><td> 5 </td><td> 7 </td><td> 8  </td><td> 11</td></tr>
</table>

#### Sample Input
```
array = [13, 14, 20, 0, 2, 3, 5, 7, 8, 11]
key = 20
```

#### Expected Output
```
2
```

#### Solution
 1. initialize low = 0 and high = length of array -1
 2. if low is greater than high return -1
 3. start loop till low is less than or equal to high
    1. initialize mid = low + (high-low)/2 we can also do mid = (low+high)/2 but this can cause overflow
    2. check if array[mid] is equal to key if yes return mid
    3. else check id array[low] is less than or equal to array[mid] if yes then
        1. check if key is greater than array[low] and key is less than array[mid] if yes then  set high = mid-1
        2. else set low = mid+1
    4. else
        1. check if key is greater than array[mid] and key is less than array[high] if yes then set low = mid+1
        2. else set high = mid-1
 4. return -1

#### Code
```
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
``` 
#### Time Complexity
    O(logn) where n is length of array
#### Space Complexity
    O(1) no extra space is used

### Smallest Common Number Between Three Arrays

#### Problem Statement
Given three integer arrays sorted in ascending order, find the smallest number that is common in all three arrays. For example, let's look at the below three arrays. Here 6 is the smallest number that's common in all the arrays.

#### Example
```
Input: [6, 7, 10, 25, 30, 63, 64], [0, 4, 5, 6, 7, 8, 50], [1, 6, 10, 14]
Output: 6
```

#### Solution
    1. initialize i=0, j=0, k=0
    2. start loop till i is less than length of array1 and j is less than length of array2 and k is less than length of array3
        1. check if array1[i] is equal to array2[j] and array2[j] is equal to array3[k] if yes then return array1[i]
        2. else check if array1[i] is less than array2[j] and array1[i] is less than array3[k] if yes then increment i
        3. else check if array2[j] is less than array1[i] and array2[j] is less than array3[k] if yes then increment j
        4. else increment k
    3. return -1
#### Code
```
def find_least_common_number(a, b, c):
    i = 0
    j = 0
    k = 0
    while i < len(a) and j < len(b) and k < len(c):
        if a[i] == b[j] and b[j] == c[k]:
            return a[i]
        elif a[i] <= b[j] and a[i] <= c[k]:
            i += 1
        elif b[j] <= a[i] and b[j] <= c[k]:
            j += 1
        elif c[k] <= a[i] and c[k] <= b[j]:
            k += 1
    return -1
```

#### Time Complexity
    O(n) where n is length of array
#### Space Complexity
    O(1) no extra space is used


### Find Low and High Index of a key in sorted array

#### Problem Statement
Given a sorted array of integers, return the low and high index of the given key. Return -1 if not found. The array length can be in millions with lots of duplicates.

#### Example
```
Input: [1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 20]
Output: 2, 9
```

#### Solution

**LOW INDEX**
1. initialize ```low = 0``` and ```high = length of array -1```
2. initialize ```mid = low + (high-low)/2``` we can also do ```mid = (low+high)/2``` but this can cause overflow
3. start loop till ```low <= high```
    1. check if ```array[mid] <=  key``` if yes then set ```low = mid+1```
    2. else set ```high = mid-1```
4. check if ```array[low] == key``` and ```low < length of array``` if yes then ```return low``` 
5. else ```return -1```

**HIGH INDEX**
1. initialize ```low = 0``` and ```high = length of array -1```
2. initialize ```mid = low + (high-low)/2``` we can also do ```mid = (low+high)/2``` but this can cause overflow
3. start loop till ```low <= high```
    1. check if ```array[mid] == key``` if yes then set ```high = mid-1```
    2. else set ```low = mid+1```
4. check if ```array[high]``` is equal to ```key``` if yes then ```return high```
5. else ```return -1```

#### Code
```
def find_low_index(arr, key):
    low = 0
    high = len(arr) - 1
    mid = high // 2
    while low <= high:
        mid_elem = arr[mid]
        if mid_elem < key:
            low = mid + 1
        else:
            high = mid - 1
        mid = low + (high - low) // 2
    if low < len(arr) and arr[low] == key:
        return low
    return -1

def find_high_index(arr, key):
    low = 0
    high = len(arr) - 1
    mid = high // 2
    while low <= high:
        mid_elem = arr[mid]
        if mid_elem <= key:
            low = mid + 1
        else:
            high = mid - 1
        mid = low + (high - low) // 2
    if high == -1:
        return high
    if high < len(arr) and arr[high] == key:
        return high
    return -1
```

#### Time Complexity
    O(logn) where n is length of array
#### Space Complexity
    O(1) no extra space is used

### Move all Zeros to the beging of the Array

#### Problem Statement
Given an integer array, move all elements containing '0' to the left while maintaining the order of other elements in the array.

#### Example
```
Input: [1,10,20,0,59,63,0,88,0]
Output: [0,0,0,1,10,20,59,63,88]
```
#### Solution
1. initialize ```write_index = length of array -1```
2. start loop from ```length of array -1``` till ```0```
    1. check if ```array[i] != 0``` if yes then set ```array[write_index] = array[i]``` and ```write_index -= 1```
3. start loop from ```write_index``` till ```0``` and set ```array[i] = 0```

#### Code
```
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
```
#### Time Complexity
    O(n) where n is length of array
#### Space Complexity
    O(1) no extra space is used

### Best Time to Buy and Sell Stock to Maximize Profit

#### Problem Statement
Given an array of numbers representing the daily stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

#### Example
```
Input: [9, 11, 8, 5, 7, 10]
Output: 5
```
#### Solution

1. check if ```array``` is ```None``` or ```length of array < 2``` if yes then ```return None```
2. initialize ```current_buy = array[0]```, ```global_sell = array[1]```, ```global_profit = global_sell - current_buy```, ```current_profit = float('-inf')```
3. start loop from ```1``` till ```length of array```
    1. set ```current_profit = array[i] - current_buy```
    2. check if ```current_profit > global_profit``` if yes then set ```global_profit = current_profit``` and ```global_sell = array[i]```
    3. check if ```current_buy > array[i]``` if yes then set ```current_buy = array[i]```
4. ```return global_sell - global_profit, global_sell```

#### Code
```
def find_buy_sell_stock_prices(array):
    if array == None or len(array) < 2:
        return None
    current_buy = array[0]
    global_sell = array[1]
    global_profit = global_sell - current_buy
    current_profit = float('-inf')
    for i in range(1, len(array)):
        current_profit = array[i] - current_buy
        if current_profit > global_profit:
            global_profit = current_profit
            global_sell = array[i]
        if current_buy > array[i]:
            current_buy = array[i]
    result = global_sell - global_profit, global_sell
    return result
```

#### Time Complexity
    O(n) where n is length of array
#### Space Complexity
    O(1) no extra space is used

### Merge An Array with Overlapping Intervals

#### Problem Statement
Given an array (list) of intervals as input where each interval has a start and end timestamps. Input array is sorted by starting timestamps. You are required to merge overlapping intervals and return output array (list).

#### Example
```
Input: [(1, 5), (3, 7), (4, 6), (6, 8), (10, 12), (11, 15)]
Output: [(1, 8), (10, 15)]
```

#### Solution
1. initialize ```merged = []```
2. start loop from ```1``` till ```length of array```
    1. check if ```array[i][0] <= merged[-1][1]``` if yes then set ```merged[-1][1] = max(merged[-1][1], array[i][1])```
    2. else append ```array[i]``` to ```merged```
3. ```return merged```

#### Code
```
def merge_intervals(v):
  result = [v[0]]
  j = 1
  for i in range(1,len(v)):
    if result[j-1][2] >= v[i][0]:
      if v[i][1] > result[j-1][1]:
        result[j-1][1] = v[i][0]

    else:
      result.append(v[i])
      j+=1
  return result
```

#### Time Complexity
    O(n) where n is length of array
#### Space Complexity
    O(1) no extra space is used

### Find Pair With Given Sum in Array

#### Problem Statement
Given an unsorted array of integers, find a pair with given sum in it.

#### Example
```
Input: [8, 7, 2, 5, 3, 1]
Sum: 10
Output: [0, 2] or [1, 4]
```

#### Solution
1. initialize ```hash_map = {}```
2. start loop from ```0``` till ```length of array```
    1. check if ```array[i] in hash_map``` if yes then ```return True```
    2. else ```hash_map[sum - array[i]] = i```
3. ```return False```

#### Code
```
def find_sum_of_two(A, val):
  hash_map = {}
  for i in range(len(A)):
    if A[i] in hash_map:
      return True
    else:
      hash_map[val - A[i]] = A[i]
  return False
```
#### Time Complexity
    O(n) where n is length of array
#### Space Complexity
    O(n) where n is length of array for hash_map

### Squares Of a Sorted Array

#### Problem Statement
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

#### Example
```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
```

#### Solution
1. initialize ```result = []```
2. initialize ```left = 0```, ```right = len(array) - 1```
3. start loop from ```right``` till ```left```
    1. check if ```abs(array[left]) > abs(array[right])``` if yes then ```result.append(array[left] * array[left])``` and ```left += 1```
    2. else ```result.append(array[right] * array[right])``` and ```right -= 1```
4. ```return result[::-1]``` to reverse the array

#### Code
```
def sortedSquares(nums):
  result = []
  left = 0
  right = len(nums) - 1
  while left <= right:
    if abs(nums[left]) > abs(nums[right]):
      result.append(nums[left] * nums[left])
      left += 1
    else:
      result.append(nums[right] * nums[right])
      right -= 1
  return result[::-1]
```

#### Time Complexity
    O(n) where n is length of array
#### Space Complexity
    O(n) where n is length of array for result

### Container With Most Water

#### Problem Statement
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

#### Example
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
```

#### Solution
1. initialize ```left = 0```, ```right = len(array) - 1```
2. initialize ```max_area = 0```
3. start loop from ```left``` till ```right```
    1. check if ```array[left] < array[right]``` if yes then ```max_area = max(max_area, array[left] * (right - left))``` and ```left += 1```
    2. else ```max_area = max(max_area, array[right] * (right - left))``` and ```right -= 1```
4. ```return max_area```

#### Code
```
def max_water_area_container(height):
    i = 0
    j = len(height)-1
    max_water = 0
    while(i<j):
        hi,hj= height[i],height[j]
        container = min(hi,hj)* (j-i)
        if max_water < container:
            max_water = container
        if hi < hj:
            i+=1
        else:
            j-=1
    return max_water
```

#### Time Complexity
    O(n) where n is length of array
#### Space Complexity
    O(1) no extra space is used

### Quick Sort Algorithm

#### Problem Statement
Given an array of integers, sort the array in ascending order using the Quick Sort algorithm.

#### Example
```
Input: [8, 7, 2, 5, 3, 1]
Output: [1, 2, 3, 5, 7, 8]
```

#### Solution
**Partition**
1. initialize ```pivot_value = array[low]```
2. initialize ```i = low```, ```j = high```
3. start loop till ```i < j```
    1. start loop till ```i <= j and array[i] <= pivot_value``` if yes then ```i += 1```
    2. start loop till ```array[j] > pivot_value``` if yes then ```j -= 1```
    3. check if ```i < j``` if yes then ```array[i], array[j] = array[j], array[i]```
4. ```array[low], array[j] = array[j], pivot_value```
5. ```return j```

**Quick Sort Helper**
1. check if ```low < high``` if yes then
    1. ```pivot_index = partition(array, low, high)```
    2. ```quick_sort_helper(array, low, pivot_index-1)```
    3. ```quick_sort_helper(array, pivot_index+1, high)```

**Quick Sort**
1. ```quick_sort_helper(array, 0, len(array)-1)```
2. ```return array```




#### Code
```
def partition(nums, low, high):
    pivot_value = nums[low]
    i = low
    j = high
    while i<j:
        while i <= j and nums[i] <= pivot_value:
            i += 1
        while nums[j] > pivot_value:
            j-=1

        if i<j:
            nums[i], nums[j] = nums[j], nums[i]
        
    nums[low], nums[j] = nums[j], pivot_value
    
    return j

def quick_sort_helper(nums, low, high):
    if low < high:
        pivot_index = partition(nums, low, high)
        quick_sort_helper(nums, low, pivot_index-1)
        quick_sort_helper(nums, pivot_index+1, high)

def quick_sort(nums):
    quick_sort_helper(nums, 0, len(nums)-1)
    return nums
```

#### Time Complexity
    O(nlogn) where n is length of array
#### Space Complexity
    O(logn) where n is length of array for recursion stack

### Sort Colors

#### Problem Statement
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

#### Example
```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

#### Solution
1. initialize ```low = 0```, ```mid = 0```, ```high = len(array) - 1```
2. start loop till ```mid <= high```
    1. check if ```array[mid] == 0``` if yes then ```array[low], array[mid] = array[mid], array[low]``` and ```low += 1```
    2. check if ```array[mid] == 1``` if yes then ```mid += 1```
    3. check if ```array[mid] == 2``` if yes then ```array[mid], array[high] = array[high], array[mid]``` and ```high -= 1```
3. ```return array```

#### Code
```
def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums
```

#### Time Complexity
    O(n) where n is length of array
#### Space Complexity
    O(1) no extra space is used

### Arrange The Largest Number

#### Problem Statement
Given a list of non negative integers, arrange them in such a manner that they form the largest number possible.The result is going to be very large, hence return the result in the form of a string.

#### Example
```
Input: [3, 30, 34, 5, 9]
Output: 9534330
```

#### Solution

1. initialize ```array = [str(i) for i in array]```
2. sort the array using ```lambda``` function
3. ```return ''.join(array)```

#### Code
```
class LargerNumKey(str):
  def __lt__(x,y):
    return x+y > y+x

def largest_number(nums):
  mapStr = map(str, nums)
  mapStr = sorted(mapStr,key=LargerNumKey)
  largest = ''.join(mapStr)
  return '0' if largest[0] == '0' else largest
```

#### Time Complexity
    O(nlogn) where n is length of array
#### Space Complexity
    O(n) where n is length of array for extra space used for storing string
### Shuffle Array

#### ~~Incomplete~~

### First Missing Positive Integer

#### Problem Statement
Given an unsorted integer array nums, find the smallest missing positive integer.

#### Example
```
Input: nums = [1,2,0]
Output: 3
```

#### Solution
1. initialize ```i = 0```
2. start loop till ```i < len(array)```
    1. check if ```array[i] > 0 and array[i] <= len(array) and array[i] != array[array[i]-1]``` if yes then ```array[array[i]-1], array[i] = array[i], array[array[i]-1]``` else ```i += 1```
3. start loop till ```i < len(array)```
    1. check if ```array[i] != i+1``` if yes then ```return i+1``` else ```i += 1```
4. ```return len(array)+1```

#### Code
```
def first_missing_positive(nums):
    i = 0
    while i < len(nums):
        if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        else:
            i += 1
    i = 0
    while i < len(nums):
        if nums[i] != i+1:
            return i+1
        else:
            i += 1
    return len(nums)+1
```

#### Time Complexity
    O(n) where n is length of array
#### Space Complexity
    O(1) no extra space is used

### Minimum Size Subarray Sum

#### Problem Statement
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

#### Example
```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
```

#### Solution

1. initialize ```left = 0```, ```sum1 = 0```, ```result = float('inf')```
2. start loop till ```i < len(array)```
    1. ```sum1 += array[i]```
    2. start loop till ```sum1 >= target```
        1. ```result = min(result,(i+1) - left)```
        2. ```sum1 -= array[left]```
        3. ```left += 1```
3. check if ```result == float('inf')``` if yes then ```return 0``` else ```return result```


#### Code
```
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
```

#### Time Complexity
    O(n) where n is length of array
#### Space Complexity
    O(1) no extra space is used


### Next Element Greater Than Subset

#### Problem Statement

Given an array, find the next greater element G[i] for every element A[i] in the array. The Next greater Element for an element A[i] is the first greater element on the right side of A[i] in array. More formally,

#### Example
**Input**
```
    nums1 = [4,1,2]
    nums2 = [1,3,4,2].
```
**Output**
```
    [-1, 3, -1]
```

#### Solution
1. initialize ```stack = []```
2. initialize ```hash_map = {}```
3. start loop from ```0``` till ```length of array2```
   1. check if ```stack is not empty and array2[i] > stack[-1]``` if yes then ```hash_map[stack.pop()] = array2[i]```
   2. append ```array2[i]``` to ```stack```
4. start loop from ```0``` till ```length of array1```
   1. check if ```array1[i] in hash_map``` if yes then ```array1[i] = hash_map[array1[i]]``` else ```array1[i] = -1```
5. return ```array1```

#### Code
```
def next_greater_element(nums1, nums2):
    stack = []
    hash_map = {}
    for i in range(len(nums2)):
        while stack and nums2[i] > stack[-1]:
            hash_map[stack.pop()] = nums2[i]
        stack.append(nums2[i])
    for i in range(len(nums1)):
        if nums1[i] in hash_map:
            nums1[i] = hash_map[nums1[i]]
        else:
            nums1[i] = -1
    return nums1
```

#### Time Complexity
    O(n) where n is length of array
#### Space Complexity
    O(n) where n is length of array for stack and hash_map

### Product of All Elements Except Itself in an Array

#### Problem Statement
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

#### Example
```
Input: [1, 2, 3, 4, 5]
Output: [120, 60, 40, 30, 24]
```

#### Solution

1. initialize ```result = [1] * len(array)```
2. initialize ```left = [1] * len(array)```
3. initialize ```right = [1] * len(array)```
4. start loop from ```1``` till ```length of array```
    1. ```left[i] = left[i-1] * array[i-1]```
5. start loop from ```length of array - 2``` till ```-1```
    1. ```right[i] = right[i+1] * array[i+1]```
6. start loop from ```0``` till ```length of array```
    1. ```result[i] = left[i] * right[i]```
7. return ```result```

#### Code
```
def product_except_self(nums):
    result = [1] * len(nums)
    left = [1] * len(nums)
    right = [1] * len(nums)
    for i in range(1, len(nums)):
        left[i] = left[i-1] * nums[i-1]
    for i in range(len(nums)-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]
    for i in range(len(nums)):
        result[i] = left[i] * right[i]
    return result
```

#### Time Complexity
    O(n) where n is length of array
#### Space Complexity    
    O(n) where n is length of array for left, right and result

## Linked-List
## Math-&-Stats
## Strings
## Trees
## Stack-&-Queues
## Graph
## Back-Tracking
## Dynamic-Programming
## Miscellaneous

