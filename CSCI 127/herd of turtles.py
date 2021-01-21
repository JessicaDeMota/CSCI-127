#Jessica De Mota Munoz
#Jessica.DeMotaMunoz86@myhunter.cuny.edu
#August, 29, 2018

import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("blue")



tess = turtle.Turtle()           # create tess and set some attributes
                                 #tess is a turtle that we created and assigned as you can have several turtles to move into different directions.tess is her own "instance"
                                 #so tess has her own function and what she is doing is using her pen size in a small dimmension in the color red.  
tess.color("red")
tess.pensize(5)

alex = turtle.Turtle()           # create alex
                                 # alex is a new instance she is used to import a new turtle that allows her to create the square
                                 #since alex isn't necessiraly using a different pen color she doesn't have to be assigned a color nor pen size. 
                                 

tess.forward(80)                 # Let tess draw an equilateral triangle
                                 #since we're starting to create an equilateral triangle, from a circle as making it a 360 .
                                 #so the reason as to why she uses 120 is because the exterior angle of an equilateral triangle is 120.
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                   # complete the triangle

tess.right(180)                  # turn tess around
tess.forward(80)                 # move her away from the origin

alex.forward(50)                 # make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()
