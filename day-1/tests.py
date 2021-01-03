import unittest

from day1 import findpair, findtriple, readnums


class FindPairTestCase(unittest.TestCase):

    def test_call_findpair(self):
        findpair(2020, [1721, 299])

    def test_findpair_of_2020_in_1721_299(self):
        n = findpair(2020, [1721, 299])
        self.assertEqual(n, [1721, 299])

    def test_find_sum_of_3_in_5_2(self):
        n = findpair(3, [1, 5, 2])
        self.assertEqual(n, [1, 2])

    def test_find_sum_of_9_in_9_3_2_1_5(self):
        n = findpair(9, [9, 4, 1, 5])
        self.assertEqual(n, [4, 5])

    def test_find_sum_of_5_in_1_2_3_4_5(self):
        n = findpair(5, [1, 2, 3, 4, 5])
        self.assertEqual(n, [1, 4])

    def test_find_sum_of_22_in_12_8_2_9_14(self):
        n = findpair(22, [12, 8, 2, 9, 14])
        self.assertEqual(n, [8, 14])

    def test_find_sum_of_8_with_3_numbers_in_2_1_5_(self):
        n = findtriple(8, [2, 1, 5])
        self.assertEqual(sorted(n), [1, 2, 5])

    def test_find_sum_of_12_with_3_numbers_in_list(self):
        n = findtriple(12, [8, 1, 3, 5, 2])
        self.assertEqual(sorted(n), [1, 3, 8])

    def test_find_sum_of_27_with_3_numbers_in_list(self):
        n = findtriple(27, [8, 1, 20, 9, 2, 12, 7])
        self.assertEqual(sorted(n), [7, 8, 12])


class ReadNumsTestCase(unittest.TestCase):

    def test_call_readnums(self):
        readnums()

    def test_readnums_returns_list_of_numbers_from_tempfile(self):
        fname = '/tmp/numbers.txt'
        file = open(fname, 'w+')
        file.write('24\n98\n3\n')
        file.seek(0)
        file.close()
        nums = readnums(fname)
        self.assertEqual(nums, [24, 98, 3])
