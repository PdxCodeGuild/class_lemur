from PIL import Image

img = Image.open("Lenna.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r,g,b = pixels[i,j]
        y = int(.299*r + .587*g + .114*b)
        pixels[i,j] = (y,y,y)

img.show()