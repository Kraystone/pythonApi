import unittest


def CAPITALIZE(chaine):
    return chaine.upper()


class Test(unittest.TestCase):
    def CAPITALIZETest(self):
        self.assertEqual(CAPITALIZE("foo"), "FOO")
        self.assertEqual(CAPITALIZE("foo"), "FOO")

    def input_value(self):
        self.assertRaises(TypeError)


if __name__ == 'main':
    unittest.main()
