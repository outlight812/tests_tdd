import unittest
from calculator import *


class CalcTest(unittest.TestCase):
    def test_calc_available(self):
        app = Calculator()
        try:
             app.calc("1 + 3")
        except AttributeError:
            self.fail("функции calс не существует")

    def test_addition(self):
        app = Calculator()
        self.assertEqual(app.calc("2 + 3"),5)
        self.assertEqual(app.calc("-2 + 3"), 1)
        self.assertEqual(app.calc("2 + -3"), -1)
        self.assertEqual(app.calc("-2 + -3"), -5)

    def test_subtraction(self):
        app = Calculator()
        self.assertEqual(app.calc("2 - 3"),-1)
        self.assertEqual(app.calc("-2 - 3"),-5)
        self.assertEqual(app.calc("2 - -3"),5)
        self.assertEqual(app.calc("-2 - -3"),1)

    def test_multiplication(self):
        app = Calculator()
        self.assertEqual(app.calc("2 * 3"),6)
        self.assertEqual(app.calc("-2 * 3"), -6)
        self.assertEqual(app.calc("2 * -3"), -6)
        self.assertEqual(app.calc("-2 * -3"), 6)

    def test_division(self):
        app = Calculator()
        self.assertEqual(app.calc("2 / 2"),1)
        self.assertEqual(app.calc("-2 / 2"), -1)
        self.assertEqual(app.calc("2 / -2"), -1)
        self.assertEqual(app.calc("-2 / -2"), 1)

    def test_power(self):
        app = Calculator()
        self.assertEqual(app.calc("2 ** 3"), 8)
        self.assertEqual(app.calc("-2 ** 3"), -8)
        self.assertEqual(app.calc("2 ** -3"), 0.125)
        self.assertEqual(app.calc("-2 ** -3"), -0.125)

class InputTest(unittest.TestCase):
    def test_input_available(self):
        app = Calculator()
        try:
            app.input("1 + 1")
        except AttributeError:
            self.fail("функции input не существует")

    def test_input_valid(self):
        app = Calculator()
        self.assertEqual(app.input("2 * 3"),[2,"*",3])
        self.assertEqual(app.input("-2 * 3"),[-2,"*",3])
        self.assertEqual(app.input("2 * -3"),[2,"*",-3])
        self.assertEqual(app.input("-2 * -3"),[-2,"*",-3])

    def test_input_invalid(self):
        app = Calculator()
        with self.assertRaises(ValueError):
            app.input("fdl")
        with self.assertRaises(ValueError):
            app.input("2.23 * 1")
        with self.assertRaises(ValueError):
            app.input("2 ! 4")
        with self.assertRaises(ValueError):
            app.input("3 3")







if __name__ == '__main__':
    unittest.main()
