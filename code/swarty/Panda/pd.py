import pandas as pd
import json
file='C:/Users/DavidSwartwood/codeguild/class_lemur/code/swarty/flask/Cars/cars.json'
updated=f'C:/Users/DavidSwartwood/codeguild/class_lemur/code/swarty/flask/Cars/carpd.json'





#cars=pd.read_json(file)
with open(file, 'r') as file:
    cars=json.loads(file.read())
brands=cars['cars']
parked=pd.DataFrame(brands)
print(parked)


