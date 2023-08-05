from SLL import LinkedList
from SLLNode import LinkedListNode
# Here is the implementation of the reverseLinkedList function, which takes the head of a linked list as an argument and returns the head of the reversed linked list.
def reverseLinkedList(head):
    if head is None or head.next is None:
        return head

    prev = None
    curr = head
    next = None

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

def main():
    v_list = [[29, 23, 82, 11, 4, 3, 21], [59, 7, -3, 21, 14, 30, 120]]
    for i in range(len(v_list)):  
        obj1 = LinkedList(v_list[i])

        print(str(i+1) + ". Original list:\t", end="")
        print(obj1)

        # Reversing the created linked list
        obj2 = LinkedList(v_list[i])
        obj2.head = reverseLinkedList(obj1.head)
        print("   Reversed list:\t", end="")

        # Display Reversed List
        print(obj2)
        print("-"*100)

if __name__ == '__main__':
    main()