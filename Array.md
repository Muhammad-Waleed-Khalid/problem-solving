<h1>Array</h1>

<h1>Table of Content</h1>

- [Introduction](#introduction)
- [1. Insertion in Array](#1-insertion-in-array)
    - [Time Complexity](#time-complexity)
  - [Space Complexity](#space-complexity)
- [2. Deletion in Array](#2-deletion-in-array)
  - [Time Complexity](#time-complexity-1)
  - [Space Complexity](#space-complexity-1)

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