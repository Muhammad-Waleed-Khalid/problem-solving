from SLL import *
from SLLNode import *


def odd_and_even_nodes(head):
    curr = head
    l_even = None
    while curr and curr.next:
        even = curr.next
        curr.next = even.next
        even.next = l_even
        l_even = even
        curr = curr.next
    return head, l_even

def merge_alternate(odd, even):
    if not odd:
        return even
    if not even:
        return odd
    head = odd
    while odd.next:
        temp = odd.next
        odd.next = even
        even = even.next
        odd.next.next = temp
        odd = temp
    odd.next = even
    return head

def reverse_even_nodes(head):
    odd,even = odd_and_even_nodes(head)
    return merge_alternate(odd, even)




def main():
    v_list = [[7, 14, 21, 28, 9],[1,2], [59, 7, -3, 21, 14, 30, 120],[7,1,7],[0,18,21,33]]
    
    for i in range(len(v_list)):
        # Declaring and creating a linked list
        obj1 = LinkedList(v_list[i])

        print("1. Original list:\t\t\t", end="")
        print(obj1)

        obj3 = LinkedList([])
        obj3.head = reverse_even_nodes(obj1.head)
        print("   After reversing even positions:\t", end="")
        print(obj3)
        print("-"*100)

if __name__ == '__main__':
    main()