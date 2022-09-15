from logging.handlers import RotatingFileHandler
from tkinter import RIGHT
from tracemalloc import stop
from turtle import *
speed(10)
color("red")
width(1)

begin_fill()
#wall
forward(200) 
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
end_fill()
left(180)

forward(200)

#roof
begin_fill()
color("blue")
right(30)
forward(200)
right(120)
forward(200)
end_fill()
#window
left(-120)
forward(180)
color("white")
begin_fill()
left(90)
penup()
forward(20)
pendown()
forward(60)
left(90)
forward(40)
left(90)
forward(60)
left(90)
forward(40)
end_fill()
#door
color("red")
forward(20)
left(90)
forward(180)
left(90)
forward(75)
color("brown")
begin_fill()
left(90)
forward(75)
left(-90)
forward(50)
right(90)
forward(75)
right(90)
forward(50)
end_fill()
#grass
color("green")
begin_fill()
forward(1000)
left(90)
forward(1000)
left(90)
forward(2000)
left(90)
forward(1000)
end_fill()



exitonclick()


