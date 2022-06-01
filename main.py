import turtle 

w = turtle.Screen()
w.title('Spiral Helix')
w.bgcolor('black')

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow', 'indigo']

t = turtle.Pen()
t.speed(150)

for x in range(270):
    color = colors[x % len(colors)]
    t.pencolor(color)
    t.width(x / 100 + 2)
    t.forward(x )
    t.left(53)

turtle.done()