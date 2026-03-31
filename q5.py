import random
import turtle

data = [[random.randint(-300,300),random.randint(-300,300)],[random.randint(-300,300),random.randint(-300,300)],[random.randint(-300,300),random.randint(-300,300)]]

t = turtle.Pen()


t.penup()
t.goto(data[0][0], data[0][1])
t.pendown()

t.goto(data[1][0], data[1][1])
t.goto(data[2][0], data[2][1])
t.goto(data[0][0], data[0][1])


turtle. done()
