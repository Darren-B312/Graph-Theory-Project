import unittest
import regex


class TestRegex(unittest.TestCase):

    def test_match(self):
        self.assertEqual(regex.match("abc", "abc"), True)
        self.assertNotEqual(regex.match("abc", "aaaaa"), True)
        self.assertNotEqual(regex.match("abc", "abbc"), True)
        self.assertNotEqual(regex.match("abc", "a"), True)
        self.assertNotEqual(regex.match("abc", ""), True)

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
