# problem-solving
Top Problems must be revised before interview
- [problem-solving](#problem-solving)
  - [Array](#array)
    - [Binary Search On Sorted Array](#binary-search-on-sorted-array)
      - [Iterative Solution Of Binary Search](#iterative-solution-of-binary-search)
        - [Code](#code)
      - [Recursive Solution of Binary Search](#recursive-solution-of-binary-search)
        - [Code](#code-1)
    - [Rotate An Array By N Elements](#rotate-an-array-by-n-elements)
      - [Problem Statement](#problem-statement)
      - [Example](#example)
      - [Solution](#solution)
      - [Code](#code-2)
    - [Rotated Binary Search](#rotated-binary-search)
      - [Problem Statement](#problem-statement-1)
      - [Example](#example-1)
    - [Smallest Common Number Between Three Arrays](#smallest-common-number-between-three-arrays)
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

  **Time Complexity : O(*log*n), Space Complexity : O(1)**
  
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
  #### Recursive Solution of Binary Search
  
  1. check base case (low is greater or equal to high)  if true return -1 // it means target is not present in array
  2. calculate mid index of low and high use **mid = low+high/2** or **mid = low+(high-low)/2**
  3. check if nums[mid] equal to target
  4. [true] **HURRAH!** (we found the element in array) return mid
  5. [False] check if nums[mid] smaller to target
  ##### Code
  ~~~
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
  ~~~
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

### Rotated Binary Search

#### Problem Statement
We’re given a sorted integer array, ```array``` and an integer value, ```key```. The array is rotated by some arbitrary number. Search the ```target``` in this array. If the target does not exist then return -1.

#### Example
<table border=1>
<tr> <td>0 </td><td>  1 </td><td>  2 </td><td>  3 </td><td>  4 </td><td>  5 </td><td>  6 </td><td>  7 </td><td>  8 </td><td>  9</td></tr>
<tr> <span bg-color=red><td>13 </td><td>  14 </td><td> 20 </td></span><td> 0  </td><td> 2 </td><td> 3 </td><td> 5 </td><td> 7 </td><td> 8  </td><td> 11</td></tr>
</table>

### Smallest Common Number Between Three Arrays
### Find Low and High Index of a key in sorted array
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
