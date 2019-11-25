# exercises week 02


import math


def circumference_of_circle(radius):
    return 2 * math.pi * radius


def area_of_circle(radius):
    print(math.pi * radius ** 2)


def cost_of_pizza():
    print("Cost: ", 1.5 * (math.pi * ((float(input("Diameter: "))) / 2) ** 2), "p")


def slop_of_line():
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    print("Slope: ", (y2 - y1) / (x2 - x1))


def distance_between_points(p1, p2):
    return math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)


def travel_statistics():
    avg_speed = float(input("Average Speed: "))
    dur = float(input("Duration: "))
    print("Distance", avg_speed * dur)
    print("Fuel use: ", (avg_speed * dur) / 5)


def sum_of_numbers():
    n = int(input("n: "))
    a = 0
    for v in range(n):
        a = a + (v + 1)
    print(a)


def average_of_number():
    amount = int(input("Amount: "))
    numbers = []
    total = 0
    for a in range(amount):
        numbers.append(float(input("Enter number: ")))
    for f in numbers:
        total = total + f
    print("Average: ", total / len(numbers))


def select_coins():
    amount = int(input("Amount: "))
    print("£2: ", amount // 200)
    amount = amount % 200
    print("£1: ", amount // 100)
    amount = amount % 100
    print("50p: ", amount // 50)
    amount = amount % 50
    print("20p: ", amount // 20)
    amount = amount % 20
    print("10p: ", amount // 10)
    amount = amount % 10
    print("5p: ", amount // 5)
    amount = amount % 5
    print("2p: ", amount // 2)
    amount = amount % 2
    print("1p: ", amount)
