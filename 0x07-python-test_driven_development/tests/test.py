#!/usr/bin/python3
import unittest
add_integer = __import__('../0-add_integer').add_integer

class Testy(unittest.TestCase):
    def test(self):
        self.assertTrue(1 == 1, "It's not ok")

add_integer(2, 5)
unittest.main()