import turtle
from turtle import *

s=turtle.getscreen()
t=turtle.Turtle()

#Leaving a Stamp
t.stamp()
8
t.fd(100)
t.stamp()
9
t.fd(100)
# clear the stmp
t.clearstamp(9)

#Cloning Your Turtle

c=t.clone()
t.color("magenta")
c.color("red")
t.circle(150)
c.circle(100)

mainloop()

