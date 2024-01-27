import unittest
matrix_divided = __import__('2-matrix_divided').matrix_divided

class Testy(unittest.TestCase):
    def test(self):
        self.assertEqual(1, 1,"It's not ok")

matrix_divided([[1, 5], "damn"], 1)