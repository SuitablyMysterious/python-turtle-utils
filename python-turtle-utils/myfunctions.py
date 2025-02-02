import turtle as tr
import math

def draw_square(t, side_length):
    # Draws a square
    for _ in range(4):
        t.forward(side_length)
        t.right(90)

def draw_triangle(t, a, b, c):
    # Calculate angles using the law of cosines
    angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angle_C = 180 - angle_A - angle_B

    # Draw the triangle
    t.forward(a)
    t.left(180 - angle_A)
    t.forward(b)
    t.left(180 - angle_B)
    t.forward(c)
    t.left(180 - angle_C)

def draw_shape(t, side_length, sides):
    for _ in range(sides):
        t.forward(side_length)
        t.right(360 / sides)

def euclidean_distance(x1, y1, x2, y2):
    # Euclidean distance between two points
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def easy_setup(t,w,width,height,bgcolor):
    # Setup the turtle
    t.speed(0)
    t.hideturtle()
    w.setup(width, height)
    w.bgcolor(bgcolor)

def wasdGameControls(t,w):
    w.onkey(lambda: t.setheading(90), 'w')
    w.onkey(lambda: t.setheading(180), 'a')
    w.onkey(lambda: t.setheading(270), 's')
    w.onkey(lambda: t.setheading(0), 'd')
    w.listen()