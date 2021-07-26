from turtle import *

penup()
setposition(100, 100)
pendown()

i = 0
while i < 100:
    forward(2)
    left(360/100)
    i = i + 1

penup()
setposition(-15, -72)
pendown()

fillcolor('pink')
begin_fill()

forward(200)
left(120)
forward(200)
left(120)
forward(200)
left(120)
forward(200)
left(120)

end_fill()


done()