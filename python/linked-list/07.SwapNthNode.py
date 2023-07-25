from SLL import *
from SLLNode import *

# Node indices starts from 1.
def swap_nth_node(head, n):
    prev = head
    curr = head
    while n>0 and curr.next is not None:
        prev = curr
        curr = curr.next
        n-=1
    if n==0 and prev is not None:   
        head.value, prev.value = prev.value, head.value
    return head


def main():
    input_lists = [[-1, 2, 3, 4], [10], [1, 1, 2, 3, 4, 5], [28, 21, 14, 7]]
    inputs = [1, 2, 3, 4]

    results = []

    for i in range(len(input_lists)):
        obj = LinkedList(input_lists[i])

        print(str(i + 1) + '. swap_nth_node(' + str(input_lists[i]) +
              ', ' + str(inputs[i])+')\n   ', end='')

        obj2 = LinkedList([])
        obj2.head = swap_nth_node(obj.head, inputs[i])
        print(obj2)
        print("-"*100)


if __name__ == '__main__':
    main()
