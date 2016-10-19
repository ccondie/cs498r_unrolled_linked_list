''' You will need the following import if using python2 '''
# from __future__ import absolute_import

from ..unrolled_linked_list.module import UnrolledLinkedList
import unittest


class UnrolledLinkedList_Test(unittest.TestCase):
    """

    """

    def setUp(self):
        self.l = UnrolledLinkedList()
        # create a unrolled linked list with one node with 5 elements 1-5
        for i in range(1, 6):
            self.l.append(i)

    def tearDown(self):
        del self.l

    """
    Begin Unit Tests
    """

    def test_default_node_capacity(self):
        """Test that the default node capacity is being set, and is set to 16
        """
        self.assertEqual(self.l.max_node_capacity, 16)

    def test_get_item(self):
        self.assertEqual(self.l[1], 2)
        self.assertEqual(self.l[-2], 4)
        with self.assertRaises(IndexError) as cm:
            dummy = self.l[10]

    def test_del_item(self):
        self.assertEqual(self.l[1], 2)
        del self.l[1]
        self.assertEqual(self.l[1], 3)
        self.assertEqual(self.l[-2], 4)
        del self.l[-2]
        self.assertEqual(self.l[-2], 3)
        with self.assertRaises(IndexError) as cm:
            del self.l[5]

    def test_append(self):
        # shrink the max capacity to something more manageable
        self.l.max_node_capacity = 6
        self.assertEqual(self.l.length, 5)
        # add element 6
        self.l.append(6)
        self.assertEqual(self.l.length, 6)
