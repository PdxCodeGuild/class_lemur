'''
Version 1: GET all Cities
Your Flask app will read your JSON file and list all the data on your home page (localhost:500/).

Version 2 (Optional): POST a new City
Include a form on your home page for the user to submit a new entry to your json database through a POST request.

Version 3 (Optional): GET individual Cities
Create a detail view and detail.html template to serve individual pages for each city (localhost:5000/Portland).
 Also, alter the home page to show links to each city.

Version 4 (Optional): PATCH requests to detail view
Add a form with method="PATCH" to your detail page for users to send patch requests (updates) to the detail view.

Version 5 (Optional): DELETE requests to detail view
Add a form with method="DELETE" to your detail page so users can delete an entry from the json database. 
The form can have just a submit button inside.
'''

# 127.0.0.1:5000/
@app.route('/', methods=['GET', 'POST'])
def index():
    """
Sent a GET request, this view lists all of the cities.
Sent a POST request, this view adds a new city to the
json file, and redirects back to the same view with a GET request
    """
    if request.method == 'POST':
        cities = read_cities() # read cities from json file
        # extract new city data from request.form
        # add new city dictionary to cities list
        write_cities(cities) # write updated cities to json file
        return redirect('/') # redirect back to the same view, as a GET request
    cities = read_cities() # read cities from json file
    # render index template, passing cities list as a context kwarg
    return render_template('index.html', cities=cities)


# 127.0.0.1:5000/Portland
@app.route('/<name>/', methods=['GET', 'PATCH', 'DELETE'])
def detail(name):
    """
Sent a GET request, this view shows detailed information about one city
Sent a PATCH request, this view updates the information for that city
Sent a DELETE request, this view deletes that city from the json file
PATCH requests redirect back to this route as a GET request
DELETE requests redirect back to the home page
    """
    # read json files to get cities list
    # find the right city
    city ='???'

    if request.method == 'PATCH':
        # extract data from form
        # update city in list of dictionaries
        # write file
        # redirect to city's GET request
        return redirect(f'/{name}/') # what if the PATCH request changes the city's name?
    
    if request.method == 'DELETE':
        # remove city from list of cities
		# write file
        # redirect back to home page
        return redirect('/')

    # render detail template with that city as a context kwarg
    return render_template('detail.html', city=city)
