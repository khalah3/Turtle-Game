from turtle import Turtle, Screen
from turtle import *
import random

all_turtles=[]

screen = Screen()
screen.setup(width=500,height=400)
user_input=screen.textinput(title='what is your bet', prompt='please enter the turtle favorite color')
colors = ['green','red','purple','yellow','orange','blue']
y=-200

# def color_choice(colors):
#
#     for item in range(len(colors)):
#         random.shuffle(colors)
#     return ahmad_turtles.color(pick)

race_is_on=True

random.shuffle(colors)

for i in range(6):
    ahmad_turtle=Turtle(shape='turtle')
    all_turtles.append(ahmad_turtle)
    for color in colors:
        ahmad_turtle.color(colors[i])
        x=-240
        ahmad_turtle.penup()
        ahmad_turtle.goto(x, y)
        y=y+10

while race_is_on==True:



   for turtle in all_turtles:
        turtle.forward(random.randint(1,10))
        if turtle.xcor()>=220:
            race_is_on=False
            winning_color=turtle.pencolor()
            print(f'{winning_color} turtle won')
            if user_input == winning_color:
                print('You won too')
            else:
                print("You lost")
            break


































screen.exitonclick()