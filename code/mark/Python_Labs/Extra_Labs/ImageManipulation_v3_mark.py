from PIL import Image, ImageDraw
from random import choice

def draw_stick_figure(img, leg_length, leg_spread, arm_length, arm_spread, center_of_body, head_x, head_y, head_radius, body_length, color_list):
    diameter = 2*head_radius
    draw.ellipse((center_of_body-head_radius, 0, center_of_body + head_radius, diameter), fill=choice(color_list))
    draw.line((center_of_body,diameter, center_of_body, diameter + body_length), fill=choice(color_list))
    draw.line((center_of_body, (diameter + body_length)/2, center_of_body - arm_spread, (diameter + body_length)/2 + arm_length ), fill=choice(color_list))
    draw.line((center_of_body, (diameter + body_length)/2, center_of_body + arm_spread, (diameter + body_length)/2 + arm_length ), fill=choice(color_list))
    draw.line((center_of_body, diameter + body_length, center_of_body - leg_spread, diameter + body_length + leg_length ), fill=choice(color_list))
    draw.line((center_of_body, diameter + body_length, center_of_body + leg_spread, diameter + body_length + leg_length ), fill=choice(color_list))
    img.show()

if __name__ == '__main__':
    color_list = ['red','blue','green','yellow','brown','orange','purple']
    width = 1000
    height = 1000
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    center_of_body = width/2
    head_x = width/2
    head_y = height/2
    head_radius = 100
    body_length = 300
    diameter = 2*head_radius
    leg_length = 300
    leg_spread = 50
    arm_length = 250
    arm_spread = 100
    draw_stick_figure(img, leg_length, leg_spread, arm_length, arm_spread, center_of_body, head_x, head_y, head_radius, body_length, color_list)
    