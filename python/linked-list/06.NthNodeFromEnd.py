from SLL import *
from SLLNode import *

def find_nth_from_end(head,n):
    ptr = head
    while n>0 and ptr is not None:
        ptr = ptr.next
        n-=1
    if ptr is None and n>0:
        return None
    while ptr is not None:
        ptr = ptr.next
        head = head.next
    return head

def main():
    input_lists = [[-1, 2, 3, 4], [10], [1, 1, 2, 3, 4, 5], [28, 21, 14, 7]]
    inputs = [1, 2, 3, 4]

    for i in range(len(input_lists)):
        obj = LinkedList(input_lists[i])
        print(str(i + 1) + ". Original list:  " + str(input_lists[i]))
        actual_output = find_nth_from_end(obj.head, inputs[i])
        if not actual_output:
            print("   Node no.", inputs[i], "from the last node: None")
        else:
            print("   Node no.", inputs[i], "from the last node:", str(
                actual_output.value))
        print("-"*100)

if __name__ == '__main__':
    main()