import turtle


screen = turtle.Screen()
screen.bgcolor("light blue") 
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(5)
pen.color("black", "red")
pen.begin_fill()
for _ in range(3):
    pen.forward(100)
    pen.left(120)
pen.end_fill()
pen.penup()
pen.goto(-150, -150)
pen.pendown()
pen.color("black", "green")
pen.begin_fill()
for i in range(2):
    pen.forward(150)
    pen.left(90)
    pen.forward(80)
    pen.left(90)
pen.end_fill()
pen.penup()
pen.goto(150, -150)
pen.pendown()
pen.color("black", "yellow")
pen.begin_fill()
for i in range(6):
    pen.forward(70)
    pen.left(60)
pen.end_fill()

turtle.done()
