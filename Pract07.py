# Practical Worksheet P07: Using Booleans and While Loops

import re
import time
from random import randint

import graphics as g
from Pract06 import calculate_grade
from Pract05 import draw_brown_eye_in_centre
from Pract02 import distance_between_points


def get_name():
    while True:
        name = input('name:')
        if re.match('[A-Za-z]', name):
            return name


def traffic_lights():
    win = g.GraphWin()
    red = g.Circle(g.Point(100, 50), 20)
    red.setFill("black")
    red.draw(win)
    amber = g.Circle(g.Point(100, 100), 20)
    amber.setFill("black")
    amber.draw(win)
    green = g.Circle(g.Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)
    while True:
        red.setFill('red')
        time.sleep(0.5)
        amber.setFill('yellow')
        time.sleep(0.5)
        red.setFill('black')
        amber.setFill('black')
        green.setFill('green')
        time.sleep(0.5)
        green.setFill('black')
        amber.setFill('yellow')
        time.sleep(0.5)
        amber.setFill('black')


def grade_coursework():
    while True:
        grade = input('grade:')
        if re.match('[0-9]', grade) and 0 < int(grade) < 20:
            print('The pupil achieved a grade of', calculate_grade(int(grade)))
        print('invalid grade')


def order_price():
    while True:
        unit_price = int(input('unit price:'))
        quantity = int(input('quantity:'))
        more = bool(input('more products?'))
        print('total:', unit_price * quantity)


def clickable_eye():
    window = g.GraphWin('clickable_eye', 500, 500)
    centre = g.Point(250, 250)
    draw_brown_eye_in_centre(window, centre, 100)
    label = g.Text(g.Point(50, 50), '')
    label.draw(window)
    while True:
        m = window.getMouse()
        if distance_between_points(centre, m) < 25:
            label.setText('pupil')
        elif distance_between_points(centre, m) < 50:
            label.setText('iris')
        elif distance_between_points(centre, m) < 100:
            label.setText('sclera')
        else:
            window.close()
            return


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_fahrenheit(celsius):
    return 9 / 5 * celsius + 32


def temperature_converter():
    while True:
        option = input('[c]elsius to fahrenheit   -   [f]ahrenheit to celsius')
        value = int(input('Value: '))
        if option.lower() == 'c':
            print(celsius_to_fahrenheit(value), 'f')
        elif option.lower() == 'f':
            print(fahrenheit_to_celsius(value), 'c')
        else:
            print('Invalid input')


def guess_the_number():
    number = randint(1, 100)
    for i in range(7):
        guess = int(input('Take a guess'))
        if guess < number:
            print('higher')
        elif guess > number:
            print('lower')
        else:
            print('correct')
            return


def table_tennis_scorer():
    window = g.GraphWin('table_tennis_scorer', 700, 400)
    separator = g.Line(g.Point(350, 0), g.Point(350, 400))
    separator.draw(window)
    label_left = g.Text(g.Point(175, 50), 0)
    label_left.draw(window)
    label_right = g.Text(g.Point(525, 50), 0)
    label_right.draw(window)
    score_left = 0
    score_right = 0
    while True:
        m = window.getMouse()
        if m.getX() < 350:
            score_left += 1
        else:
            score_right += 1
        label_left.setText(score_left)
        label_right.setText(score_right)
        if score_left >= 11 and score_left - score_right >= 2:
            label_wins = g.Text(g.Point(175, 100), 'wins')
            label_wins.draw(window)
            return
        elif score_right >= 11 and score_right - score_left >= 2:
            label_wins = g.Text(g.Point(525, 100), 'wins')
            label_wins.draw(window)
            return


def clickable_box_of_eyes():
    window = g.GraphWin('clickable_box_of_eyes', 700, 400)
    border = g.Rectangle(g.Point(50, 50), g.Point(650, 350))
    border.draw(window)
    label = g.Text(g.Point(60, 375), 'test')
    label.draw(window)
    for i in range(125, 600, 150):
        for j in range(125, 300, 150):
            draw_brown_eye_in_centre(window, g.Point(i, j), 75)
    while True:
        m = window.getMouse()
