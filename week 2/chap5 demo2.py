import turtle as squirtle
import random as ran

squirtle.shape("turtle")
squirtle.speed(10)
squirtle.up()

def drawCircle (x, y):

    squirtle.fillcolor(ran.random(), ran.random(), 1)
    squirtle.goto(x, y)
    print (x,y)

    squirtle.down()
    squirtle.begin_fill()
    squirtle.circle(ran.randint(10,30))
    squirtle.end_fill()
    squirtle.up()

squirtle.title('Click on the Canvas')

squirtle.onscreenclick(drawCircle)
squirtle.mainloop()