import turtle

def clicked(racer):
    def hurdle(x,y):
        racer.forward(-100)
    racer.onclick(hurdle)

def makeRacer(cor, color):
    racer = turtle.Turtle()
    racer.penup()
    racer.goto(cor[0], cor[1])
    racer.color(color)
    racer.shape("turtle")
    
    clicked(racer)
    return racer

tom = makeRacer((-200,200), "red")
tommy = makeRacer((-200,170), "orange")
bob = makeRacer((-200,140), "yellow")
bobby = makeRacer((-200,110), "green")
jim = makeRacer((-200,80), "blue")
jimmy = makeRacer((-200,50), "purple")