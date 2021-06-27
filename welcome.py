from turtle import *
from time import *
colormode(255)
bgcolor(135,206,250)
hideturtle()
penup()
hideturtle()
goto(0, 200)
pendown()
write("WELCOME TO THE TURTLE RACE GAME!", font=("Arial", 25, "normal"), align=("center"))
penup()
goto(0, -200)
write("""
    There will be 6 turtles racing your job is to make the red turtle (Tom) win.
    Keep clicking Tom to make him move forward!
    Here are the 6 turtles
    - Tom(red turtle play as him)
    - Tommy(orange turtle)
    - Bob(yellow turtle)
    - Bobby(green turtle)
    - Jim(blue turtle)
    - Jimmy(purple turtle)
    """, font=("Arial", 15, "normal"), align=("center"))
sleep(10)
clear()