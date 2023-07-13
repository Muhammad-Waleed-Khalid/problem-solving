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
