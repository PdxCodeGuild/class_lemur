# Contacts List Redux

Create a Flask app that serves as a GUI (graphical user interface) version of your [Contacts List Python Lab](../../1%20Python/labs/12%20Contact%20List.md).

Transform your csv-formatted data into valid JSON (JavaScript Object Notation).  This example is of a list of `"cities"`, so change that key accordingly for your data.

```json
{
	"cities": [
		{
			"name": "Portland",
			"cuisine": "everything",
			"country": "USA",
			"weather": "temperate"
		},
		{
			"name": "Detroit",
			"cuisine": "Greek",
			"country": "USA",
			"weather": "temperate"
		},
		{
			"name": "D.C.",
			"cuisine": "ramen",
			"country": "USA",
			"weather": "temperate"
		},
		{
			"name": "Florence",
			"cuisine": "pasta",
			"country": "Italy",
			"weather": "hot"
		}
	]
}
```

### Note on JSON:
Formatting is very important.  Keys must have double-quotes.  VSCode will let you know if JSON is improperly formatted.


## JSON-reading functions

You can use these functions to read from and write to your json file.  Of course, change `cities` to the appropriate term.
```py
import json

app = Flask(__name__)

def read_cities():
    """
Reads the contents of cities.json and returns the list of cities
    """
    with open('cities.json', 'r') as f:
        data = json.load(f)
    return data.get('cities')

def write_cities(cities):
    """
Passed a list of cities, writes those cities to the json file
    """
    with open('cities.json', 'w') as f:
        json.dump({'cities': cities}, f)
```

### Version 1: GET all Cities

Your Flask app will read your JSON file and list all the data on your home page (`localhost:500/`).

### Version 2 (Optional): POST a new City

Include a form on your home page for the user to submit a new entry to your json database through a POST request.

#### This is what your home page might look like with Versions 1 & 2
![Versions 1 & 2](cities01.png)

### Version 3 (Optional): GET individual Cities

Create a `detail` view and `detail.html` template to serve individual pages for each city (`localhost:5000/Portland`).  Also, alter the home page to show links to each city.

#### Your index page might look like this after Version 3
![Version 3](cities02.png)

### Version 4 (Optional): PATCH requests to detail view
Add a form with `method="PATCH"` to your detail page for users to send patch requests (updates) to the `detail` view.

### Version 5 (Optional): DELETE requests to detail view
Add a form with `method="DELETE"` to your detail page so users can delete an entry from the json database.  The form can have just a submit button inside.

#### With Versions 3, 4 & 5, your detail page might look like this
![Versions 3, 4 & 5](cities03.png)

Feel free to use this starter code in your `app.py`:
```py
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
```