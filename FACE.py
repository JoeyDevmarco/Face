#created by Joey De Marco: Joeyandstuff.neocities.org
#import libs
import time
import turtle as tur


#setup turtle

tur.turtlesize(.001)
tur.title("Face")
tur.speed(10)
tur.turtlesize(1)


#Smile

def smile():
    tur.clearscreen()
    tur.goto(0,0)
    tur.pendown()
    tur.circle(radius=100)
    tur.penup()
    tur.goto(-50, 131)
    tur.down()
    tur.circle(10)
    tur.penup()
    tur.goto(50, 131)
    tur.pendown()
    tur.circle(10)
    tur.up()
    tur.goto(-40, 84)
    tur.down()
    tur.right(90)
    tur.circle(40, 180)
    tur.penup()
    tur.goto(-500, -300)
    time.sleep(5.5)
    menu()
#neutral

def neutral():
    tur.clearscreen()
    tur.goto(0,0)
    tur.pendown()
    tur.circle(radius=100)
    tur.penup()
    tur.goto(-50, 131)
    tur.down()
    tur.circle(10)
    tur.penup()
    tur.goto(50, 131)
    tur.pendown()
    tur.circle(10)
    tur.up()
    tur.goto(-82, 84)
    tur.forward(50)
    tur.pendown()
    tur.goto(32,84)
    tur.penup()
    tur.goto(-500,-300)
    time.sleep(5)
    menu()

#frown

def frown():
    tur.clearscreen()
    tur.goto(0,0)
    tur.pendown()
    tur.circle(radius=100)
    tur.penup()
    tur.goto(-50, 131)
    tur.down()
    tur.circle(10)
    tur.penup()
    tur.goto(50, 131)
    tur.pendown()
    tur.circle(10)
    tur.up()
    tur.goto(-40, 84)
    tur.up()
    tur.forward(80)
    tur.rt(90)
    tur.forward(10)
    tur.down()
    tur.circle(-40, -180)
    tur.up()
    tur.goto(-500,-300)
    time.sleep(5)
    menu()













#menu
def menu():
    tur.clearscreen()
    tur.up()
    tur.goto(-361, -164)
    tur.down()
    tur.forward(200)
    tur.rt(90)
    tur.forward(100)
    tur.rt(90)
    tur.forward(200)
    tur.rt(90)
    tur.forward(100)
    tur.up()
    tur.goto(-343.0, -165.0)
    tur.rt(90)
    tur.write("MENU: Press corresponding number. ")
    tur.goto(-353, -180)
    tur.write("1. Smiley")
    tur.rt(90)
    tur.forward(15)
    tur.left(90)
    tur.write("2. Neutral")
    tur.rt(90)
    tur.forward(15)
    tur.left(90)
    tur.write("3. Frown")
    tur.listen()
    tur.onkeypress(smile, "1")
    tur.onkeypress(neutral,"2")
    tur.onkeypress(frown,"3")
    tur.goto(-500, -300)

menu()


tur.done()
