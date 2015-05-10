import turtle

t = turtle.Turtle()

for d in [20, 40, 60]:
    for c in ['red', 'green', 'yellow', 'blue']:
        t.color(c)
        t.forward(d)
        t.left(90)
        
for _ in range(1,36):
    t.forward(10)
    t.left(10)
            
turtle.done()        