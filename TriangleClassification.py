"""Gabriela Onelli
Dr. Saremi
SSW 567
Hw 1 Triangle Classifcation

I pledge my honor that I have abided by the Stevens Honor System. -Gabriela Onelli"""

"Returns for the inputs"
right = "This is a right triangle";
isosceles = "This is an isosceles triangle";
equilateral = "This is an equilateral triangle";
scalene = "This is a scalene triangle";

"Function to classify a triangle based on side lengths"
def classify_triangle(a,b,c):
    sideA = a**2;
    sideB = b**2;
    sideC = c**2;
    if a==b and a==c:
        return equilateral;
    elif (sideA+sideB)==sideC:
        return right;
    elif a!=b and a!=c and c!=b:
        return scalene;
    else:
        return isosceles;
