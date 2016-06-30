import turtle as t
import random as r
sides=0
colors=["Black","Orange","Red","Blue","Green"]
def setup(pen,fill,width,length,x,y,speed):
    t.penup()
    t.setpos(x,y)
    t.pencolor(pen)
    t.fillcolor(fill)
    t.width(width)
    t.speed(speed)
    LENGTH=length
def shape(sides):
    t.pendown()
    t.begin_fill()
    for i in range(sides):
        t.fd(120/sides)
        t.rt(360/sides)
    t.end_fill()
    t.penup()
    t.fd(30)
def newshape():
    t.pencolor(colors[r.randint(0,4)])
    t.fillcolor(colors[r.randint(0,4)])
    t.fd(30)
def newline():
    t.setx(-350)
    t.sety(t.ycor()-60)
while True:
    setup("RED","BLACK",10,80,-350,350,1000)
    while(t.ycor()>-350):
        while(t.xcor()<350):
            sides=r.randint(3,6)
            shape(sides)
            newshape()
        newline()

        
        
