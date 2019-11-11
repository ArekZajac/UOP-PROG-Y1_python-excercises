# Practical Worksheet P05: Defining and Using Functions

import graphics as g
from Pract02 import area_of_circle, circumference_of_circle, distance_between_points
from random import randint


def circle_info(radius):
    return 'The area is ' + str(area_of_circle(radius)) + 'and the circumference is ' + \
           str(circumference_of_circle(radius))


def draw_circle(win, centre, radius, colour):
    circle = g.Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


def draw_brown_eye_in_centre(window, centre, radius):
    if window == 'null':
        window = g.GraphWin("draw_brown_eye_in_centre", 1000, 700)
    if centre == 'null':
        centre = g.Point(500, 350)
    draw_circle(window, centre, radius, 'white')
    draw_circle(window, centre, radius / 2, 'brown')
    draw_circle(window, centre, radius / 4, 'black')


def draw_block_of_stars(width, height):
    for i in range(height):
        for j in range(width):
            print('*', end='')
        print()


def draw_letter_e():
    draw_block_of_stars(8, 2)
    draw_block_of_stars(2, 2)
    draw_block_of_stars(5, 2)
    draw_block_of_stars(2, 2)
    draw_block_of_stars(8, 2)


def draw_pair_of_brown_eyes():
    window = g.GraphWin("draw_pair_of_brown_eyes", 1000, 700)
    radius = 60
    centre = g.Point(500, 350)
    draw_brown_eye_in_centre(window, g.Point(centre.getX() - radius, centre.getY()), radius)
    draw_brown_eye_in_centre(window, g.Point(centre.getX() + radius, centre.getY()), radius)


def draw_blocks(b1, c1, b2, c2, height):
    for i in range(height):
        for j in range(b1):
            print(' ', end='')
        for j in range(c1):
            print('*', end='')
        for j in range(b2):
            print(' ', end='')
        for j in range(c2):
            print('*', end='')
        print('')


def draw_letter_a():
    draw_blocks(1, 8, 1, 0, 2)
    draw_blocks(0, 2, 6, 2, 2)
    draw_blocks(0, 10, 0, 0, 2)
    draw_blocks(0, 2, 6, 2, 3)


def draw_four_pairs_of_brown_eyes():
    window = g.GraphWin('draw_four_pairs_of_brown_eyes', 1000, 700)
    for i in range(2):
        centre_1 = window.getMouse()
        radius_1 = distance_between_points(centre_1, window.getMouse())
        draw_brown_eye_in_centre(window, g.Point(centre_1.getX() + radius_1, centre_1.getY()), radius_1)
        draw_brown_eye_in_centre(window, g.Point(centre_1.getX() - radius_1, centre_1.getY()), radius_1)


def display_text_with_spaces(window, text, size, position):
    label = g.Text(position, ' '.join(text))
    label.setSize(size)
    label.draw(window)


def construct_vision_chart():
    window = g.GraphWin('construct_vision_chart', 1000, 700)
    sizes = [30, 25, 20, 15, 10, 5]
    positions = [100, 200, 300, 400, 500, 600]
    for i in range(6):
        display_text_with_spaces(window, str(input()).upper(), sizes[i], g.Point(500, positions[i]))


def independent_stick_figure(window, origin_x, origin_y):
    head = g.Circle(g.Point(origin_x, origin_y), 20)
    head.draw(window)
    body = g.Line(g.Point(origin_x, origin_y + 20), g.Point(origin_x, origin_y + 60))
    body.draw(window)
    arms = g.Line(g.Point(origin_x - 30, origin_y + 40), g.Point(origin_x + 30, origin_y + 40))
    arms.draw(window)
    leg_l = g.Line(g.Point(origin_x, origin_y + 60), g.Point(origin_x + 20, origin_y + 110))
    leg_l.draw(window)
    leg_r = g.Line(g.Point(origin_x, origin_y + 60), g.Point(origin_x - 20, origin_y + 110))
    leg_r.draw(window)


def draw_stick_figure_family():
    window = g.GraphWin('draw_stick_figure_family', 1000, 700)
    # while 1 == 1:
    #     m = window.getMouse()
    #     independent_stick_figure(window, m.getX(), m.getY())
    while 1 == 1:
        independent_stick_figure(window, randint(0, 1000), randint(0, 700))