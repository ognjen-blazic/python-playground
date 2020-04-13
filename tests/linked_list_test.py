import unittest

from data_structures.linked_list import LinkedList
from data_structures.linked_list_node import LinkedListNode


class LinkedListTestCase(unittest.TestCase):
    def test_add_front(self):
        linked_list = LinkedList()

        linked_list.add_front(LinkedListNode(5))
        linked_list.add_front(LinkedListNode(3))
        linked_list.add_front(LinkedListNode(1))

        current_node = linked_list.head
        while current_node is not linked_list.tail:
            print(current_node.value)
            current_node = current_node.next_node
        print(current_node.value)

        self.assertEqual(3, linked_list.count)

    def test_add_end(self):
        linked_list = LinkedList()

        linked_list.add_end(LinkedListNode(1))
        linked_list.add_end(LinkedListNode(3))
        linked_list.add_end(LinkedListNode(5))

        current_node = linked_list.head
        while current_node is not linked_list.tail:
            print(current_node.value)
            current_node = current_node.next_node
        print(current_node.value)

        self.assertEqual(3, linked_list.count)

    def test_remove_front(self):
        linked_list = LinkedList()

        linked_list.add_end(LinkedListNode(1))
        linked_list.add_end(LinkedListNode(3))
        linked_list.add_end(LinkedListNode(5))

        linked_list.remove_front()

        current_node = linked_list.head
        while current_node is not linked_list.tail:
            print(current_node.value)
            current_node = current_node.next_node
        print(current_node.value)

        self.assertEqual(2, linked_list.count)

    def test_remove_end(self):
        linked_list = LinkedList()

        linked_list.add_end(LinkedListNode(1))
        linked_list.add_end(LinkedListNode(3))
        linked_list.add_end(LinkedListNode(5))

        linked_list.remove_end()
        linked_list.remove_end()
        linked_list.remove_end()

        self.assertEqual(0, linked_list.count)

    def test_contains_true(self):
        linked_list = LinkedList()

        linked_list.add_end(LinkedListNode(1))
        linked_list.add_end(LinkedListNode(3))
        linked_list.add_end(LinkedListNode(5))

        self.assertTrue(linked_list.contains(3))

    def test_contains_false(self):
        linked_list = LinkedList()

        linked_list.add_end(LinkedListNode(1))
        linked_list.add_end(LinkedListNode(3))
        linked_list.add_end(LinkedListNode(5))

        self.assertFalse(linked_list.contains(4))


if __name__ == '__main__':
    unittest.main()
