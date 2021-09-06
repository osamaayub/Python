import turtle

tle = turtle
screen = turtle.Screen()
screen.setup(400, 300)
screen.bgcolor("black")
tle.pencolor("Orange")

tle.pensize(5)
tle.speed(1)

tle.shape("turtle")
tle.forward(100)
tle.right(90)
tle.forward(100)
tle.right(90)
tle.forward(100)
tle.right(90)
tle.forward(100)
tle.right(90)
tle.penup()
tle.forward(100)
tle.setpos(-120, 100)
tle.pendown()
tle.pencolor("blue")
tle.write("This is Square ","Italics", 26,"bold")
tle.penup()
tle.ht()
