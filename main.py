# from turtle import Turtle, Screen, mainloop
#
# tim = Turtle()
# screen = Screen()
#
# def move_forwards():
#     tim.forward(10)
#
# screen.listen()
# screen.onkeypress(fun = move_forwards, key = "space")
# mainloop()


from turtle import Turtle, Screen
from turtle import *


my_turtle = Turtle()
screen = Screen()

def turtle_forward():
    my_turtle.forward(30)
def turtle_backward():
    my_turtle.backward(30)
def turtle_CC():
    my_turtle.left(30)
def turtle_CCC():
    my_turtle.right(30)

def turtle_clear():
    my_turtle.clear()




screen.listen()
screen.onkey(fun=turtle_forward, key='w')
screen.onkey(fun=turtle_backward, key='s')
screen.onkey(fun=turtle_CCC, key='a')
screen.onkey(fun=turtle_CC, key='d')
screen.onkey(fun=turtle_clear, key='c')


screen.exitonclick()