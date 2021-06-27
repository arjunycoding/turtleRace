from random import *
from setUp import *
from racers import *
from turtle import *
def whoWon():
    tomx = tom.xcor() 
    tommyx = tommy.xcor()
    bobx = bob.xcor()
    bobbyx = bobby.xcor()
    jimx = jim.xcor()
    jimmyx = jimmy.xcor()
    highest = max(tomx, tommyx, bobx, bobbyx, jimmyx)
    if highest == tomx:
        write("Tom (the red turtle) wins the Turtle Race",font=("Arial", 25, "normal"), align=("center"))
    elif highest == tommyx:
        write("Tommy (the orange turtle) wins the Turtle Race",  font=("Arial", 25, "normal"),  align=("center"))
    elif highest == bobx:
        write("Bob (the yellow turtle) wins the Turtle Race",  font=("Arial", 25, "normal"),  align=("center"))
    elif highest == bobbyx:
        write("Bobby (the green turtle) wins the Turtle Race",  font=("Arial", 25, "normal"),  align=("center"))
    elif highest == jimx:
        write("Jim (the blue turtle) wins the Turtle Race",  font=("Arial", 25, "normal"),  align=("center"))
    elif highest == jimmyx:
        write("Jimmy (the purple turtle) wins the Turtle Race",  font=("Arial", 25, "normal"),  align=("center"))