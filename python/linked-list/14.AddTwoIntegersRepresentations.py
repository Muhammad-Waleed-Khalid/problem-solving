from SLL import *
from SLLNode import *

def add_integers(int1,int2):
    carry = 0
    head = None
    while int1 or int2 or carry:
        sum = carry
        if int1:
            sum += int1.value
            int1 = int1.next
        if int2:
            sum += int2.value
            int2 = int2.next
        digit = sum % 10
        carry = sum // 10
        if not head:
            head = LinkedListNode(digit)
            tail = head
        else:
            tail.next = LinkedListNode(digit)
            tail = tail.next
    return head

def main():
    v1_list = [[1, 0, 9, 9], [2, 5, 0, 0, 0]]
    v2_list = [[7, 3, 2], [1, 1, 1, 1]]

    for i in range(len(v1_list)):
        obj1 = LinkedList(v1_list[i])
        obj2 = LinkedList(v2_list[i])

        print(str(i+1) + ". First list: \t    ", end="")
        print(obj1)
        print("   Second list:\t    ", end="")
        print(obj2)

        obj_r1 = LinkedList([])
        obj_r1.head = add_integers(obj1.head, obj2.head)
        print("   Addition result: ", end="")
        print(obj_r1)

        print("-"*100)

if __name__ == '__main__':
    main()
