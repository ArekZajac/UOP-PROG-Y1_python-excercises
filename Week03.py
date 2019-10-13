# exercises week 03
import graphics as g
import random
import math

width = 700
height = 500
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
        message = g.Text(g.Point(100, 100), "Click on first g.Point")
        message.draw(win)
        p1 = win.getMouse()
        message.setText("Click on second g.Point")
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

    mouse4 = win.getMouse()
    print(mouse4, mouse1.getX())
    arms = g.Line(g.Point(mouse4.getX(), (mouse1.getY() + radius) + 10),
                  g.Point((mouse4.getX()) + ((mouse4.getX() + mouse3.getX()) / 4), (mouse1.getY() + radius) + 10))
    arms.draw(win)

    mouse5 = win.getMouse()
    leg_l = g.Line(g.Point(mouse1.getX(), mouse3.getY()), g.Point(mouse5.getX(), mouse5.getY()))
    leg_l.draw(win)
    leg_r = g.Line(g.Point(mouse1.getX(), mouse3.getY()), g.Point(mouse5.getY() - mouse1.getY() - mouse1.getY()
                                                                  , mouse5.getY()))
    leg_r.draw(win)
