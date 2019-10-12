import unittest
from testAll import TestHome
from testAll import TestAbout


def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestHome('test_TC1'))
    suite.addTest(TestHome('test_TC4'))
    suite.addTest(TestHome('test_TC2'))

    suite.addTest(TestAbout('test_TC3'))
    suite.addTest(TestAbout('test_TC5'))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=3)
    suite = suite()
    runner.run(suite)
