
import turtle
turtle.bgcolor("light Blue")

turtle.pensize(1.5)

turtle.speed(10)
color = ["red", "blue", "purple", "green"]

for a in range(9):
    for i in color:
        turtle.color(i)
        turtle.circle(50)
        turtle.left(80)
        turtle.forward(100)
        turtle.pencolor("blue")
        turtle.backward(20)
turtle.mainloop()
