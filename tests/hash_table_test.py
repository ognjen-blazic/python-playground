import unittest

from data_structures.hash_table import HashTable


class HashTableTestCase(unittest.TestCase):
    def test_add(self):
        table = HashTable(10)

        table.add('a', 1)
        table.add('b', 2)
        table.add('c', 3)

        self.assertEqual(3, table.count)

    def test_dump_table_content(self):
        table = HashTable(10)

        table.add('a', 1)
        table.add('b', 2)
        table.add('c', 3)

        table.dump_table_content()

    def test_get(self):
        table = HashTable(10)

        table.add('a', 1)
        table.add('b', 2)
        table.add('c', 3)

        self.assertEqual(1, table.get('a'))
        self.assertEqual(2, table.get('b'))
        self.assertEqual(3, table.get('c'))
        self.assertIsNone(table.get('d'))

    def test_remove(self):
        table = HashTable(10)

        table.add('a', 1)
        table.add('b', 2)
        table.add('c', 3)
        table.remove('b')

        self.assertEqual(1, table.get('a'))
        self.assertEqual(3, table.get('c'))
        self.assertIsNone(table.get('b'))
        self.assertEqual(2, table.count)

    def test_capacity_exceeded(self):
        table = HashTable(2)

        table.add('a', 1)

        self.assertRaises(Exception, table.add, 'b', 2)


if __name__ == '__main__':
    unittest.main()
