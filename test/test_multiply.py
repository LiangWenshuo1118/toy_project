import unittest
from my_package.multiply.multiply import multiply_numbers

class TestSum(unittest.TestCase):
    def test_sum_numbers(self):
        self.assertEqual(multiply_numbers([1, 2, 3]), 6)
        self.assertEqual(multiply_numbers([-1, 1]), -1)
        self.assertEqual(multiply_numbers([2]*10), 1024)

if __name__ == '__main__':
    unittest.main()
