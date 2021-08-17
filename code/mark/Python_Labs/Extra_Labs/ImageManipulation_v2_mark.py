import colorsys
from PIL import Image

def convert_to_rgb(h,s,v):
    r,g,b = colorsys.hsv_to_rgb(h,s,v)
    r = int(r*255)
    g = int(g*255)
    b = int(b*255)
    return r,g,b

def get_user_input():
    input_options = ['H','S','V']
    while True:
        user_input = input("\nWhich variable would you like to change (H,S,V)? ").capitalize()
        if user_input in input_options:
            break
    
    while True:
        try:
            amount_input = float(input("\nEnter numerical amount for adjustment: "))
            break
        except:
            print("That was not a valid input")

    return user_input, amount_input
        
    


if __name__ == '__main__':
    image_file = ("Lenna.png")
    img = Image.open(image_file)
    width, height = img.size
    pixels = img.load()

    variable, amount = get_user_input()
    for i in range(width):
        for j in range(height):
            r,g,b = pixels[i,j]
            h,s,v = colorsys.rgb_to_hsv(r/255,g/255,b/255)
            if variable == 'H':
                h = h + amount/360
            if variable == 'S':
                s = s * amount
            if variable == 'V':
                v = v * amount
            pixels[i,j] = convert_to_rgb(h,s,v)



    img.show()