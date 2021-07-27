"""Lab 1 for David Swartwood in Class Lemur"""

from turtle import *
#Head
i = 0
while i < 200:
    forward(2)
    left(360/200)
    i = i + 1
armlength=100
necklength=20
leglength=130
bodyength=80
#neck
right(90)
forward(necklength)
#arms
right(110)
forward (armlength)
back(armlength)
right(140)
forward (armlength)
back(armlength)
#body
right(110)
forward(bodyength)
#legs
right(15)
forward (leglength)
back(leglength)
left(30)
forward (leglength)
back(leglength)


done()