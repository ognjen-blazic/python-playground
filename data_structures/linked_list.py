class LinkedList:
    head = None
    tail = None
    count = 0

    def add_front(self, node):
        old_head = self.head
        self.head = node
        self.head.next_node = old_head
        self.count = self.count + 1

        if self.count == 1:
            self.tail = self.head

    def add_end(self, node):
        if self.count == 0:
            self.head = node
        else:
            self.tail.next_node = node

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
        while current_node.next_node is not self.tail:
            current_node = current_node.next_node

        current_node.next_node = None
        self.tail = current_node
        self.count = self.count - 1

    def remove_front(self):
        self.head = self.head.next_node
        self.count = self.count - 1

        if self.count == 0:
            self.tail = None

    def contains(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_node

        return False
