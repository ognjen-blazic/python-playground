import unittest

from data_structures.queue import Queue


class QueueTestCase(unittest.TestCase):
    def test_enqueue(self):
        q = Queue()

        q.enqueue(1)
        q.enqueue(3)
        q.enqueue(5)

        self.assertEqual(3, q.linked_list.count)

    def test_dequeue(self):
        q = Queue()

        q.enqueue(1)
        q.enqueue(3)
        q.enqueue(5)

        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(0, q.linked_list.count)

    def test_dequeue_on_empty_queue(self):
        q = Queue()

        self.assertRaises(Exception, q.dequeue)


if __name__ == '__main__':
    unittest.main()
