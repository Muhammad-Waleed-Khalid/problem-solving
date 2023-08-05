from SLL import *
from SLLNode import *

def deleteAllOccurrencesOfAGivenKey(head, key):
    if head is None:
        return None
    curr = head
    prev = None
    while curr is not None:
        if curr.value == key:
            if prev is None:
                head = curr.next
                curr = head
            else:
                prev.next = curr.next
                curr = curr.next
        else:
            prev = curr
            curr = curr.next
    return head


def main():
    v_list = [[1, 1, 2, 2, 3, -1, 10, 12], [10, 20, -22, 21, -12]]
    nodes_to_del = [-1, -12]
    
    for i in range(len(v_list)):
        obj1 = LinkedList(v_list[i])
        print(str(i+1) + ". Original list:\t", end="")
        print(obj1)
        print("   Key to delete:\t" + str(nodes_to_del[i]))

        obj1.head = deleteAllOccurrencesOfAGivenKey(obj1.head, nodes_to_del[i])
        print("   After deletion:\t", end="")

        print(obj1)
        print("-"*100)
        
if __name__ == '__main__':
    main()