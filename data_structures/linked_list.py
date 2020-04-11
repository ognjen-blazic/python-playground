class LinkedList:
    head = None
    tail = None
    count = 0

    def add_front(self, node):
        old_head = self.head
        self.head = node
        self.head.next = old_head
        self.count = self.count + 1

        if self.count == 1:
            self.tail = self.head

    def add_end(self, node):
        if self.count == 0:
            self.head = node
        else:
            self.tail.next = node

        self.count = self.count + 1
        self.tail = node

    def remove_end(self):
        if self.count == 0:
            return

        if self.count == 1:
            self.head = None
            self.tail = None
            self.count = 0
            return

        current_node = self.head
        while current_node.next is not self.tail:
            current_node = current_node.next

        current_node.next = None
        self.tail = current_node
        self.count = self.count - 1

    def remove_front(self):
        self.head = self.head.next
        self.count = self.count - 1

        if self.count == 0:
            self.tail = None
