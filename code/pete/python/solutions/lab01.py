from turtle import *

speed('fastest')
bgcolor('black')
rainbow = [
    '#8C00FC',
    '#3500FF',
    '#01FE01',
    '#FFFE37',
    '#FF8600',
    '#ED0003',
]
setpos((0.0, 60.0))

rainbow_index = 0
move_dist = 1
turn_deg = 1

while True:
    rainbow_color = rainbow[rainbow_index % len(rainbow)]
    color(rainbow_color)
    forward(move_dist)
    right(turn_deg)
    rainbow_index += 1
    move_dist += 1
    turn_deg += 1
