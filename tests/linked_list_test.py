import unittest

from data_structures.linked_list import LinkedList
from data_structures.node import Node


class LinkedListTestCase(unittest.TestCase):
    def test_add_front(self):
        linked_list = LinkedList()

        linked_list.add_front(Node(5))
        linked_list.add_front(Node(3))
        linked_list.add_front(Node(1))

        current_node = linked_list.head
        while current_node is not linked_list.tail:
            print(current_node.value)
            current_node = current_node.next
        print(current_node.value)

        self.assertEqual(3, linked_list.count)

    def test_add_end(self):
        linked_list = LinkedList()

        linked_list.add_end(Node(1))
        linked_list.add_end(Node(3))
        linked_list.add_end(Node(5))

        current_node = linked_list.head
        while current_node is not linked_list.tail:
            print(current_node.value)
            current_node = current_node.next
        print(current_node.value)

        self.assertEqual(3, linked_list.count)

    def test_remove_front(self):
        linked_list = LinkedList()

        linked_list.add_end(Node(1))
        linked_list.add_end(Node(3))
        linked_list.add_end(Node(5))

        linked_list.remove_front()

        current_node = linked_list.head
        while current_node is not linked_list.tail:
            print(current_node.value)
            current_node = current_node.next
        print(current_node.value)

        self.assertEqual(2, linked_list.count)

    def test_remove_end(self):
        linked_list = LinkedList()

        linked_list.add_end(Node(1))
        linked_list.add_end(Node(3))
        linked_list.add_end(Node(5))

        linked_list.remove_end()
        linked_list.remove_end()
        linked_list.remove_end()

        self.assertEqual(0, linked_list.count)


if __name__ == '__main__':
    unittest.main()
