<h1>Array</h1>

<h1>Table of Content</h1>

- [Introduction](#introduction)
- [1. Insertion in Array](#1-insertion-in-array)
    - [Time Complexity](#time-complexity)
  - [Space Complexity](#space-complexity)
- [2. Deletion in Array](#2-deletion-in-array)
  - [Time Complexity](#time-complexity-1)
  - [Space Complexity](#space-complexity-1)
- [3. Searching in Array](#3-searching-in-array)
  - [Time Complexity](#time-complexity-2)
  - [Space Complexity](#space-complexity-2)
- [4. Reversing an Array](#4-reversing-an-array)
  - [Time Complexity](#time-complexity-3)
  - [Space Complexity](#space-complexity-3)

## Introduction
An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. This makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the name of the array).

For simplicity, we can think of an array a fleet of stairs where on each step is placed a value (let’s say one of your friends). Here, you can identify the location of any of your friends by simply knowing the count of the step they are on.

## 1. Insertion in Array
Inserting a new element in an array of size n can be broadly divided in two steps:

1. The first step is to find the location in the array where we want to insert the new element. 
2. The second step is to insert the element at that location, shifting all the elements after that location by 1 position to the right.

```python
def insert_at(self, value, position):
    if position < 0 or position > self.length:
        return None
    left = self.arr[:position]
    right = self.arr[position:]
    self.arr = left + [value] + right
```
```cpp
void insert(int value, int position) {
    if (position < 0 || position > length) {
        return;
    }
    int *new_arr = new int[length + 1];
    for (int i = 0; i < position; i++) {
        new_arr[i] = arr[i];
    }
    new_arr[position] = value;
    for (int i = position + 1; i < length + 1; i++) {
        new_arr[i] = arr[i - 1];
    }
    if (arr != nullptr) {
      delete[] arr;
    }
    arr = new_arr;
    length++;
}
```
#### Time Complexity
O(n)
### Space Complexity
O(n)

## 2. Deletion in Array
Deletion from an array can be divided into two steps:

1. The first step is to locate the position of the element to be deleted in the array.
2. Move all the elements after the deleted element by one place to the left.

```python
def delete_at(self, position):
    if position < 0 or position >= self.length:
        return None
    left = self.arr[:position]
    right = self.arr[position + 1:]
    self.arr = left + right
```
```cpp
void delete_at(int position) {
    if (position < 0 || position >= length) {
        return;
    }
    int *new_arr = new int[length - 1];
    for (int i = 0; i < position; i++) {
        new_arr[i] = arr[i];
    }
    for (int i = position + 1; i < length; i++) {
        new_arr[i - 1] = arr[i];
    }
    if (arr != nullptr) {
      delete[] arr;
    }
    arr = new_arr;
    length--;
}
```
### Time Complexity
  O(n)
### Space Complexity
  O(n)

## 3. Searching in Array
Searching for an element in an array means to check if a given element is present in the array or not. This can be done by comparing each element of the array with the given element.

```python
def search(self, value):
    for i in range(self.length):
        if self.arr[i] == value:
            return i
    return -1
```
```cpp
int search(int value) {
    for (int i = 0; i < length; i++) {
        if (arr[i] == value) {
            return i;
        }
    }
    return -1;
}
```
### Time Complexity
  O(n)
### Space Complexity
  O(1)

## 4. Reversing an Array
```python
def reverse(self):
    left = 0
    right = self.length - 1
    while left < right:
        self.arr[left], self.arr[right] = self.arr[right], self.arr[left]
        left += 1
        right -= 1
```
```cpp
void reverse() {
    int left = 0;
    int right = length - 1;
    while (left < right) {
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;
    }
}
```

### Time Complexity
  O(n)
### Space Complexity
  O(1)


