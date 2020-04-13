from data_structures.linked_list import LinkedList


class Queue:
    linked_list = LinkedList()

    def enqueue(self, value):
        self.linked_list.add_end(value)

    def dequeue(self):
        if self.linked_list.count == 0:
            raise Exception('Q has no items')

        item = self.linked_list.head.value
        self.linked_list.remove_front()

        return item
