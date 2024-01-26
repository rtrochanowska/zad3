import unittest
from program import sum
from program import multiply

class Test_program(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
    def test_sum_zero(self):
        self.assertEqual(multiply(0, 0), 0)
    def test_sum(self):
        self.assertEqual(sum(-4, 6), 2)

if __name__ == '__main__':
    unittest.main()
