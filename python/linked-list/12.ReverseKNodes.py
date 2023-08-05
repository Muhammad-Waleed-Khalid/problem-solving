from SLL import *
from SLLNode import *

def reverse_k_nodes(head, k):
    if k <= 1 or not head:
        return head
    curr_head = head
    curr_tail = head
    prev_rail = None
    reversed = None
    while curr_head:
        count = 0
        prev = None
        tail = curr_head.next
        while count < k and curr_head:
            curr_head.next = prev
            prev = curr_head
            curr_head = tail
            if tail:
                tail = tail.next
            count += 1
        if not reversed:
            reversed = prev
        if prev_rail:
            prev_rail.next = prev
        prev_rail = curr_tail
        curr_tail.next = curr_head
        curr_tail = curr_head
    return reversed

