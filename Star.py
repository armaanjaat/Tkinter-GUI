#turtle graphics
#star pattern

import turtle

star= turtle.Turtle() #own turtle created
star.penup()
star.goto((-200,100))
star.pendown()

star.getscreen().bgcolor("Green") #background color changed

def st(turtle,size):#Function created
    if size <= 10:
        return
    else:
        for i in range(5):#loop used
            turtle.speed(10)
            turtle.forward(size) #forwarding 10 pixels
            st(turtle,size/2)
            turtle.left(216) #turning 216 degrees left(Specific angle )
star.speed(10)
st(star,150)







turtle.done()
