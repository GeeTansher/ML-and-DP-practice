from turtle import *
bgcolor('grey')
up()
goto(-90, -150)
down()
width(3)
speed(0)

begin_fill()
for _ in range(2):
    fd(150)
    circle(100, 90)
    fd(100)
    circle(100, 90)
end_fill()

up()
goto(-50, -100)
down()

speed(3)

begin_fill()
color('#E50914')
for _ in range(2):
    left(90)
    forward(200)
    left(90)
    forward(30)
end_fill()

up()
goto(50, -100)
down()

begin_fill()
for _ in range(2):
    left(90)
    forward(200)
    left(90)
    forward(30)
end_fill()

begin_fill()
color('red')
i = 0
for i in range(4):
    if i == 0:
        left(116)
        forward(224)
    elif i == 1:
        pos = position()
        goto(pos[0]-32, pos[1])
    if i == 2:
        left(180)
        forward(224)
end_fill()
hideturtle()

Screen().exitonclick()
