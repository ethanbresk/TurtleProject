import turtle
from random import randint
from tkinter import *
wn = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.width(1)
wn.title("Turtle Project - Ethan Bresk")

z = 50
class TurtleProject():
    #Randomizing the turtle functions
    def randomizer():
        wn.tracer(0)
        for i in range(6):
            y = randint(1,3)
            if y == 1:
                TurtleProject.drawSpiral()
            if y == 2:
                TurtleProject.drawSquareSpiral()
            if y == 3:
                TurtleProject.drawTriangleSpiral()
        wn.update()
    #Creating turtle functions
    def drawSpiral():
        global z
        for i in range(36):
            t.circle(z)
            t.right(10)
            x = i % 10
            if i == 0 or x == 0:
                t.pencolor("blue")
            if i == 1 or x == 1:
                t.pencolor("turquoise")
            if i == 2 or x == 2:
                t.pencolor("green")
            if i == 3 or x == 3:
                t.pencolor("yellow")
            if i == 4 or x == 4:
                t.pencolor("orange")
            if i == 5 or x == 5:
                t.pencolor("red")
            if i == 6 or x == 6:
                t.pencolor("maroon")
            if i == 7 or x == 7:
                t.pencolor("violet")
            if i == 8 or x == 8:
                t.pencolor("magenta")
            if i == 9 or x == 9:
                t.pencolor("purple")
        z += 25
    def drawSquareSpiral():
        global z
        for i in range(36):
            t.forward(z*1.5)
            t.right(90)
            t.forward(z*1.5)
            t.right(90)
            t.forward(z*1.5)
            t.right(90)
            t.forward(z*1.5)
            t.right(90)
            t.right(10)
            x = i % 10
            if i == 0 or x == 0:
                t.pencolor("blue")
            if i == 1 or x == 1:
                t.pencolor("turquoise")
            if i == 2 or x == 2:
                t.pencolor("green")
            if i == 3 or x == 3:
                t.pencolor("yellow")
            if i == 4 or x == 4:
                t.pencolor("orange")
            if i == 5 or x == 5:
                t.pencolor("red")
            if i == 6 or x == 6:
                t.pencolor("maroon")
            if i == 7 or x == 7:
                t.pencolor("violet")
            if i == 8 or x == 8:
                t.pencolor("magenta")
            if i == 9 or x == 9:
                t.pencolor("purple")
        z += 25
    def drawTriangleSpiral():
        global z
        for i in range(36):
            t.forward(z*1.5)
            t.right(120)
            t.forward(z*1.5)
            t.right(120)
            t.forward(z*1.5)
            t.right(120)
            t.right(10)
            x = i % 10
            if i == 0 or x == 0:
                t.pencolor("blue")
            if i == 1 or x == 1:
                t.pencolor("turquoise")
            if i == 2 or x == 2:
                t.pencolor("green")
            if i == 3 or x == 3:
                t.pencolor("yellow")
            if i == 4 or x == 4:
                t.pencolor("orange")
            if i == 5 or x == 5:
                t.pencolor("red")
            if i == 6 or x == 6:
                t.pencolor("maroon")
            if i == 7 or x == 7:
                t.pencolor("violet")
            if i == 8 or x == 8:
                t.pencolor("magenta")
            if i == 9 or x == 9:
                t.pencolor("purple")
        z += 25
    def drawStars():
        t.pencolor("white")
        t.fillcolor("white")
        t.begin_fill()
        for i in range(30):
            t.penup()
            t.end_fill()
            star_y = randint(-400,400)
            star_x = randint(-400,400)
            t.goto(star_x,star_y)
            t.pendown()
            t.begin_fill()
            for i in range(5):
                t.forward(10)
                t.right(144)

win = Tk()
win.geometry("225x75")
#Text
text = Label(win, text="Generate a random design:", font=("Arial",12)).place(x=15,y=5)
#Button click
def buttonClick():
    global z
    t.clear()
    t.penup()
    t.goto(0,0)
    z=50
    t.pendown()
    TurtleProject.randomizer()
    TurtleProject.drawStars()
#Button
button = Button(win, text="Generate", font=("Arial",12),height=1,width=20, command=buttonClick).place(x=15,y=35)
TurtleProject.randomizer()
TurtleProject.drawStars()
turtle.exitonclick()