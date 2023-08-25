from turtle import  Turtle,Screen
nikunj=Turtle()
screen=Screen()
nikunj.shape("arrow")
screen.listen()
screen.title("Sketch Book")
screen.bgcolor("black")
nikunj.color("white")
def up():
    nikunj.setheading(90)
    nikunj.forward(20)

def right():
    nikunj.setheading(0)
    nikunj.forward(20)
def left():
    nikunj.setheading(180)
    nikunj.forward(20)
def bottom():
    nikunj.setheading(270)
    nikunj.forward(20)
def clock_circle():
    nikunj.circle(30)

def anti():
    nikunj.circle(-30)
screen.onkey(up,"w")
screen.onkey(right,"d")
screen.onkey(bottom,"s")
screen.onkey(left,"a")
screen.onkey(clock_circle,"e")
screen.onkey(anti,"q")










screen.exitonclick()