import turtle
from turtle import *

s=turtle.getscreen()
t=turtle.Turtle()

# t.pencolor("purple")
# t.fillcolor("black")
# t.pensize(10)
# t.speed(9)
t.pen(pencolor="purple",fillcolor="orange",pensize=10,speed=9)
t.begin_fill()
t.circle(90)
t.end_fill()

t.fd(100)
t.rt(90)
t.penup() # pen up there is no line showing 
t.fd(100)
t.rt(90)
t.pendown() # pen down and again pen make a line acc.
t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.pendown()

#  t.undo() Undoing Changes
# t.clear() Clearing the Screen
# t.reset() Resetting the Environment

mainloop()