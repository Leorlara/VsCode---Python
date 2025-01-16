import numpy as np

def triangle_area (a,b,c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return area

def square_area (a):
    return a**2

def circle_area (r):
    return np.pi * r**2

Selection = input("What shape would you like to calculate? (Square / Circle / Triangle)").title().strip()

if Selection == triangle:
    input_a = float(input("Enter the length of side 1: "))
    input_b = float(input("Enter the length of side 2: "))
    input_c = float(input("Enter the length of side 3: "))
    print(f"The area of the triangle is: {triangle_area(input_a, input_b, input_c):.2f}")

elif Selection == square:
    input_a = float(input("Enter the length of side: "))
    print(f"The area of the square is: {square_area(input_a):.2f}")

elif Selection == circle:
    input_a = float(input("Enter the radius of the circle: "))
    print(f"The area of the circle is: {circle_area(input_a):.2f}")