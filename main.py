import unittest
from rectangle import *
from square import *
from triangle import *
from circle import *

class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(10, 0), 0)
        self.assertEqual(rectangle_area(10, 10), 100)
        self.assertEqual(rectangle_area(1, 55676865462), 55676865462)
        self.assertEqual(rectangle_area(1000000, 10000), 10000000000)
        self.assertEqual(rectangle_area(1, 1), 1)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(0, 0), 0)
        self.assertEqual(rectangle_perimeter(100, 100), 400)
        self.assertEqual(rectangle_perimeter(1, 9), 20)
        self.assertEqual(rectangle_perimeter(100000000, 1), 200000002)
        self.assertEqual(rectangle_perimeter(52, 52), 208)

class CircleTestCase(unittest.TestCase):
    def test_circle_area(self):
        self.assertEqual(circle_area(1), math.pi)
        self.assertEqual(circle_area(100000), 10000000000 * math.pi)
        self.assertEqual(circle_area(25), 625 * math.pi)
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(0.1), 0.01 * math.pi)

    def test_circle_perimeter(self):
        self.assertEqual(circle_perimeter(1), 2 * math.pi)
        self.assertEqual(circle_perimeter(1 / math.pi), 2)
        self.assertEqual(circle_perimeter(0), 0)
        self.assertEqual(circle_perimeter(52), 104 * math.pi)
        self.assertEqual(circle_perimeter(0.01), 0.02 * math.pi)

class SquareTestCase(unittest.TestCase):
    def test_square_area(self):
        self.assertEqual(square_area(1), 1)
        self.assertEqual(square_area(2), 4)
        self.assertEqual(square_area(100000), 10000000000)
        self.assertEqual(square_area(8), 64)
        self.assertEqual(square_area(0), 0)

    def test_square_perimeter(self):
        self.assertEqual(square_perimeter(1), 4)
        self.assertEqual(square_perimeter(10000), 40000)
        self.assertEqual(square_perimeter(-1), -4)
        self.assertEqual(square_perimeter(0), 0)
        self.assertEqual(square_perimeter(8), 32)

class TriangleTestCase(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(triangle_area(5, 4), 10)
        self.assertEqual(triangle_area(0, 4), 0)
        self.assertEqual(triangle_area(1, 2), 1)
        self.assertEqual(triangle_area(-1, -2), 1)
        self.assertEqual(triangle_area(52, 4), 104)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle_perimeter(0, 0, 0), 0)
        self.assertEqual(triangle_perimeter(1, 1, 1), 3)
        self.assertEqual(triangle_perimeter(200, 300, 400), 900)
        self.assertEqual(triangle_perimeter(252, 312, 499), 1063)
        self.assertEqual(triangle_perimeter(25, 50, 60), 135)

