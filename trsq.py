import turtle
turtle.Screen().bgcolor("Blue")
sc=turtle.Screen()
sc.setup(300,400)
turtle.title("My Turtle Program")
board=turtle.Turtle()
for i in range(4):
    board.pensize(3)
    board.pencolor("orange")
    board.forward(100)
    board.left(90)
    i=i+1
turtle.done()