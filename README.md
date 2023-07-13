# problem-solving
Top Problems must be revised before interview
- [Array](README.md#Array)
- [Linked List](README.md#Linked-List)
- [Math & Stats](README.md#Math-&-Stats)
- [Strings](README.md#Strings)
- [Trees](README.md#Trees)
- [Stack & Queues](README.md#Stack-&-Queues)
- [Graph](README.md#Graph)
- [Back Tracking](README.md#Back-Tracking)
- [Dynamic Programming](README.md#Dynamic-Programming)
- [Miscellaneous](README.md#Miscellaneous)

## Array 
### Binary Search On Sorted Array
  Binary Search is the most efficient way to search in Sorted array.  
  **Time Complexity :** O(*log*n)  
  **Space Complexity :** O(1) (iterative Solution), O(*log*n) recursive Solution
  #### Iterative Solution
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
  #### Recursive Solution
  

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
    def binary_search(nums,target):
        binary_search_rec(nums,target,0,len(nums))
  ~~~
### Rotate An Array By N Elements
### Rotated Binary Search
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
