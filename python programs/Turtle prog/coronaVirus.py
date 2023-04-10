from turtle import *
up()
goto(0,140)
down()
color('green')
bgcolor('black')
hideturtle()
speed(0)
i=0
for i in range(200):
    right(i)
    forward(i*3)
    i=i+1

Screen().exitonclick()