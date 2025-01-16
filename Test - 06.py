def triangle_area (a,b,c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return area

def square_area (a):
    return a**2

def circle_area (r):
    return 3.14159 * r**2

input_a = float(input("Enter the length of side 1: "))
input_b = float(input("Enter the length of side 2: "))
input_c = float(input("Enter the length of side 3: "))

print(f"The area of the triangle is: {triangle_area(input_a, input_b, input_c):.2f}")