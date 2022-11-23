import turtle
import random
a = 5
bg = turtle.Screen()
bg.bgcolor("dark blue")
ornament_list = ["light blue", "maroon", "purple",
                 "silver", "white", "yellow", "magenta"]
xys = [(5, 120), (50, 70), (-50, 70), (-80, 10), (80, 10),
       (30, 40), (30, -40), (-30, -40), (-60, -40)]


def draw_star(turtle, size, x, y):
    color = "white"
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(72)
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
        turtle.forward(size)
    turtle.end_fill()


def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()


t = turtle.Turtle()
t.shape("turtle")
t.speed(100)

t.penup()
t.goto(0, 0)
t.color("green")
t.begin_fill()
t.fillcolor("green")
t.pensize(8)
t.pendown()
t.goto(100, 0)
t.penup()
t.end_fill()

t.goto(100, 0)
t.pendown()
t.color("green")
t.begin_fill()
t.fillcolor("green")
t.goto(0, 75)
t.goto(-100, 0)
t.forward(100)
t.goto(125, -65)
t.goto(-125, -65)
t.goto(0, 0)
t.penup()
t.end_fill()

t.goto(0, 75)
t.pendown()
t.color("green")
t.begin_fill()
t.fillcolor("green")
t.goto(50, 75)
t.goto(0, 120)
t.goto(-50, 75)
t.goto(0, 75)
t.penup()
t.end_fill()

t.goto(0, -90)
t.pendown()
t.color("brown")
t.begin_fill()
t.fillcolor("brown")
t.goto(20, -90)
t.left(90)
t.forward(20)
t.left(90)
t.forward(40)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.penup()
t.end_fill()

for i in range(len(xys)-1):
    t.penup()
    size = 5
    colors = (random.choice(ornament_list))
    t.goto(xys[i][0], xys[i][0])
    t.pendown()
    if i == 0:
        draw_star(t, size*2, xys[i][0], xys[i][1])
    else:
        draw_circle(t, colors, size, xys[i][0], xys[i][1])
        t.penup()

        t.goto(200, -200)
t.color("yellow")
t.write("@bilge", font=('Arial', 15, 'normal'))
t.hideturtle()
breakpoint()
