import unittest
from lab1_proc import get_roots

class TestGetRoots(unittest.TestCase):
    def test_get_roots(self):
        self.assertEqual([1, -1], get_roots(1, -2, 1), msg = "Wrong roots")
    def test_get_roots2(self):
        self.assertEqual([], get_roots(1, 2, 1), msg = "Wrong roots")
    def test_get_roots3(self):
        self.assertEqual([0], get_roots(1, 0, 0), msg = "Wrong roots")

if __name__ == '__main__':
    unittest.main()