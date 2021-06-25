import turtle


pen = turtle.Turtle()

def goto(position):
    pen.penup()
    pen.goto(position[0], position[1])

def drawTrack(): 
    pen.pendown()
    pen.forward(200)

def write(label): 
    pen.pendown()
    pen.write(label)


start_cord = (-180, 210)
line_length = 200
race_width = 210
finish_cord = (race_width + start_cord[0], start_cord[1])
start_label_cord = (start_cord[0]-30, start_cord[1]+10)
finish_label_cord = (finish_cord[0]-30, finish_cord[1]+10)

turtle.colormode(255)
turtle.Screen().bgcolor(135,206,250)

pen.hideturtle()
goto(start_cord)
pen.right(90)
drawTrack()
goto(finish_cord)
drawTrack()
goto(start_label_cord)
write("START")
goto(finish_label_cord)
write("FINISH")