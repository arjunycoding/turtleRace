from welcome import *
from setUp import *
from racers import *
from whoWon import *
from random import *
from turtle import *
i = 0
turtle.hideturtle()
winningXcor = 11
penup()
goto(-80, -20)
color("white")
def move(racer): 
    racer.forward(randint(1, 5))
while(tom.xcor() != winningXcor and tommy.xcor() != winningXcor and bob.xcor() != winningXcor and bobby.xcor() != winningXcor and jim.xcor() != winningXcor and jimmy.xcor() != winningXcor):
    moveForward(tom)
    i = 0
    move(tom)
    move(tommy)
    move(bob)
    move(bobby)
    move(jim)
    move(jimmy)
whoWon()
turtle.done()