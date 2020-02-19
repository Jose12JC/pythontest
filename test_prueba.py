import unittest

class tests(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_is_upper(self):

        self.assertTrue("FOO".isupper())
        self.assertFalse("foo".isupper())