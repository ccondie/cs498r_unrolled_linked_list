# from __future__ import absolute_import

from ..unrolled_linked_list.module import UnrolledLinkedList
import unittest


class UnrolledLinkedList_Test(unittest.TestCase):
    """

    """

    def setUp(self):
        self.l = UnrolledLinkedList()
        # create a unrolled linked list with one node with 5 elements 0-4
        for i in range(0, 5):
            self.l.append(i)

    def tearDown(self):
        del self.l

    """
    MISC TESTS
    """

    def test_default_node_capacity(self):
        """Test that the default node capacity is being set, and is set to 16
        """
        self.assertEqual(self.l.max_node_capacity, 16)

    def test_length(self):
        self.assertEqual(len(self.l), 5)

    """
    GET ITEM TESTS
    """

    def test_get_item_single_node(self):
        # check that index 1 is 1 [0, |1|, 2, 3, 4]
        self.assertEqual(self.l[1], 1)

    def test_get_item_single_node_neg_index(self):
        # check that the second to last el is 3 [0, 1, 2, |3| ,4]
        self.assertEqual(self.l[-2], 3)

    def test_get_item_exception(self):
        # attempt to get an item outside of max index
        with self.assertRaises(IndexError) as cm:
            dummy = self.l[self.l.length + 1]

    def test_get_item_two_node(self):
        self.l.max_node_capacity = 5
        for i in range(5, 7):
            self.l.append(i)
        self.assertEqual(self.l[5], 5)

    def test_get_item_two_node_neg_index(self):
        self.l.max_node_capacity = 5
        for i in range(5, 7):
            self.l.append(i)
        self.assertEqual(self.l[-1], 6)

    """
    SET ITEM TESTS
    """

    def test_set_item(self):
        self.assertEqual(self.l[2], 2)
        self.l[2] = 100
        self.assertEqual(self.l[2], 100)

    def test_set_item_neg_index(self):
        self.assertEqual(self.l[-2], 3)
        self.l[-2] = 100
        self.assertEqual(self.l[-2], 100)

    def test_set_item_exception(self):
        with self.assertRaises(IndexError) as cm:
            self.l[self.l.length + 1] = 5

    def test_set_item_two_node(self):
        self.l.max_node_capacity = 5
        for i in range(5, 7):
            self.l.append(i)
        self.assertEqual(self.l[6], 6)
        self.l[6] = 100
        self.assertEqual(self.l[6], 100)

    """
    ITER TESTS
    """

    def test_iter(self):
        cur_index = 0
        for el in self.l:
            self.assertEqual(el, self.l[cur_index])
            cur_index += 1

    """
    REVERSE TESTS
    """

    def test_reverse(self):
        cur_index = self.l.length - 1
        for el in reversed(self.l):
            self.assertEqual(el, self.l[cur_index])
            cur_index -= 1

    """
    DELETE ITEM TESTS
    """

    def test_del_item(self):
        # check that index 1 is 1
        self.assertEqual(self.l[1], 1)
        # delete el 1 at index 1
        del self.l[1]
        # check that index 1 is now 2
        self.assertEqual(self.l.length, 4)
        self.assertEqual(self.l[1], 2)

    def test_del_item_exception(self):
        with self.assertRaises(IndexError) as cm:
            del self.l[7]

    def test_del_item_neg_index(self):
        # check that the second to last index i 4 [0, 1, 2, 3, 4]
        self.assertEqual(self.l[-2], 3)
        # delete the second to last element [0, 1, 2, |3|, 4]
        del self.l[-2]
        # check that the second to last index is now 2 [0, 1, |2|, 4]
        self.assertEqual(self.l.length, 4)
        self.assertEqual(self.l[-2], 2)

    def test_del_item_two_node_single(self):
        self.l.max_node_capacity = 5
        for i in range(5, 7):
            self.l.append(i)
        # [0, 1, 2, 3, 4, |5|, 6]
        self.assertEqual(self.l[5], 5)
        del self.l[5]
        # [0, 1, 2, 3, 4, |6|]
        self.assertEqual(self.l[5], 6)

    # NEEDS WORK
    def test_del_item_delete_last_node(self):
        self.l.max_node_capacity = 5
        self.l.append(5)
        # {[0, 1], [2, 3, 4, 5}
        self.assertEqual(len(self.l.nodeList), 2)
        # delete nodes in the last node until the whole node is gone
        del self.l[5]
        del self.l[4]
        del self.l[3]
        del self.l[2]
        self.assertEqual(len(self.l.nodeList), 1)

    def test_del_item_balance(self):
        self.r = UnrolledLinkedList()
        self.r.max_node_capacity = 5
        for i in range(0, 10):
            self.r.append(i)
        del self.r[0]
        del self.r[0]
        del self.r[0]

    def test_max_6(self):
        self.l.max_node_capacity = 6
        for i in range(5, 20):
            self.l.append(i)

        print(self.l)
        del self.l[4]
        print(str(self.l))


    """
    APPEND TESTS
    """

    def test_append(self):
        # shrink the max capacity to something more manageable
        self.l.max_node_capacity = 5
        self.assertEqual(self.l.length, 5)
        # add element 5
        self.l.append(5)
        self.assertEqual(self.l.length, 6)
        self.assertEqual(str(self.l), '{[0, 1, 2], [3, 4, 5]}')

    """
    CONTAINS TESTS
    """
    def test_contains_true(self):
        var = False
        if 3 in self.l:
            var = True
        self.assertTrue(var)

    def test_contains_false(self):
        var = False
        if 10 not in self.l:
            var = True
        self.assertTrue(var)
