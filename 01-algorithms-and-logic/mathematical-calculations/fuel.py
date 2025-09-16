import math

def ex1():
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter another number: "))
    print("Result:", (n1 + n2) / 2)

def ex2():
    gas = float(input("Enter the price of petrol: "))
    alc = float(input("Enter the price of alcohol: "))
    print("Price ratio:", gas / alc, ": 1")

def ex3():
    base = int(input("Enter the base of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))
    print("Area:", base * height, "cm²")
    print("Perimeter:", 2 * (base + height), "cm")

def ex4():
    radius = float(input("Enter the radius of the sphere: "))
    print("Volume of the sphere:", (4 * math.pi * math.pow(radius, 3)) / 3, "cm³")

def ex5():
    radius = float(input("Enter the radius of the circle: "))
    print("Area:", math.pi * math.pow(radius, 2), "cm²")
    print("Circumference:", 2 * math.pi * radius)

def ex6():
    angle = int(input("Enter the angle in degrees: "))
    print("Angle in radians:", (math.pi * angle) / 180)

def ex7():
    temp = int(input("Enter the temperature in degrees Celsius: "))
    print((9/5 * temp) + 32, "° Fahrenheit")

