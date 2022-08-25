import math
import unittest

from geom2d.point import Point
from geom2d.segment import Segment


class TestSegment(unittest.TestCase):

    start = Point(400, 0)
    end = Point(0, 400)
    segment = Segment(start, end)

    def test_length(self):
        expected = 400 * math.sqrt(2)
        actual = self.segment.length
        self.assertAlmostEqual(expected, actual)
