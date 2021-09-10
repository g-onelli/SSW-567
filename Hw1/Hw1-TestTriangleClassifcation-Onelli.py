"""Gabriela Onelli
Dr. Saremi
SSW 567
Hw 1 Triangle Classifcation Test File

I pledge my honor that I have abided by the Stevens Honor System. -Gabriela Onelli"""

import unittest;
import TriangleClassification;

class TestTriangleClassification(unittest.TestCase):
    def test_right(self):
        right = "This is a right triangle";
        result = TriangleClassification.classify_triangle(3,4,5);
        self.assertEqual(result, right);
    def test_equilateral(self):
        equilateral = "This is an equilateral triangle";
        result = TriangleClassification.classify_triangle(3,3,3);
        self.assertEqual(result, equilateral);        
    def test_isosceles(self):
        isosceles = "This is an isosceles triangle";
        result = TriangleClassification.classify_triangle(4,4,5);
        self.assertEqual(result, isosceles);
    def test_scalene(self):
        scalene = "This is a scalene triangle";
        result = TriangleClassification.classify_triangle(3,4,8);
        self.assertEqual(result, scalene);        
    def test_triangle(self):
        triangle = "This is not a triangle";
        result = TriangleClassification.classify_triangle(0,4,5);
        self.assertEqual(result, triangle);

        
if __name__ == '__main__':
    unittest.main();
