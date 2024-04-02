# Python program to draw  
# Rainbow Benzene 
# using Turtle Programming 
import turtle 
from turtle import *
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
t = turtle.Turtle() 
t.speed(10)
turtle.bgcolor('black') 
for x in range(360): 
    t.pencolor(colors[x%6]) 
    t.width(x//100 + 1) 
    t.forward(x) 
    t.left(59) 

mainloop()