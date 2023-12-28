import unittest

from main import *

class TestSolutions(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle("синего", 3, 2)
        self.circle = Circle("зеленого", 5)
        self.square = Square("красного", 5)
    def test_task1_solution(self):
        result = self.rectangle.__repr__()
        self.assertEqual(
            result, 'Прямоугольник синего цвета шириной 3 и высотой 2 площадью 6.'
        )

    def test_task2_solution(self):
        result = self.circle.__repr__()
        self.assertEqual(
            result, 'Круг зеленого цвета радиусом 5 площадью 78.53981633974483.'
        )

    def test_task3_solution(self):
        result = self.square.__repr__()
        self.assertEqual(
            result, 'Квадрат красного цвета со стороной 5 площадью 25.'
        )

if __name__ == '__main__':
    unittest.main()