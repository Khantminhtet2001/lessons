from turtle import*
import random

color = ['yellow','pink','light blue']

for i in range(6):
    begin_fill()
    a=random.choice(color)
    fillcolor(a)
    for j in range(2):
        forward(150)
        left(30)
        forward(150)
        left(150)
    left(60)
    end_fill()