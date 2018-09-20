import turtle
##8-квадратная спираль
#m=10
#a = 5
#for _ in range(10):
#    for _ in range(4):
#        turtle.shape('turtle')
#        turtle.forward(m)
#        m += a
#        #a += 2
#        turtle.left(90)


##5-больше квадратов
#m = 20
#a = 10
#for _ in range(10):
#    for _ in range(4):
#        turtle.shape('turtle')
#        turtle.forward(m)
#        turtle.left(90)
#    m += a
#    turtle.penup()
#    turtle.right(90)
#    turtle.forward(a/2)
#    turtle.right(90)
#    turtle.forward(a/2)
#    turtle.left(180)
#    turtle.pendown()


##7-спираль (Архимедова спираль)
#m = 10
#a = 10.0
#for _ in range(100):
#    turtle.shape('turtle')
#    turtle.forward(5)
#    turtle.left(a)
#    a -= 0.04

##9-Правильные многоугольники
#from math import sin, radians
#
#def rect(iters,m):
#    r = m / (2 * sin(radians(360 / (2 * 3))))
#    b = r
#    for iter in range(3, iters+1):
#        a = 180 - 360 / iter
#        turtle.shape('turtle')
#        turtle.left(a/2)
#        for _ in range(iter):
#            turtle.left(180 - a)
#            turtle.forward(m)
#
#        turtle.penup()
#        turtle.right(a/2)
#        turtle.forward(r)
#        turtle.pendown()
#
#        b += r
#        m = sin(radians(360 / (2 * (iter+1)))) * (2 * b)
#
#
#rect(15, 70)

##10-Цветок
#leafs = 3
#m = 5
#a = 360 / 100
#alfa = 0
#def flower(alfa):
#    turtle.shape('turtle')
#    turtle.left(alfa)
#    for _ in range(100):
#        turtle.left(a)
#        turtle.forward(m)
#    for _ in range(100):
#        turtle.right(a)
#        turtle.forward(m)
#
#for _ in range(leafs):
#    flower(alfa)
#    alfa+=45

