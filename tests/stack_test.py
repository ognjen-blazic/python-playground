import unittest

from data_structures.stack import Stack


class StackTestCase(unittest.TestCase):
    def test_push(self):
        stack = Stack()

        stack.push(1)
        stack.push(3)
        stack.push(5)

        self.assertEqual(3, stack.linked_list.count)

    def test_pop(self):
        stack = Stack()

        stack.push(1)
        stack.push(3)
        stack.push(5)

        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(0, stack.linked_list.count)

    def test_pop_on_empty_stack(self):
        stack = Stack()

        self.assertRaises(Exception, stack.pop)


if __name__ == '__main__':
    unittest.main()
