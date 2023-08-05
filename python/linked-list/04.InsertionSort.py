from SLL import *
from SLLNode import *


def sorted_insert(head, node):
    if node is None:
        return head
    if head is None or node.value <= head.value:
        node.next = head
        return node
    curr = head
    while curr.next is not None and curr.next.value < node.value:
        curr = curr.next
    node.next = curr.next
    curr.next = node
    return head

def insertion_sort(head):
    if head is None:
        return None
    sorted_list = None
    curr = head
    while curr is not None:
        temp = curr.next
        sorted_list = sorted_insert(sorted_list, curr)
        curr = temp
    return sorted_list

def main():
    v_list = [[29, 23, 82, 11, 4, 3, 21], [59, 7, -3, 21, 14, 30, 120]]
    for i in range(len(v_list)):
        obj1 = LinkedList(v_list[i])

        print(str(i+1) + ". Unsorted list:\t", end="")
        print(obj1)

        # Reversing the created linked list
        obj1.head = insertion_sort(obj1.head)
        print("   Sorted list:\t\t", end="")

        # Display Reversed List
        print(obj1)
        print("-"*100)

if __name__ == '__main__':
    main()