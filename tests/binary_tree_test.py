import unittest

from data_structures.binary_tree import BinaryTree
from data_structures.binary_tree_node import BinaryTreeNode


class BinaryTreeTestCase(unittest.TestCase):
    def test_add(self):
        tree = BinaryTree()

        tree.add(BinaryTreeNode(4))
        tree.add(BinaryTreeNode(2))
        tree.add(BinaryTreeNode(6))
        tree.add(BinaryTreeNode(1))
        tree.add(BinaryTreeNode(3))
        tree.add(BinaryTreeNode(5))
        tree.add(BinaryTreeNode(7))
        tree.add(BinaryTreeNode(8))
        tree.add(BinaryTreeNode(0))

        self.assertEqual(9, tree.count)

    def test_in_order_traversal(self):
        tree = BinaryTree()

        tree.add(BinaryTreeNode(4))
        tree.add(BinaryTreeNode(2))
        tree.add(BinaryTreeNode(6))
        tree.add(BinaryTreeNode(1))
        tree.add(BinaryTreeNode(3))
        tree.add(BinaryTreeNode(5))
        tree.add(BinaryTreeNode(7))
        tree.add(BinaryTreeNode(7))
        tree.add(BinaryTreeNode(8))
        tree.add(BinaryTreeNode(0))
        tree.add(BinaryTreeNode(2))

        tree.in_order_traversal(tree.head)

    def test_contains_true(self):
        tree = BinaryTree()

        tree.add(BinaryTreeNode(4))
        tree.add(BinaryTreeNode(2))
        tree.add(BinaryTreeNode(6))
        tree.add(BinaryTreeNode(1))
        tree.add(BinaryTreeNode(3))

        self.assertTrue(tree.contains(6))

    def test_contains_false(self):
        tree = BinaryTree()

        tree.add(BinaryTreeNode(4))
        tree.add(BinaryTreeNode(2))
        tree.add(BinaryTreeNode(6))
        tree.add(BinaryTreeNode(1))
        tree.add(BinaryTreeNode(3))

        self.assertFalse(tree.contains(5))


if __name__ == '__main__':
    unittest.main()
