from data_structures.binary_tree_node import BinaryTreeNode


class BinaryTree:
    head = None
    count = 0

    def add(self, value):
        node = BinaryTreeNode(value)
        if self.head is None:
            self.head = node
            self.count = 1
            return

        self.link(self.head, node)
        self.count = self.count + 1

    def link(self, current_head, node):
        if node.value < current_head.value:
            if current_head.left is None:
                current_head.left = node
            else:
                self.link(current_head.left, node)
        else:  # equal values are considered as "greater"
            if current_head.right is None:
                current_head.right = node
            else:
                self.link(current_head.right, node)

    def contains(self, value):
        current = self.head

        while current is not None:
            if current.value == value:  # TODO: use equals or compare
                return True

            if value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def in_order_traversal(self, node):
        if node is None:
            return
        self.in_order_traversal(node.left)
        print(node.value)
        self.in_order_traversal(node.right)
