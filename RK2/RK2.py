import sys
sys.path.append('./RK1')
import RK1
from operator import itemgetter
import unittest

class Test(unittest.TestCase):
    def test_first_task(self):
        test_list = [("Ivanov", 1, "A"), ("Petrov", 2, "B"), ("Sidorov", 3, "C")]
        self.assertEqual(RK1.first_task(test_list), sorted(test_list, key=itemgetter(0)))

    def test_second_task(self):
        test_list = [("Ivanov", 1, "A"), ("Petrov", 2, "B"), ("Sidorov", 3, "C")]
        self.assertEqual(RK1.second_task(test_list), [("A", 1), ("B", 1), ("C", 1)])

    def test_third_task(self):
        test_list = [("Ivanov", "A"), ("Petrov", "B"), ("Sidorov", "C")]
        self.assertEqual(RK1.third_task(test_list, "ov"), [("Ivanov", "A"), ("Petrov", "B"), ("Sidorov", "C")])

if __name__ == "__main__":
    unittest.main()