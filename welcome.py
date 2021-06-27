from turtle import *
colormode(255)
bgcolor(135,206,250)
hideturtle()
penup()
hideturtle()
goto(0, 200)
pendown()
write("WELCOME TO THE TURTLE RACE GAME!", font=("Arial", 25, "normal"), align=("center"))
penup()
goto(0, -100)
write("""
    There will be 6 turtles racing your job is to stop them.
    Here are the 6 turtles
    - Tom(red turtle)
    - Tommy(orange turtle)
    - Bob(yellow turtle)
    - Bobby(green turtle)
    - Jim(blue turtle)
    - Jimmy(purple turtle)
    """, font=("Arial", 15, "normal"), align=("center"))
from turtle import Screen, Turtle

CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'bold')

def draw_onclick(x, y):
    turtle.dot(100, 'cyan')

button = Turtle()
button.hideturtle()
button.shape("rectangle")
button.fillcolor('red')
button.penup()
button.goto(150, 150)
button.write("Click me!", align='center', font=FONT)
button.sety(150 + CURSOR_SIZE + FONT_SIZE)
button.onclick(draw_onclick)
button.showturtle()

turtle = Turtle()
turtle.hideturtle()

screen = Screen()
screen.mainloop()
done()