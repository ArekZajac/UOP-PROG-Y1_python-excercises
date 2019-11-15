# Practical Worksheet P06: If Statements and For Loops

import math
import time
import graphics as g
from Pract05 import draw_circle


def fast_food_order_price():
    order = float(input("Enter price of order:"))
    if order < 10:
        order = order + 1.5
    print('The total price of your order is £', order)


def what_to_do_today():
    temp = float(input("Enter today's temperature: "))
    if temp > 25:
        print('swim')
    elif temp >= 10:
        print('shopping')
    else:
        print('watch film')


def display_square_roots(start, end):
    range_list = list(range(start, end + 1))
    for i in range(end - start + 1):
        print('The square root of', range_list[i], 'is', round(math.sqrt(range_list[i]), 3))


def calculate_grade(grade):
    if grade >= 16:
        return 'A'
    elif grade >= 12:
        return 'B'
    elif grade >= 8:
        return 'C'
    else:
        return 'F'


def peas_in_a_pod():
    peas = int(input("Enter number of peas:"))
    window = g.GraphWin('Peas In A Pod', peas * 100, 100)
    for i in range(peas):
        circle = g.Circle(g.Point(50 + (50 * i * 2), 50), 50)
        circle.setFill('green')
        circle.draw(window)


def ticket_price(distance, age):
    price = 3
    for i in range(distance):
        price += 0.15
    if age >= 60 or age <= 15:
        return round(price - (price / 100 * 40), 2)
    return round(price, 2)


def numbered_square(n):
    displace = 0
    for i in range(n):
        for j in range(n):
            print((n + j) - displace, end=' ')
        displace += 1
        print('')


def draw_coloured_eye(window, centre, radius, colour):
    draw_circle(window, centre, radius, 'white')
    draw_circle(window, centre, radius / 2, colour)
    draw_circle(window, centre, radius / 4, 'black')


def eye_picker():
    centre = g.Point(int(input('X: ')), int(input('Y: ')))
    try:
        draw_coloured_eye(g.GraphWin('eye_picker', 1000, 700), centre, float(input('Radius: ')), input('Colour: '))
    except:
        print('invalid input')


def draw_patch_window(patch):
    window = g.GraphWin('draw_patch_window', 600, 600)
    if patch == 0:
        patch_zero(window)
    elif patch == 1:
        patch_one(window)
    elif patch == 2:
        patch_two(window)
    elif patch == 3:
        patch_three(window)
    elif patch == 6:
        patch_six(window)
    elif patch == 9:
        patch_nine(window)


def block_fill(anchor, window, i, j):
    corner = g.Point(anchor.getX() + (j * 50), anchor.getY() + (i * 50))
    square = g.Rectangle(g.Point(corner.getX(), corner.getY()), g.Point(corner.getX() + 50, corner.getY() + 50))
    square.setFill('black')
    square.setOutline('white')
    square.draw(window)


def patch_zero(window):
    anchor = g.Point(50, 50)
    for i in range(10):
        for j in range(10):
            if i > 8 - j:
                block_fill(anchor, window, i, j)


def patch_one(window):
    anchor = g.Point(25, 25)
    for i in range(10):
        corner = g.Point(anchor.getX() + (i * 25), anchor.getY() + (i * 25))
        square = g.Rectangle(corner, g.Point(600 - corner.getX(), 600 - corner.getY()))
        square.setFill('white')
        if (i % 2) == 0:
            square.setFill('black')
        square.draw(window)


def patch_two(window):
    anchor = g.Point(300, 550)
    for i in range(11):
        circle = g.Circle(g.Point(anchor.getX(), anchor.getY() - (i * 25)), i * 25)
        circle.draw(window)


def patch_three(window):
    print()


def patch_four(window):
    print()


def patch_five(window):
    print()


def patch_six(window):
    for i in range(11):
        p1 = g.Point(50 + (i * 50), 50)
        p2 = g.Point(600 - p1.getX(), 600 - p1.getY())
        line = g.Line(p1, p2)
        line.draw(window)
    for i in range(11):
        p1 = g.Point(50, 50 + (i * 50))
        p2 = g.Point(600 - p1.getX(), 600 - p1.getY())
        line = g.Line(p1, p2)
        line.draw(window)


def patch_seven(window):
    print()


def patch_eight(window):
    anchor = g.Point(100, 100)
    for i in range(5):
        for j in range(5):
            circle = g.Circle()


def patch_nine(window):
    anchor = g.Point(50, 50)
    for i in range(10):
        for j in range(10):
            if i == 9 - j:
                block_fill(anchor, window, i, j)
