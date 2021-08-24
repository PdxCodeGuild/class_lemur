import pandas as pd
import json
import pprint as ppr


original='C:/Users/DavidSwartwood/codeguild/class_lemur/code/swarty/flask/Cars/cars.json'
updated=f'C:/Users/DavidSwartwood/codeguild/class_lemur/code/swarty/flask/Cars/carpd.json'





#cars=pd.read_json(file)
with open(original, 'r') as file:
    cars=json.loads(file.read())
print(cars)
brands=cars['cars']
car_data=pd.DataFrame(brands)
car_data=car_data.set_index('brand')
car_data=car_data.sort_values(by='brand')
print(car_data)
car_data=car_data.reset_index()
cars=car_data.to_dict(orient='index')
carsdict={ 'cars':[]}
for key in cars:
    carsdict['cars'].append(cars[key])

with open(updated, 'w') as updated:
        updated.write(json.dumps(carsdict, indent=4))

ppr.pp(carsdict)
