from SLLNode import LinkedListNode

class LinkedList:
    # Default Constructor
    def __init__(self) -> None:
        self.length = 0
        self.head = None
    
    # Constructor with array of values
    def __init__(self, values ) -> None:
        self.head = None
        self.length = 0
        for value in values:
            self.insert_node_at_tail(value)
    
    # Insert node at head
    def insert_at_head(self, value):
        new_node = LinkedListNode(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    # Insert node at tail
    def insert_at_tail(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node
            self.length += 1
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        self.length += 1

    # Insert node at position
    def insert_at_position(self, value, position):
        new_node = LinkedListNode(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return
        current_node = self.head
        for _ in range(position-1):
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node
        self.length += 1
    
    # Delete node at head
    def delete_node_at_head(self):
        if self.head is None:
            raise Exception('Linked List is empty')
        self.head = self.head.next
        self.length -= 1
    
    # Delete node at tail
    def delete_node_at_tail(self):
        if self.head is None:
            raise Exception('Linked List is empty')
        if self.head.next is None:
            self.head = None
            self.length -= 1
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None
        self.length -= 1

    # Delete node at position
    def delete_node_at_position(self, position):
        if self.head is None:
            raise Exception('Linked List is empty')
        if position == 0:
            self.head = self.head.next
            self.length -= 1
            return
        current_node = self.head
        for _ in range(position-1):
            if current_node.next is None:
                raise Exception('Position is out of range')
            current_node = current_node.next
        current_node.next = current_node.next.next
        self.length -= 1
    
    # Create a deep copy of the linked list
    def create_deep_copy(self):
        if self.head is None:
            return None
        current_node = self.head
        new_linked_list = LinkedList()
        while current_node:
            new_linked_list.insert_at_tail(current_node.value)
            current_node = current_node.next
        return new_linked_list

    # print the linked list
    def print_list(self):
        print(str(self))
    
    # Convert the linked list to a string
    def __str__(self):
        current_node = self.head
        string = '['
        while current_node:
            if current_node.next is None:
                string += str(current_node.value)
                break
            string += str(current_node.value) + ', '
            current_node = current_node.next
        string += ']'
        return string
    
    # Convert the linked list to a list
    def to_list(self):
        current_node = self.head
        list = []
        while current_node:
            list.append(current_node.value)
            current_node = current_node.next
        return list
    
    # Convert the linked list to a list
    def __List__(self):
        return self.to_list()
    
    def __len__(self):
        return self.length
    
    def __iter__(self):
        self.current_node = self.head
        return self
    
    def __next__(self):
        self.current_node = self.current_node.next
        return self.current_node
    
    def __getitem__(self, index):
        if index >= self.length:
            raise Exception('Index out of range')
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node.value
    
    def __setitem__(self, index, value):
        if index >= self.length:
            raise Exception('Index out of range')
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        current_node.value = value

    def __delitem__(self, index):
        self.delete_node_at_position(index)
    
    def __contains__(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False
    
    def __search__(self, value):
        current_node = self.head
        i = 0 
        while current_node:
            if current_node.value == value:
                return i
            current_node = current_node.next
            i += 1
        return -1
    
    def __add__(self, other):
        if not isinstance(other, LinkedList):
            raise Exception('Cannot add non-LinkedList object')
        new_linked_list = LinkedList()
        current_node = self.head
        while current_node:
            new_linked_list.insert_at_tail(current_node.value)
            current_node = current_node.next
        current_node = other.head
        while current_node:
            new_linked_list.insert_at_tail(current_node.value)
            current_node = current_node.next
        return new_linked_list
    
    def __reverse__(self):
        current_node = self.head
        prev_node = None
        next_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def delete_value(self, value):
        if self.head is None:
            raise Exception('Linked List is empty')
        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                self.length -= 1
                return
            current_node = current_node.next
        raise Exception('Value not found')
    
    def delete_values(self, value):
        if self.head is None:
            raise Exception('Linked List is empty')
        while self.head.value == value:
            self.head = self.head.next
            self.length -= 1
        current_node = self.head
        while current_node.next:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                current_node = current_node.next
    
    def __eq__(self, other):
        if not isinstance(other, LinkedList):
            raise Exception('Cannot compare non-LinkedList object')
        if self.length != other.length:
            return False
        current_node = self.head
        other_node = other.head
        while current_node:
            if current_node.value != other_node.value:
                return False
            current_node = current_node.next
            other_node = other_node.next
        return True
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        if not isinstance(other, LinkedList):
            raise Exception('Cannot compare non-LinkedList object')
        if self.length >= other.length:
            return False
        current_node = self.head
        other_node = other.head
        while current_node:
            if current_node.value >= other_node.value:
                return False
            current_node = current_node.next
            other_node = other_node.next
        return True
    
    def __le__(self, other):
        if not isinstance(other, LinkedList):
            raise Exception('Cannot compare non-LinkedList object')
        if self.length > other.length:
            return False
        current_node = self.head
        other_node = other.head
        while current_node:
            if current_node.value > other_node.value:
                return False
            current_node = current_node.next
            other_node = other_node.next
        return True
    
    def __gt__(self, other):
        if not isinstance(other, LinkedList):
            raise Exception('Cannot compare non-LinkedList object')
        if self.length <= other.length:
            return False
        current_node = self.head
        other_node = other.head
        while current_node:
            if current_node.value <= other_node.value:
                return False
            current_node = current_node.next
            other_node = other_node.next
        return True
    
    def __ge__(self, other):
        if not isinstance(other, LinkedList):
            raise Exception('Cannot compare non-LinkedList object')
        if self.length < other.length:
            return False
        current_node = self.head
        other_node = other.head
        while current_node:
            if current_node.value < other_node.value:
                return False
            current_node = current_node.next
            other_node = other_node.next
        return True
    
    def __copy__(self):
        return self
    
    def __deepcopy__(self):
        return self.create_deep_copy()

    def __hash__(self):
        return hash(self.to_list())
    
    def __sub__(self, other):
        if not isinstance(other, LinkedList):
            raise Exception('Cannot subtract non-LinkedList object')
        new_linked_list = LinkedList()
        current_node = self.head
        while current_node:
            if current_node.value not in other:
                new_linked_list.insert_at_tail(current_node.value)
            current_node = current_node.next
        return new_linked_list

    def __sub_eq__(self, other):
        if not isinstance(other, LinkedList):
            raise Exception('Cannot subtract non-LinkedList object')
        current_node = self.head
        while current_node:
            if current_node.value in other:
                self.delete_value(current_node.value)
            current_node = current_node.next

    def __delete__(self):
        self.head = None
        self.length = 0