from SLL import *
from SLLNode import *
def get_middle(head):
    if head is None:
        return head
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge_sorted(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.value < head2.value:
        head1.next = merge_sorted(head1.next, head2)
        return head1
    else:
        head2.next = merge_sorted(head1, head2.next)
        return head2
    

def merge_sort(head):
    if head is None or head.next is None:
        return head
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None
    left = merge_sort(head)
    right = merge_sort(next_to_middle)
    sorted_list = merge_sorted(left, right)
    return sorted_list


def main():
    v_list = [[29, 23, 82, 11, 4, 3, 21], [59, 7, -3, 21, 14, 30, 120]]
    for i in range(len(v_list)):
        obj1 = LinkedList(v_list[i])
        print("1. Unsorted list: ", end="")
        print(obj1)
        obj2 = LinkedList([])
        obj2.head = merge_sort(obj1.head)
        print("   Sorted list:   ", end="")
        print(obj2)
        print("-"*100)

if __name__ == '__main__':
    main()