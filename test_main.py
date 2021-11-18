import unittest
from unittest import TestCase
import main


class Test(TestCase):
    def test_capitalize(self):
        self.assertEqual(main.CAPITALIZE("foo"), "FOO")


if __name__ == 'main':
    unittest.main()
