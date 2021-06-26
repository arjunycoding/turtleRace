from random import *
from setUp import *
from racers import *
import turtle
winningXcor = 10
def move(racer): 
    racer.forward(randint(1, 5))
i = 0
pen = turtle.Turtle()
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
            break
        elif tommy.xcor() == winningXcor:
            pen.write("THE ORANGE TURTLE FINISHED!")
            break
        elif bob.xcor() == winningXcor:
            pen.write("THE YELLOW TURTLE FINISHED!")
            break
        elif bobby.xcor() == winningXcor:
            pen.write("THE GREEN TURTLE FINISHED!")
            break
        elif jim.xcor() == winningXcor:
            pen.write("THE BLUE TURTLE FINISHED!")
            break
        elif jimmy.xcor() == winningXcor:
            pen.write("THE PURPLE TURTLE FINISHED!")
            break
        i+=1
turtle.done()