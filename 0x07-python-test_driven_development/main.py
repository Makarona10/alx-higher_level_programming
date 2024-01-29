import unittest
print_square = __import__('4-print_square').print_square

class Testy(unittest.TestCase):
    def test(self):
        self.assertEqual(1, 1,"It's not ok")

print_square()