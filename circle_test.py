import unittest
from math import pi
from Circle.arc_length import arc_length
from Circle.area import area
from Circle.circumference import circumference
from Circle.diameter import diameter_a, diameter_c
from Circle.radius import radius
from Circle.sector_area import sector_area


class TestCircle(unittest.TestCase):
    def test_circumference(self):
        self.assertEqual(circumference(1/pi), 2.0)

    def test_radius(self):
        self.assertEqual(radius(2 * pi), 1.0)

    def test_area(self):
        self.assertEqual(area(1), pi)

    def test_sector_area(self):
        self.assertEqual(sector_area((1/pi), 6), 0.1)

    def test_diameter_a(self):
        self.assertEqual(diameter_a(pi), 2.0)

    def test_diameter_c(self):
        self.assertEqual(diameter_c(pi), 1.0)

    def test_arc_length(self):
        self.assertEqual(arc_length(180, 1.0), pi)

if __name__ == "__main__":
    unittest.main()
