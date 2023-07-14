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
  - [Move all Zeros to the beging of the Array](#move-all-zeros-to-the-beging-of-the-array)
  - [Best Time to Buy and Sell Stock to Maximize Profit](#best-time-to-buy-and-sell-stock-to-maximize-profit)
  - [Merge An Array with Overlapping Intervals](#merge-an-array-with-overlapping-intervals)
  - [Find Pair With Given Sum in Array](#find-pair-with-given-sum-in-array)
  - [Squares Of a Sorted Array](#squares-of-a-sorted-array)
  - [Container With Most Water](#container-with-most-water)
  - [Quick Sort Algorithm](#quick-sort-algorithm)
  - [Sort Colors](#sort-colors)
  - [Arrange The Largest Number](#arrange-the-largest-number)
  - [Shuffle An Array](#shuffle-an-array)
  - [First Missing Positive Integer](#first-missing-positive-integer)
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
### Best Time to Buy and Sell Stock to Maximize Profit
### Merge An Array with Overlapping Intervals
### Find Pair With Given Sum in Array
### Squares Of a Sorted Array
### Container With Most Water
### Quick Sort Algorithm
### Sort Colors
### Arrange The Largest Number
### Shuffle An Array
### First Missing Positive Integer
## Linked-List
## Math-&-Stats
## Strings
## Trees
## Stack-&-Queues
## Graph
## Back-Tracking
## Dynamic-Programming
## Miscellaneous

