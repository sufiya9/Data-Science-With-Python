from turtle import *

start=100
while start>0:
    forward(start)
    left(360/6)
    start-=5
    for i in range (4):
        pencolor("blue")
        forward(25)
        left(360/6)
    

mainloop()