import turtle






x1,y1 = eval(input("좌표1을 입력해주세요: "))
x2,y2 = eval(input("좌표2를 입력해주세요: "))

t = turtle.Pen()

t.penup()
t.goto(x1,y1)
t.write(f"{x1},{y1}")

t.pendown()
t.goto(x2,y2)
t.write(f"{x2},{y2}")



  
turtle.done()