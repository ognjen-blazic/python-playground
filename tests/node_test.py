import unittest

from data_structures.linked_list_node import LinkedListNode


class NodeTestCase(unittest.TestCase):
    def test_iterate_nodes(self):
        first_node = LinkedListNode(value=3)
        middle_node = LinkedListNode(value=5)
        last_node = LinkedListNode(value=7)

        node = first_node
        first_node.link(middle_node)
        middle_node.link(last_node)

        while node is not None:
            print(node.value)
            node = node.next_node

        self.assertIsNone(node)


if __name__ == '__main__':
    unittest.main()
