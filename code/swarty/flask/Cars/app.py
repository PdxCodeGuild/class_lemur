'''
Version 1: GET all Brands
Your Flask app will read your JSON file and list all the data on your home page (localhost:500/).

Version 2 (Optional): POST a new brand
Include a form on your home page for the user to submit a new entry to your json database through a POST request.

Version 3 (Optional): GET individual Brands
Create a detail view and detail.html template to serve individual pages for each brand (localhost:5000/Portland).
 Also, alter the home page to show links to each brand.

Version 4 (Optional): PATCH requests to detail view
Add a form with method="PATCH" to your detail page for users to send patch requests (updates) to the detail view.

Version 5 (Optional): DELETE requests to detail view
Add a form with method="DELETE" to your detail page so users can delete an entry from the json database. 
The form can have just a submit button inside.
'''
from flask import Flask, render_template, request
import pandas as pd
import json



app = Flask(__name__)
# 127.0.0.1:5000/

file='C:/Users/DavidSwartwood/codeguild/class_lemur/code/swarty/flask/Cars/cars.json'
#Original=f'C:/Users/DavidSwartwood/codeguild/class_lemur/code/swarty/flask/Cars/carsorig.json'
#get file and convert to Pandas
def read_brands():
    global file
    with open(file, 'r') as file:
        jfile=json.loads(file.read())
    brands=jfile['cars']
    car_data=pd.DataFrame(brands)
    car_data=car_data.set_index('brand')
    return car_data
#Write back to JSON as dict
def write_brands(car_data):
    global file
    carsdict=pd_to_dict(car_data)
    with open(file, 'w') as file:
        file.write(json.dumps(carsdict, indent=4))
    
#Covert back to dic from pandas
def pd_to_dict(car_data):
    car_data=car_data.reset_index()
    cars=car_data.to_dict(orient='index')
    carsdict={ 'cars':[]}
    for key in cars:
        carsdict['cars'].append(cars[key])
    return carsdict




@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Sent a GET request, this view lists all of the Brands.
    Sent a POST request, this view adds a new brand to the
    json file, and redirects back to the same view with a GET request
    """
    # if request.method == 'POST':
    #     car_data = read_brands()
        
    #     # extract new brand data from request.form
        
    #     # add new brand dictionary to brands list
        
    #     write_brands(car_data) # write updated brands to json file
    #     return render_template('/') # redirect back to the same view, as a GET request
    car_data = read_brands() # read brands from json file
    cars=car_data.style.to_html()
    # render index template, passing brands list as a context kwarg
    # print(car_data)
    # print(cars)
    return render_template('index.html', cars=cars)


# 127.0.0.1:5000/Portland
# @app.route('/<name>/', methods=['GET', 'PATCH', 'DELETE'])
# def detail(name):
#     """
#     Sent a GET request, this view shows detailed information about one brand
#     Sent a PATCH request, this view updates the information for that brand
#     Sent a DELETE request, this view deletes that brand from the json file
#     PATCH requests redirect back to this route as a GET request
#     DELETE requests redirect back to the home page
#     """
#     # read json files to get car list
#     # find the right Brand
#     Brand ='???'

#     if request.method == 'PATCH':
#         # extract data from form
#         # update Brand in list of dictionaries
#         # write file
#         # redirect to Brand's GET request
#         return redirect(f'/{name}/') # what if the PATCH request changes the Brand's name?
    
#     if request.method == 'DELETE':
#         # remove brand from list of brands
# 		# write file
#         # redirect back to home page
#         return redirect('/')

#     # render detail template with that Brand as a context kwarg
#     return render_template('detail.html', brand=brand)


app.run(debug=True)
