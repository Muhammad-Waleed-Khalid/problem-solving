class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def str(self):
        current_node = self
        string = '['
        while current_node:
            if current_node.next is None:
                string += str(current_node.value)
                break
            string += str(current_node.value) + ', '
            current_node = current_node.next
        string += ']'
        return string
    
    def to_list(self):
        current_node = self
        list = []
        while current_node:
            list.append(current_node.value)
            current_node = current_node.next
        return list