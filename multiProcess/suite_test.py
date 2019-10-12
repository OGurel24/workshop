import unittest
from testAll import TestHome
from testAll import TestAbout
from multiprocessing import Pool


def run_test(test_to_run):
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_to_run)


tests = [TestHome('test_TC1'), TestHome('test_TC2'), TestHome('test_TC4')]

if __name__ == '__main__':
    with Pool(3) as p:
        p.map(run_test, tests)
