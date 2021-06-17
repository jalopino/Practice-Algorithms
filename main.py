import time
from turtle import *
import turtle
from turtle import turtles
from random import randint
import keyboard

height = 0
width = 0
window = turtle.Screen()
turtle.screensize(500, 500, "black")
turtle.title("Stupid Snek")

up = 0
down = 0
left = 0
right = 0
global points
points = 0

paused = False

square1 = Turtle()
circle = Turtle()
point = Turtle()
pause = Turtle()

newBody = []

def object():
    square1.penup()
    square1.speed(0)
    square1.color("red")
    square1.shape("square")
    square1.setposition(width, height)

    circle.penup()
    circle.speed(0)
    circle.color("yellow")
    circle.shape("circle")
    circle.setposition(randint(-100, 100) * 3, randint(-100, 100) * 3)

    point.penup()
    point.hideturtle()
    point.speed(0)
    point.setposition(250, 350)
    point.color("white")

    pause.penup()
    pause.hideturtle()
    pause.speed(0)
    pause.setposition(0, 0)
    pause.color("white")

    global body
    body = Turtle()
    body.speed(0)
    body.color("green")

def collision():
    if (circle.distance(square1.xcor(), square1.ycor()) < 10):
        circle.setposition(randint(-100, 100) * 3, randint(-100, 100) * 3)


def limits():
    if (square1.ycor() > 420):
        square1.sety(-420)
    if (square1.ycor() < -420):
        square1.sety(420)
    if (square1.xcor() > 500):
        square1.setx(-500)
    if (square1.xcor() < -500):
        square1.setx(500)

object()
window.listen()
while(True):
    window.update()
    limits()
    #SCORE
    if (circle.distance(square1.xcor(), square1.ycor()) < 10):
        point.clear()
        points += 1
        convert = str(points)
        point.write("Points: " + convert, move=False, align="left", font=("Arial", 30, "normal"))
    collision()

    #MOVEMENT
    if keyboard.is_pressed('w'):
        up = 1
        down = 0
        left = 0
        right = 0
    elif keyboard.is_pressed('s'):
        up = 0
        down = 1
        left = 0
        right = 0
    elif keyboard.is_pressed('a'):
        up = 0
        down = 0
        left = 1
        right = 0
    elif keyboard.is_pressed('d'):
        up = 0
        down = 0
        left = 0
        right = 1
    elif keyboard.is_pressed('x'):
        up = 0
        down = 0
        left = 0
        right = 0
        pause.write("Game Paused - Press w, a, s, d to resume", move=False, align="center", font=("Arial", 30, "normal"))
        paused = True
    if (up == 0 and down == 0 and left == 0 and right == 0 and paused == True):
        while(paused):
            if keyboard.is_pressed('a'):
                pause.clear()
                break;
            elif keyboard.is_pressed('w'):
                pause.clear()
                break;
            elif keyboard.is_pressed('s'):
                pause.clear()
                break;
            elif keyboard.is_pressed('d'):
                pause.clear()
                break;


    if (up == 1):
        square1.sety(square1.ycor() + 3)
    elif (down == 1):
        square1.sety(square1.ycor() - 3)
    elif (left == 1):
        square1.setx(square1.xcor() - 3)
    elif (right == 1):
        square1.setx(square1.xcor() + 3)

done()