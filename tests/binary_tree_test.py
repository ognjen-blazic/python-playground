import unittest

from data_structures.binary_tree import BinaryTree


class BinaryTreeTestCase(unittest.TestCase):
    def test_add(self):
        tree = BinaryTree()

        tree.add(4)
        tree.add(2)
        tree.add(6)
        tree.add(1)
        tree.add(3)
        tree.add(5)
        tree.add(7)
        tree.add(8)
        tree.add(0)

        self.assertEqual(9, tree.count)

    def test_in_order_traversal(self):
        tree = BinaryTree()

        tree.add(4)
        tree.add(2)
        tree.add(6)
        tree.add(1)
        tree.add(3)
        tree.add(5)
        tree.add(7)
        tree.add(7)
        tree.add(8)
        tree.add(0)
        tree.add(2)

        tree.in_order_traversal(tree.head)

    def test_contains_true(self):
        tree = BinaryTree()

        tree.add(4)
        tree.add(2)
        tree.add(6)
        tree.add(1)
        tree.add(3)

        self.assertTrue(tree.contains(6))

    def test_contains_false(self):
        tree = BinaryTree()

        tree.add(4)
        tree.add(2)
        tree.add(6)
        tree.add(1)
        tree.add(3)

        self.assertFalse(tree.contains(5))


if __name__ == '__main__':
    unittest.main()
