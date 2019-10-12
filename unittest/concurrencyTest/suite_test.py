import unittest
from testAll import TestHome
from testAll import TestAbout
from concurrencytest import ConcurrentTestSuite, fork_for_tests


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
    concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(3))
    runner.run(concurrent_suite)
