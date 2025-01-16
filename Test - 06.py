def triangle_area (a,b,c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return area

input_a = float(input("Enter the length of side 1: "))
input_b = float(input("Enter the length of side 2: "))
input_c = float(input("Enter the length of side c3 "))