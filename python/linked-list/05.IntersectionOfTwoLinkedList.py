from SLL import *
from SLLNode import *

def length(head):
    count = 0
    curr = head
    while curr is not None:
        count += 1
        curr = curr.next
    return count

def intersect(head1, head2):
    l1 = length(head1)
    l2 = length(head2)
    if l1 > l2:
        return intersect(head2, head1)
    diff = l2 - l1
    curr1 = head1
    curr2 = head2
    for i in range(diff):
        curr2 = curr2.next
    while curr1 is not None and curr2 is not None:
        if curr1 == curr2:
            return curr1
        curr1 = curr1.next
        curr2 = curr2.next
    return None

def intersect_using_extra_space(head1,head2):
    hash_set = set()
    curr = head1
    while curr is not None:
        hash_set.add(curr)
        curr = curr.next
    curr = head2
    while curr is not None and curr not in hash_set:
        curr = curr.next
    return curr


#### Main ####

node1 = LinkedListNode(25)
node2 = LinkedListNode(30)
node3 = LinkedListNode(18)
node4 = LinkedListNode(10)
nodeList = [node1, node2, node3, node4]
# list 1
list1 = [4,9,16]
obj1 = LinkedList(list1)
ptr = obj1.head
while ptr.next is not None:
    ptr = ptr.next

for i in range(len(nodeList)):
    ptr.next = nodeList[i]
    ptr = ptr.next


# list 2
obj2 = LinkedList([])
obj2.head = node1

# list 3
list3 = [22,11]
obj3 = LinkedList(list3)
ptr = obj3.head
while ptr.next is not None:
    ptr = ptr.next


ptr.next = nodeList[3]


intersection_lists = [[obj1.head, obj2.head], [obj1.head, obj3.head], [obj2.head, obj3.head]] 
for i in range(len(intersection_lists)):
    head1 = intersection_lists[i][0]
    head2 = intersection_lists[i][1]
    print(str(i + 1) + '. List 1:\t\t' + str(head1.to_list()))
    print('   List 2:\t\t' + str(head2.to_list()))
    intersection_node = intersect(head1, head2)
    
    if intersection_node == None:
        print('   No intersection node found')
    else:
        print('   Intersection at:\t' + str(intersection_node.value))
    print("-------------------------------------------------------------------------------------------------------\n")
    
    print(str(i + 1) + '. List 1:\t\t' + str(head1.to_list()))
    print('   List 2:\t\t' + str(head2.to_list()))
    intersection_node = intersect(head1, head2)
    
    if intersection_node == None:
        print('   No intersection node found')
    else:
        print('   Intersection using extra space at:\t' + str(intersection_node.value))
    print("-------------------------------------------------------------------------------------------------------\n")

