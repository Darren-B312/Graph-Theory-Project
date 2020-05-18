import unittest
import regex


class TestRegex(unittest.TestCase):

    def test_match(self):
        # . concatenation
        # should match one and only one of each of the characters in the
        # order specified
        self.assertEqual(regex.match("abc", "abc"), True)
        self.assertEqual(regex.match("abc", "aaaaa"), False)
        self.assertEqual(regex.match("abc", "abbc"), False)
        self.assertEqual(regex.match("abc", "abcd"), False)
        self.assertEqual(regex.match("abc", "a"), False)
        self.assertEqual(regex.match("abc", ""), False)

        # * Kleene star
        # should match 0, 1 or many of the character
        self.assertEqual(regex.match("a*", ""), True)
        self.assertEqual(regex.match("a*", "a"), True)
        self.assertEqual(regex.match("a*", "aaaaaaaaaaa"), True)
        self.assertEqual(regex.match("a*", "b"), False)
        self.assertEqual(regex.match("a*", "ab"), False)
        self.assertEqual(regex.match("a*", "abc"), False)

        # +
        # should match 1 or more but not 0 of the character
        self.assertEqual(regex.match("a+", ""), False)
        self.assertEqual(regex.match("a+", "a"), True)
        self.assertEqual(regex.match("a+", "aaaaaaa"), True)
        self.assertEqual(regex.match("a+", "b"), False)
        self.assertEqual(regex.match("a+", "ab"), False)
        self.assertEqual(regex.match("a+", "aaaaaab"), False)

        # | alternation
        # should match either the character before or after but not both
        self.assertEqual(regex.match("a|b", "a"), True)
        self.assertEqual(regex.match("a|b", "b"), True)
        self.assertEqual(regex.match("a|b", "ab"), False)
        self.assertEqual(regex.match("a|b", "aaaaaa"), False)
        self.assertEqual(regex.match("a|b", "bbbbbb"), False)
        self.assertEqual(regex.match("a|b", "c"), False)

        # () grouping
        # can be used to apply precedence to a regular expression
        self.assertEqual(regex.match("a(bc*|d+)", "ab"), True)
        self.assertEqual(regex.match("a(bc*|d+)", "abc"), True)
        self.assertEqual(regex.match("a(bc*|d+)", "abcccccc"), True)
        self.assertEqual(regex.match("a(bc*|d+)", "ad"), True)
        self.assertEqual(regex.match("a(bc*|d+)", "adddddddddd"), True)
        self.assertEqual(regex.match("a(bc*|d+)", "bc"), False)


    def test_concat(self):
        self.assertEqual(regex.concat("abc"), "a.b.c")
        self.assertEqual(regex.concat("abc|(a+bc)"), "a.b.c|(a+.b.c)")
        self.assertEqual(regex.concat("(ab)+"), "(a.b)+")
        self.assertEqual(regex.concat("a(bc|d*)"), "a.(b.c|d*)")

    def test_shunt(self):
        self.assertEqual(regex.shunt("a.b.c"), "abc..")
        self.assertEqual(regex.shunt("a.b.c|(a+.b.c)"), "abc..a+bc..|")
        self.assertEqual(regex.shunt("(a.b)+"), "ab.+")
        self.assertEqual(regex.shunt("a.(b.c|d*)"), "abc.d*|.")


if __name__ == '__main__':
    unittest.main()
