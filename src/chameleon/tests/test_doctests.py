import unittest
import doctest

OPTIONFLAGS = (doctest.ELLIPSIS |
               doctest.NORMALIZE_WHITESPACE |
               doctest.REPORT_ONLY_FIRST_FAILURE)


class DoctestCase(unittest.TestCase):
    def __new__(self, test):
        return getattr(self, test)()

    @classmethod
    def test_tal(cls):
        from chameleon import tal
        return doctest.DocTestSuite(
            tal, optionflags=OPTIONFLAGS)

    @classmethod
    def test_tales(cls):
        from chameleon import tales
        return doctest.DocTestSuite(
            tales, optionflags=OPTIONFLAGS)

    @classmethod
    def test_utils(cls):
        from chameleon import utils
        return doctest.DocTestSuite(
            utils, optionflags=OPTIONFLAGS)
