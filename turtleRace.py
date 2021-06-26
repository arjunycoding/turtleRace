from random import *
from setUp import *
from racers import *
from turtle import *
print(True or False or False or False or False or False or False or False)
i = 0
turtle.hideturtle()
winningXcor = 11
penup()
goto(-80, -20)
color("white")
def move(racer): 
    racer.forward(randint(1, 5))
while(tom.xcor() != winningXcor and tommy.xcor() != winningXcor and bob.xcor() != winningXcor and bobby.xcor() != winningXcor and jim.xcor() != winningXcor and jimmy.xcor() != winningXcor):
    i = 0
    move(tom)
    move(tommy)
    move(bob)
    move(bobby)
    move(jim)
    move(jimmy)
    print(tom.xcor())
tomx = tom.xcor() 
tommyx = tommy.xcor()
bobx = bob.xcor()
bobbyx = bobby.xcor()
jimx = jim.xcor()
jimmyx = jimmy.xcor()
highest = max(tomx, tommyx, bobx, bobbyx, jimmyx)
if highest == tomx:
    write("Tom wins the Turtle Race",font=("Arial", 25, "normal"), align=("center"))
elif highest == tommyx:
    write("Tommy wins the Turtle Race",  font=("Arial", 25, "normal"),  align=("center"))
elif highest == bobx:
    write("Bob wins the Turtle Race",  font=("Arial", 25, "normal"),  align=("center"))
elif highest == bobbyx:
    write("Bobby wins the Turtle Race",  font=("Arial", 25, "normal"),  align=("center"))
elif highest == jimx:
    write("Jim wins the Turtle Race",  font=("Arial", 25, "normal"),  align=("center"))
elif highest == jimmyx:
    write("Jimmy wins the Turtle Race",  font=("Arial", 25, "normal"),  align=("center"))
turtle.done()