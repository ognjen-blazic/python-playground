import unittest

from data_structures.node import Node


class NodeTestCase(unittest.TestCase):
    def test_iterate_nodes(self):
        first_node = Node(value=3)
        middle_node = Node(value=5)
        last_node = Node(value=7)

        node = first_node
        first_node.link(middle_node)
        middle_node.link(last_node)

        while node is not None:
            print(node.value)
            node = node.next_node

        self.assertIsNone(node)


if __name__ == '__main__':
    unittest.main()
