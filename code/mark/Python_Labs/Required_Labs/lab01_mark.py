from turtle import *
import random

list_of_colors = ['yellow','red','blue','green','purple','black']
speed("fastest")
def get_user_input():
    while True:
        try: 
            user_input = int(input("How many people (1-7) would you like to draw: "))
        except ValueError:
            print("That is not a valid entry. Please enter an integer between 1 and 7")
            continue
        else:
            if user_input > 7 or user_input < 1:
                 print("That is not a valid entry. Please enter an integer between 1 and 7")
                 continue
            else:
                break
    return user_input

def draw_person(colors):
    # head
    color = random.choice(colors)
    fillcolor(color)
    begin_fill()
    i = 0
    while i < 100:
        forward(2)
        left(360/100)
        i += 1
    end_fill()
    # neck
    right(90)
    forward(40)
    # arms
    right(90)
    forward(50)
    right(180)
    forward(100)
    right(180)
    forward(50)
    # lower body
    left(90)
    forward(60)
    # legs
    right(30)
    forward(90)
    right(180)
    forward(90)
    right(120)
    forward(90)
    #reset pen direction
    left(60)

def move_pen_position(x_postion, y_position):
    penup()
    setposition(x_postion,y_position)
    pendown()

def repeat_draw(x_start, y_start, colors, number_of_people):
    i = 0
    while i < number_of_people:
        move_pen_position(x_start + (i*100), y_start)
        draw_person(colors)
        i += 1
def main():
    number_of_people = get_user_input()
    repeat_draw(-400,200, list_of_colors, number_of_people)

main()