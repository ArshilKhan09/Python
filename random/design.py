import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)

colors = ["orange","white","green"]

for i in range(250):
    t.pencolor(colors[i % 3])
    t.forward(i * 2)
    t.right(200)
turtle.done()