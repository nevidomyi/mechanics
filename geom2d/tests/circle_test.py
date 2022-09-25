import math
import unittest

from geom2d.circle import Circle
from geom2d.point import Point
# from geom2d.polygon import Polygon
# from geom2d.vector import Vector


class TestCircle(unittest.TestCase):
    circle = Circle(Point(10, 10), 10)

    def test_area(self):
        expected = math.pi * 100
        self.assertAlmostEqual(expected, self.circle.area)

    def test_circumference(self):
        expected = math.pi * 20
        self.assertAlmostEqual(expected, self.circle.circumference)

    # def test_contains_point(self):
    #     point = Point(11, 12)
    #     self.assertTrue(self.circle.contains_point(point))
