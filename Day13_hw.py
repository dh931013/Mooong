import turtle as t
import random  
a=random.randint(1,360)  
  
t.speed(3)
t.shape("turtle")
t.color("orange")
    
t.pensize(3)
t.up() 
t.goto(-250,-250)
t.down()
for x in range(4): 
     t.fd(500) 
     t.lt(90) 

t.up()
t.home()
t.down()

t.seth(a) 
while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:  
     t.fd(1) 
while True: 
     b=t.heading() 
     if 0<b<45 or 135<b<180 or 225<b<270: 
         if -250 < t.xcor() < 250  :  
             t.seth(360-b) 
             t.fd(1) 
             while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:  
                 t.fd(1) 
         else:  
             t.seth(180-b) 
             t.fd(1) 
             while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:  
                 t.fd(1) 
     if 45<b<135 or 270<b<315: 
         if -250 < t.xcor() < 250 :  
             t.seth(360-b) 
             t.fd(1) 
             while -250 < t.xcor() < 250 and -250 < t.ycor() < 250: 
                t.fd(1) 
         else: 
            t.seth(540-b) 
            t.fd(1) 
            while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:  
                 t.fd(1) 
     if 180<b<225 or 315<b<360: 
         if-250 < t.xcor() < 250 :  
             t.seth(360-b) 
             t.fd(1) 
             while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:  
                 t.fd(1) 
         else: 
             t.seth(540-b) 
             t.fd(1) 
             while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:  
                 t.fd(1) 
     if a == 0 or a == 45 or a == 90 or a == 135 or a == 180 or a == 225 or a == 270 or a == 315 or a == 360: 
         t.lt(180) 
         t.fd(1) 
         while -250 < t.xcor() < 250 and -250 < t.ycor() < 250: 
             t.fd(1)
