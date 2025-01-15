# Create a Python program that computes the area of a triangle using Heron's Formula. Instead of using the sqrt() function from the math module, use exponentiation to calculate the square root.

import math

def heron_area(a, b, c):
    """Calculates the area of a triangle using Heron's formula."""
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        return "Invalid triangle sides."
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

try:
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))
    area = heron_area(a, b, c)
    print(f"The area of the triangle is: {area}")
except ValueError:
    print("Invalid input.")
