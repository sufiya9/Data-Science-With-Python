import turtle
from turtle import *

s=turtle.getscreen()
t=turtle.Turtle()

# Using Loops and Conditional Statements

# for i in range(4):
#     t.fd(100)
#     t.rt(90)

# # While Loop
# n=10
# while n <=40:
#     t.circle(n)
#     n=n+10

#Conditional Statements
u = input("Would you like me to draw a shape? Type yes or no: ")
if u == "yes":
    t.circle(50)
elif u == "no":
    print("Okay")
else:
    print("Invalid Reply")

mainloop()