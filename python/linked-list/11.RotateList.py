from SLL import *
from SLLNode import *

def rotate_list(head,n):
    n = n % len(head)
    if n == 0 or not head:
        return head
    curr = head
    for i in range(n-1):
        curr = curr.next
    new_head = curr.next
    curr.next = None
    curr = new_head
    while curr.next:
        curr = curr.next
    curr.next = head
    return new_head

def main():
    v_list = [[7, 14, 21, 28, 9],[1,2], [59, 7, -3, 21, 14, 30, 120],[7,1,7],[0,18,21,33]]
    rotation = [1,-2,-3,4,-5]
    for i in range(len(v_list)):
        # Declaring and creating a linked list
        obj1 = LinkedList(v_list[i])

        print("1. Original list:\t\t\t", end="")
        print(obj1)
        obj1.head = rotate_list(obj1.head,rotation[i])
        print(F"Rotation of list by {rotation[i]}:\t", end="")
        print(obj1)
        print("-"*100)

if __name__ == '__main__':
    main()
    