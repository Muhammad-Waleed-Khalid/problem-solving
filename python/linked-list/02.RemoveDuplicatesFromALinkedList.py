from SLLNode import LinkedListNode
from SLL import LinkedList

# Here is the implementation of the removeDuplicates function, which takes the head of a linked list as an argument and returns the head of the linked list with duplicates removed.
def removeDuplicates(head):
    if head is None or head.next is None:
        return head
    
    curr = head
    hashset = set()
    hashset.add(curr.value)
    while curr.next is not None:
        if curr.next.value in hashset:
            curr.next = curr.next.next
        else:
            hashset.add(curr.next.value)
            curr = curr.next
    return head

# Driver code
def main():

    v_list = [[4, 7, 4, 9, 7, 11, 4], [10, -20, 10, -20, 20, 10]]
    
    for i in range(len(v_list)):
        obj1 = LinkedList(v_list[i])

        # The CreateLinkedList function will convert our vector to a Linked list
        print(str(i+1) + ". Original list:\t\t", end="")
        print(obj1)

        # merge sort display
        obj1.head = removeDuplicates(obj1.head)
        print("   Removed Duplicate list:\t", end="")

        # Display Merge Sorted List
        print(obj1)
        print("-"*100)

if __name__ == '__main__':
    main()