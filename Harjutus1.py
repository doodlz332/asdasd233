import turtle

#liikumine
turtle.penup()#pliiats üles
turtle.goto(-400,200)#asukoht
turtle.pendown()#pliiats alla
#kolmnurk
for i in range (3): #tsükkel x3
    turtle.fd(200) #pikkus forward
    turtle.left(120) #kraadid väliskülg

turtle.penup()
turtle.goto(-40,375)
turtle.pendown()
t=turtle

t.forward(100)
t.backward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.backward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)



turtle.done()
