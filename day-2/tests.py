import unittest

from password import (is_valid,
                      parse_policy,
                      parse_password,
                      count_valid,
                      is_valid_pos)


class PasswordValidationByPositionTestCase(unittest.TestCase):

    def test_validate_2_char_valid(self):
        pwd = 'ab'
        policy = {'a': [1, 2]}
        self.assertTrue(is_valid_pos(pwd, policy))

    def test_validate_2_char_invalid(self):
        pwd = 'aa'
        policy = {'a': [1, 2]}
        self.assertFalse(is_valid_pos(pwd, policy))

    def test_validate_5_char_valid(self):
        pwd = 'abcdef'
        policy = {'a': [1, 4]}
        self.assertTrue(is_valid_pos(pwd, policy))

    def test_validate_5_char_with_repetition_valid(self):
        pwd = 'abbca'
        policy = {'a': [1, 4]}
        self.assertTrue(is_valid_pos(pwd, policy))

    def test_validate_5_char_with_repetition_invalid(self):
        pwd = 'booze'
        policy = {'o': [2, 3]}
        self.assertFalse(is_valid_pos(pwd, policy))


class PasswordValidationTestCase(unittest.TestCase):

    def test_validate_1_char_valid(self):
        pwd = 'a'
        policy = {'a': [1, 2]}
        self.assertTrue(is_valid(pwd, policy))

    def test_validate_1_char_invalid(self):
        pwd = 'b'
        policy = {'a': [1, 2]}
        self.assertFalse(is_valid(pwd, policy))

    def test_validate_2_char_valid(self):
        pwd = 'ab'
        policy = {'a': [1, 2], 'b': [1, 2]}
        self.assertTrue(is_valid(pwd, policy))

    def test_validate_2_char_invalid(self):
        pwd = 'cd'
        policy = {'a': [1, 2], 'b': [1, 2]}
        self.assertFalse(is_valid(pwd, policy))

    def test_validate_2_char_invalid_too_many(self):
        pwd = 'aaab'
        policy = {'a': [1, 2], 'b': [1, 2]}
        self.assertFalse(is_valid(pwd, policy))

    def test_validate_3_char_valid(self):
        pwd = 'bazookaaaaa'
        policy = {'a': [1, 6], 'o': [2, 3], 'k': [1, 2], 'b': [1, 2]}
        self.assertTrue(is_valid(pwd, policy))

class PolicyParserTestCase(unittest.TestCase):

    def test_parse_1_2_policy(self):
        policy = '1-2 a'
        expected = {'a': [1, 2]}
        self.assertEqual(parse_policy(policy), expected)

    def test_parse_3_6_policy(self):
        policy = '3-6 b'
        expected = {'b': [3, 6]}
        self.assertEqual(parse_policy(policy), expected)


class PasswordParserTestCase(unittest.TestCase):

    def test_parse_abc_1_6_a_password(self):
        input_ = '1-6 a: abc'
        out = ('abc', {'a': [1, 6]})
        self.assertEqual(parse_password(input_), out)

    def test_parse_abcde_1_2_b_password(self):
        input_ = '1-2 b: abcde'
        out = ('abcde', {'b': [1, 2]})
        self.assertEqual(parse_password(input_), out)


class ValidCountTestCase(unittest.TestCase):

    def test_count_1_valid_out_of_1(self):
        pwds = [('abc', {'b': [1, 2]})]
        valid_count = 1
        self.assertEqual(count_valid(pwds), valid_count)

    def test_count_1_valid_out_of_2(self):
        pwds = [
            ('abc', {'b': [1, 2]}),
            ('def', {'g': [1, 2]})  # invalid: missing g
        ]
        valid_count = 1
        self.assertEqual(count_valid(pwds), valid_count)

    def test_count_2_valid_out_of_2(self):
        pwds = [
            ('abc', {'b': [1, 2]}),
            ('defg', {'g': [1, 2]})
        ]
        valid_count = 2
        self.assertEqual(count_valid(pwds), valid_count)

    def test_count_2_valid_out_of_3(self):
        pwds = [
            ('abc', {'b': [1, 2]}),
            ('defg', {'g': [1, 2]}),
            ('abc', {'k': [1, 2]}),  # invalid: missing k
        ]
        valid_count = 2
        self.assertEqual(count_valid(pwds), valid_count)
