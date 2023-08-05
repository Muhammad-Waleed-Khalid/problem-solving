from SLL import *
from SLLNode import *

def halves(head):
    if not head:
        return None, None
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    head2 = slow.next
    slow.next = None
    rev_head2 = None
    while head2:
        temp = head2.next
        head2.next = rev_head2
        rev_head2 = head2
        head2 = temp
    head2 = rev_head2
    return head, head2

def merge_alternate(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    head = head1
    while head1.next:
        temp = head1.next
        head1.next = head2
        head2 = head2.next
        head1.next.next = temp
        head1 = temp
    head1.next = head2
    return head

def reorder_list(head):
    head1, head2 = halves(head)
    return merge_alternate(head1, head2)