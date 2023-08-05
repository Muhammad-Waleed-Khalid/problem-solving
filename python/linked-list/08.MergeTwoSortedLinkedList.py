from SLL import *
from SLLNode import *

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
    
def main():
    list1 = [1, 2, 3, 5, 45]
    obj1 = LinkedList(list1)

    list2 = [10, 20, 30, 40, 50]
    obj2 = LinkedList(list2)

    list3 = [6, 7, 8, 9, 10]
    obj3 = LinkedList(list3)

    list4 = [29, 39, 49, 69]
    obj4 = LinkedList(list4)

    head1_none = LinkedList([])
    # print(obj3.head.next.data)
    head_list = [[head1_none.head, head1_none.head],
                 [head1_none.head, obj1.head],
                 [obj1.head, head1_none.head],
                 [obj1.head, obj2.head],
                 [obj4.head, obj3.head]]

    for i in range(len(head_list)):
        # Creating objects
        res_obj = LinkedList([])
        display_obj = LinkedList([])

        head1 = head_list[i][0]
        head2 = head_list[i][1]

        display_obj.head = head1
        print(str(i + 1) + ". List 1:\t", end="")
        print(display_obj)

        display_obj.head = head2
        print("   List 2:\t", end="")
        print(display_obj)

        res_obj.head = merge_sorted(head1, head2)
        print("   Merged List:\t", end="")
        print(res_obj)
        print("-"*100)

if __name__ == '__main__':
    main()