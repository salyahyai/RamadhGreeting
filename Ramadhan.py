#import libs
import turtle
import random
import time
import playsound

pen = turtle.Turtle()
turtle.setup(1000,600)
pen.shape("turtle")


#Add background
turtle.bgpic("Ramadhan.png")

#prepare to draw the first Minarah
pen.color("yellow")
pen.up()
pen.goto(-40,-270)
pen.down()
pen.pensize(3)
pen.seth(90)
time.sleep( 2 )

#Read Quran on the background
playsound.playsound('Baqara_183.mp3',False)

#1  1st minarah
pen.fd(200)
pen.right(25)
pen.fd(60)
pen.right(135)
pen.fd(60)
pen.right(20)
pen.fd(150)

#2 Qubah1
pen.seth(90)
pen.circle(-45,180)

#3 2nd Minarah
pen.seth(90)
pen.fd(260)
pen.right(25)
pen.fd(60)
pen.right(130)
pen.fd(60)
pen.right(25)
pen.fd(240)

#4 Qubah2
pen.seth(90)
pen.circle(-70,180)

#5 3rd Minarah
pen.seth(90)
pen.fd(250)
pen.right(25)
pen.fd(60)
pen.right(130)
pen.fd(60)
pen.right(25)
pen.fd(280)

#6 Qubah3
pen.seth(90)
pen.circle(-50,180)
 
#7 4th Minarah
pen.seth(90)
pen.fd(170)
pen.right(25)
pen.fd(45)
pen.right(130)
pen.fd(45)
pen.right(25)
pen.fd(280)

#Draw the Star
pen.up()
pen.goto(-380,100)
pen.down()

pen.color("white","white")
pen.begin_fill()
for i in range(5):
    pen.forward(30)
    pen.right(144)
     
pen.end_fill()


#Write Ramadhan Mubarak
pen.up()
pen.goto(-450,-100)
pen.down()
pen.color("white")
msg="Ramadhan Mubarak"
pen.write(msg, move=False, align="left", font=("Arial", 15, "bold"))

#Write تقبل الله طاعاتكم
pen.up()
pen.goto(0,160)
pen.down()
pen.color("white")
msg="تقبل الله طاعاتكم"
pen.write(msg, move=False, align="left", font=("VIP Arabic Typo", 15, "normal"))

#Write the year
pen.up()
pen.goto(-230,80)
pen.down()
pen.color("white")
msg="1442" + "هـ"
pen.write(msg, move=False, align="left", font=("VIP Arabic Typo", 13, "normal"))



pen.up()
pen.goto(-430,-200)
pen.down()
msg="المبرمجون_يغيرون_العالم#"
pen.write(msg, move=False, align="left", font=("Arial", 14, "bold"))

# Stamp it with @SultanAl_Yahyai
pen.color("yellow")
pen.up()
pen.goto(-450,220)
pen.down()
msg="@SultanAl_Yahyai"
pen.write(msg, move=False, align="left", font=("Arial", 10, "bold"))


#Hide the Turtle logo
pen.hideturtle()