class LinkedListNode:
    value = None
    next_node = None

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def link(self, next_node):
        self.next_node = next_node
