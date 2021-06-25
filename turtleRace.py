from random import *
from setUp import *
from racers import *
import turtle
def move(racer): 
    racer.forward(randint(1, 5))

i = 0
winningXcor = 10
pen.goto(-80, -10)
pen.color("white")
for i in range(75):
    i = 0
    move(tom)
    move(tommy)
    move(bob)
    move(bobby)
    move(jim)
    move(jimmy)
    while(i < 1):
        pen.pendown()
        if tom.xcor() == winningXcor:
            pen.write("THE RED TURTLE FINISHED!")
            pen.ycor(-10)
            break
        elif tommy.xcor() == winningXcor:
            pen.write("THE ORANGE TURTLE FINISHED!")
            pen.ycor(-10)
            break
        elif bob.xcor() == winningXcor:
            pen.write("THE YELLOW TURTLE FINISHED!")
            pen.ycor(-10)
            break
        elif bobby.xcor() == winningXcor:
            pen.write("THE GREEN TURTLE FINISHED!")
            pen.ycor(-10)
            break
        elif jim.xcor() == winningXcor:
            pen.write("THE BLUE TURTLE FINISHED!")
            pen.ycor(-10)
            break
        elif jimmy.xcor() == winningXcor:
            pen.write("THE PURPLE TURTLE FINISHED!")
            pen.ycor(-10)
            break
        i+=1
turtle.done()