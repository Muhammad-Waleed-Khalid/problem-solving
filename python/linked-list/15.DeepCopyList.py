from SLL import *
from SLLNode import *

def deep_copy_list(head):
    deep_head = None
    deep_tail = None
    curr = head
    while curr:
        if not deep_head:
            deep_head = LinkedListNode(curr.value)
            deep_tail = deep_head
        else:
            deep_tail.next = LinkedListNode(curr.value)
            deep_tail = deep_tail.next
        curr = curr.next
    return deep_head