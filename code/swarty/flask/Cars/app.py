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
from markupsafe import Markup


app = Flask(__name__)
# 127.0.0.1:5000/

file1='C:/Users/DavidSwartwood/codeguild/class_lemur/code/swarty/flask/Cars/cars.json'
#Original=f'C:/Users/DavidSwartwood/codeguild/class_lemur/code/swarty/flask/Cars/carsorig.json'
#get file
def read_brands():
    with open(file1, 'r') as file:
        jfile=json.loads(file.read())
    brands=jfile['cars']
    return brands

    return brands
#Write back to JSON as dict
def write_brands(brands):
    jfile={'cars': brands}
    with open(file1, 'w') as file:
        file.write(json.dumps(jfile, indent=4))


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Sent a GET request, this view lists all of the Brands.
    Sent a POST request, this view adds a new brand to the
    json file, and redirects back to the same view with a GET request
    """   
    if request.method == 'POST':
        brands=read_brands()
        # extract new brand data from request.form
        while request.form != brands:
            brands.append(dict(request.form))
        brands=sorted(brands, key=lambda i:i['Brand'])
        print(brands)
        
        # add new brand dictionary to brands list
        write_brands(brands)
        # car_data = pd.DataFrame(brands).style 
        # car_data=car_data.hide_index() 
        # cars=Markup(car_data.to_html(table_uuid='panda'))
        # return render_template('index.html', cars=cars) # redirect back to the same view, as a GET request
    brands=read_brands()
    car_data = pd.DataFrame(brands).style 
    car_data=car_data.hide_index() 
    cars=Markup(car_data.to_html(table_uuid='panda'))
    # render index template, passing brands list as a context kwarg
    # print(car_data)
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
