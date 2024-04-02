from turtle import *
import turtle

s=turtle.getscreen # for Screen
t=turtle.Turtle() #for program refer to the Turtle
t.shape("circle") #to change the shape of turtle
# t.shapesize(1,5,10) #to increase or decrease the size of the turtle this can't affecting the output of the pen 
t.shapesize(3,3,3) # Change the shape size of turtle
# t.fillcolor("red") # change the color fill of turtle

t.pensize(5) #increase the size of penline
# t.pencolor("green")  #change the color of the penline
t.color("black","red")  # first color indicate pen and second color indicate the turtle


turtle.title("My turtle Program") # For thr title line
turtle.bgcolor("White")  #For the background color We can use blue black red green
t.begin_fill() #start the color filling
t.fd(100) # For going forward
t.rt(90)  # For going rignt or turn right
t.fd(100)
t.rt(90)
t.speed(10) #to increase the speed of pe
t.fd(100)
t.rt(90)
t.fd(100)
t.end_fill() # end of the color filling
t.circle(20)  # for Drawing a circle
t.dot(20)  # for Drawing a dot

mainloop()

