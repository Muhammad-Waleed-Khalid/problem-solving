<h1>Linked List</h1>
<h1>Table of Content</h1>

- [Introduction](#introduction)
- [1. Single Linked List](#1-single-linked-list)
  - [1.1. Insertion](#11-insertion)
    - [1.1.1. Insertion at the beginning](#111-insertion-at-the-beginning)
      - [Time Complexity](#time-complexity)
    - [1.1.2. Insertion at the end](#112-insertion-at-the-end)
      - [Time Complexity](#time-complexity-1)
    - [1.1.3. Insertion at a given position](#113-insertion-at-a-given-position)
      - [Time Complexity](#time-complexity-2)
  - [1.2. Deletion](#12-deletion)
    - [1.2.1. Deletion at the beginning](#121-deletion-at-the-beginning)
      - [Time Complexity](#time-complexity-3)
    - [1.2.2. Deletion at the end](#122-deletion-at-the-end)
      - [Time Complexity](#time-complexity-4)
    - [1.2.3. Deletion at a given position](#123-deletion-at-a-given-position)
      - [Time Complexity](#time-complexity-5)
  - [1.3. Searching](#13-searching)
      - [Time Complexity](#time-complexity-6)
  - [1.4. Reversing](#14-reversing)
      - [Time Complexity](#time-complexity-7)
- [2. Double Linked List](#2-double-linked-list)
- [3. Circular Linked List](#3-circular-linked-list)
- [4. Doubly Circular Linked List](#4-doubly-circular-linked-list)

## Introduction
A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers.

In simple words, a linked list consists of nodes where each node contains a data field and a reference(link) to the next node in the list.

Types of Linked List:  
    1. [Single Linked List](#1-single-linked-list)  
    2. [Double Linked List](#2-double-linked-list)  
    3. [Circular Linked List](#3-circular-linked-list)  
    4. [Doubly Circular Linked List](#4-doubly-circular-linked-list)  

## 1. Single Linked List
A linked list in which each node has only one pointer to the next node is called a single linked list.
### 1.1. Insertion
#### 1.1.1. Insertion at the beginning
```python
    def insert_at_head(self, value):
        new_node = LinkedListNode(value)
        new_node.next = self.head
        self.head = new_node
```
```cpp
    void insert_at_head(int value) {
        LinkedListNode* new_node = new LinkedListNode(value);
        new_node->next = head;
        head = new_node;
    }
```
##### Time Complexity
O(1)

#### 1.1.2. Insertion at the end
```python
    def insert_at_tail(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
```
```cpp
    void insert_at_tail(int value) {
        LinkedListNode* new_node = new LinkedListNode(value);
        if (head == NULL) {
            head = new_node;
            return;
        }
        LinkedListNode* temp = head;
        while (temp->next) {
            temp = temp->next;
        }
        temp->next = new_node;
    }
```
##### Time Complexity
O(n)

#### 1.1.3. Insertion at a given position
```python
    def insert_at_position(self, value, position):
        if position < 0 or position > self.get_length():
            raise Exception("Invalid position")
        if position == 0:
            self.insert_at_head(value)
            return
        new_node = LinkedListNode(value)
        temp = self.head
        for i in range(position - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
```
```cpp
    void insert_at_position(int value, int position) {
        if (position < 0 || position > get_length()) {
            throw "Invalid position";
        }
        if (position == 0) {
            insert_at_head(value);
            return;
        }
        LinkedListNode* new_node = new LinkedListNode(value);
        LinkedListNode* temp = head;
        for (int i = 0; i < position - 1; i++) {
            temp = temp->next;
        }
        new_node->next = temp->next;
        temp->next = new_node;
    }
```
##### Time Complexity
O(n)

### 1.2. Deletion
#### 1.2.1. Deletion at the beginning
```python
    def delete_at_head(self):
        if self.head is None:
            raise Exception("List is empty")
        self.head = self.head.next
```
```cpp
    void delete_at_head() {
        if (head == NULL) {
            throw "List is empty";
        }
        head = head->next;
    }
```
##### Time Complexity
O(1)

#### 1.2.2. Deletion at the end
```python
    def delete_at_tail(self):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
```
```cpp
    void delete_at_tail() {
        if (head == NULL) {
            throw "List is empty";
        }
        if (head->next == NULL) {
            head = NULL;
            return;
        }
        LinkedListNode* temp = head;
        while (temp->next->next) {
            temp = temp->next;
        }
        temp->next = NULL;
    }
```

##### Time Complexity
O(n)

#### 1.2.3. Deletion at a given position
```python
    def delete_at_position(self, position):
        if position < 0 or position >= self.get_length():
            raise Exception("Invalid position")
        if position == 0:
            self.delete_at_head()
            return
        temp = self.head
        for i in range(position - 1):
            temp = temp.next
        temp.next = temp.next.next
```
```cpp
    void delete_at_position(int position) {
        if (position < 0 || position >= get_length()) {
            throw "Invalid position";
        }
        if (position == 0) {
            delete_at_head();
            return;
        }
        LinkedListNode* temp = head;
        for (int i = 0; i < position - 1; i++) {
            temp = temp->next;
        }
        temp->next = temp->next->next;
    }
```
##### Time Complexity
O(n)

### 1.3. Searching
```python
    def search(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                return True
            temp = temp.next
        return False
```
```cpp
    bool search(int value) {
        LinkedListNode* temp = head;
        while (temp) {
            if (temp->data == value) {
                return true;
            }
            temp = temp->next;
        }
        return false;
    }
```

##### Time Complexity
O(n)


### 1.4. Reversing
```python
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
```
```cpp
    void reverse() {
        LinkedListNode* prev = NULL;
        LinkedListNode* current = head;
        while (current) {
            LinkedListNode* next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        head = prev;
    }
```

##### Time Complexity
O(n)




## 2. Double Linked List
A linked list in which each node has two pointers, one to the next node and one to the previous node, is called a double linked list.
## 3. Circular Linked List
A linked list in which the last node points to the first node is called a circular linked list.
## 4. Doubly Circular Linked List
A linked list in which the last node points to the first node and the first node points to the last node is called a doubly circular linked list.
