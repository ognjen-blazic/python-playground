from data_structures.linked_list import LinkedList


class Stack:
    linked_list = LinkedList()

    def push(self, node):
        self.linked_list.add_end(node)

    def pop(self):
        if self.linked_list.count == 0:
            raise Exception('Stack has no items')
        item = self.linked_list.tail.value
        self.linked_list.remove_end()

        return item
