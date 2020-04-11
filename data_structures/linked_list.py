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
