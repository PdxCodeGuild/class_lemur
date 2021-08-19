import pandas as pd

file='C:/Users/DavidSwartwood/codeguild/class_lemur/code/swarty/flask/Cars/cars.json'
updated=f'C:/Users/DavidSwartwood/codeguild/class_lemur/code/swarty/flask/Cars/carpd.json'

with open(file, 'r') as file:
    cars=file.read()

print(cars)
brands=cars('cars')
print(brands)