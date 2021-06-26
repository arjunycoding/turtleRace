from random import *
from setUp import *
from racers import *
import turtle
winningXcor = 10
pen.goto(-80, -10)
pen.color("white")
i = 0
compareRacers = ""
# tom.xcor() == winningXcor or tommy.xcor() == winningXcor or
# bob.xcor() == winningXcor or bobny.xcor() == winningXcor or
# jim.xcor() == winningXcor or jimmy.xcor() == winningXcor or

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