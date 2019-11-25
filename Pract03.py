# exercises week 03

import graphics as g
import random
import math

width = 1000
height = 700
win = g.GraphWin("Window", width, height)
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]


def misc():
    for a in range(height):
        circle = g.Circle(g.Point(width / 2, height / 2), a)
        circle.setOutline(random.choice(colors))
        circle.draw(win)


def draw_stick_figure():
    head = g.Circle(g.Point(100, 60), 20)
    head.draw(win)
    body = g.Line(g.Point(100, 80), g.Point(100, 120))
    body.draw(win)
    arms = g.Line(g.Point(70, 100), g.Point(130, 100))
    arms.draw(win)
    leg_l = g.Line(g.Point(100, 120), g.Point(120, 170))
    leg_l.draw(win)
    leg_r = g.Line(g.Point(100, 120), g.Point(80, 170))
    leg_r.draw(win)


def draw_circle():
    circle = g.Circle(g.Point(width / 2, height / 2), float(input("Radius: ")))
    circle.draw(win)


def draw_archery_target():
    circle1 = g.Circle(g.Point(width / 2, height / 2), 50)
    circle1.setFill("yellow")
    circle2 = g.Circle(g.Point(width / 2, height / 2), circle1.getRadius() * 2)
    circle2.setFill("red")
    circle3 = g.Circle(g.Point(width / 2, height / 2), circle1.getRadius() * 3)
    circle3.setFill("blue")
    circle3.draw(win)
    circle2.draw(win)
    circle1.draw(win)


def draw_rectangle():
    rec_width = float(input("Width: "))
    rec_length = float(input("Length: "))
    rectangle = g.Rectangle(g.Point((width / 2) - (rec_width / 2), (height / 2) - (rec_length / 2)), g.Point((width / 2)
                            + (rec_width / 2), (height / 2) + (rec_length / 2)))
    rectangle.draw(win)


def blue_circle():
    while 1 == 1:
        m = win.getMouse()
        circle = g.Circle(g.Point(m.getX(), m.getY()), 50)
        circle.setFill("blue")
        circle.draw(win)


def ten_lines():
    for i in range(10):
        message = g.Text(g.Point(100, 100), "Click on first point")
        message.draw(win)
        p1 = win.getMouse()
        message.setText("Click on second point")
        p2 = win.getMouse()
        line = g.Line(p1, p2)
        line.draw(win)
        message.setText("")


def ten_strings():
    input_box = g.Entry(g.Point(50, 50), 10)
    input_box.draw(win)
    for i in range(10):
        m = win.getMouse()
        text = g.Text(g.Point(m.getX(), m.getY()), input_box.getText())
        text.draw(win)


def ten_coloured_rectangles():
    input_box = g.Entry(g.Point(50, 50), 10)
    input_box.draw(win)
    for i in range(10):
        m = win.getMouse()
        point_a = g.Point(m.getX(), m.getY())
        m = win.getMouse()
        point_b = g.Point(m.getX(), m.getY())
        rectangle = g.Rectangle(point_a, point_b)
        rectangle.setFill(input_box.getText())
        rectangle.draw(win)


def five_click_stick_figure():
    mouse1 = win.getMouse()
    mouse2 = win.getMouse()
    radius = math.sqrt((mouse1.getX() - mouse2.getX()) ** 2 + (mouse1.getY() - mouse2.getY()) ** 2)
    head = g.Circle(g.Point(mouse1.getX(), mouse1.getY()), radius)
    head.draw(win)

    mouse3 = win.getMouse()
    body = g.Line(g.Point(mouse1.getX(), mouse1.getY() + radius), g.Point(mouse1.getX(), mouse3.getY()))
    body.draw(win)

    symmetry = mouse1.getX()

    mouse4 = win.getMouse()
    arm_distance = (symmetry - mouse4.getX()) * 2
    arms = g.Line(g.Point(mouse4.getX(), mouse4.getY()), g.Point(mouse4.getX() + arm_distance, mouse4.getY()))
    arms.draw(win)

    mouse5 = win.getMouse()
    leg_distance = (symmetry - mouse5.getX()) * 2
    leg_l = g.Line(g.Point(mouse1.getX(), mouse3.getY()), g.Point(mouse5.getX(), mouse5.getY()))
    leg_l.draw(win)
    leg_r = g.Line(g.Point(mouse1.getX(), mouse3.getY()), g.Point(mouse5.getX() + leg_distance, mouse5.getY()))
    leg_r.draw(win)


def plot_rainfall():
    # input boxes
    input1 = g.Entry(g.Point(100, 50), 5)
    input1.draw(win)
    input2 = g.Entry(g.Point(200, 50), 5)
    input2.draw(win)
    input3 = g.Entry(g.Point(300, 50), 5)
    input3.draw(win)
    input4 = g.Entry(g.Point(400, 50), 5)
    input4.draw(win)
    input5 = g.Entry(g.Point(500, 50), 5)
    input5.draw(win)
    input6 = g.Entry(g.Point(600, 50), 5)
    input6.draw(win)
    input7 = g.Entry(g.Point(700, 50), 5)
    input7.draw(win)

    # input labels
    input_label1 = g.Text(g.Point(100, 25), "Day 1")
    input_label1.draw(win)
    input_label2 = g.Text(g.Point(200, 25), "Day 2")
    input_label2.draw(win)
    input_label3 = g.Text(g.Point(300, 25), "Day 3")
    input_label3.draw(win)
    input_label4 = g.Text(g.Point(400, 25), "Day 4")
    input_label4.draw(win)
    input_label5 = g.Text(g.Point(500, 25), "Day 5")
    input_label5.draw(win)
    input_label6 = g.Text(g.Point(600, 25), "Day 6")
    input_label6.draw(win)
    input_label7 = g.Text(g.Point(700, 25), "Day 7")
    input_label7.draw(win)

    # apply button
    button_apply = g.Rectangle(g.Point(800, 35), g.Point(875, 65))
    button_apply.draw(win)
    text_apply = g.Text(g.Point(837, 50), "Apply")
    text_apply.draw(win)

    # axis lines
    line_y = g.Line(g.Point(50, 100), g.Point(50, 500))
    line_y.draw(win)
    line_x = g.Line(g.Point(50, 500), g.Point(850, 500))
    line_x.draw(win)

    # bars
    while 1 == 1:
        m = win.getMouse()
        if 800 <= m.getX() <= 875 and 35 <= m.getY() <= 65:

            bar1 = g.Rectangle(g.Point(50, 500), g.Point(150, 500 - int(input1.getText())))
            bar1.draw(win)
            bar2 = g.Rectangle(g.Point(150, 500), g.Point(250, 500 - int(input2.getText())))
            bar2.draw(win)
            bar3 = g.Rectangle(g.Point(250, 500), g.Point(350, 500 - int(input3.getText())))
            bar3.draw(win)
            bar4 = g.Rectangle(g.Point(350, 500), g.Point(450, 500 - int(input4.getText())))
            bar4.draw(win)
            bar5 = g.Rectangle(g.Point(450, 500), g.Point(550, 500 - int(input5.getText())))
            bar5.draw(win)
            bar6 = g.Rectangle(g.Point(550, 500), g.Point(650, 500 - int(input6.getText())))
            bar6.draw(win)
            bar7 = g.Rectangle(g.Point(650, 500), g.Point(750, 500 - int(input7.getText())))
            bar7.draw(win)
