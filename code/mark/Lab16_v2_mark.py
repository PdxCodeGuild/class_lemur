import requests
import cowsay
from time import sleep
import re

def select_animal():
    options = {'cow': cowsay.cow, 'dragon': cowsay.dragon, 'penguin': cowsay.tux, 'kitty': cowsay.kitty, 'cat': cowsay.meow, 'turtle': cowsay.turtle, 'done': 'done'}
    while True:
        selection = input("Select an animal to tell you a joke or 'done' to quit: ").lower()
        if selection in options.keys():
            return options[selection]
        else:
            print("That animal is not available at this time.  Please select: ")
            for key in options.keys():
                print(key)

def search_term():
    return input("\nSelect a keyword for your joke category: ")
    
def get_jokes(url, headers, term):
    list_of_jokes = []
    params = {
        'term': term 
    }
    response =  requests.get(url, headers=headers, params=params).json()
    results = response.get('results')
    for result in results:
        list_of_jokes.append(result.get('joke'))
    return list_of_jokes

def process_joke(joke_raw):
    joke_sentence_list = re.split(r'(?<=[.?!])\s*', joke_raw)
    return joke_sentence_list[:-1]

def print_joke(joke_list, animal):
    for joke in joke_list:
        animal(joke)
        sleep(4)

def loop_through_joke_list(list_of_jokes, term, animal):
    print(f"We have found {len(list_of_jokes)} jokes about {term}")
    for i in range(len(list_of_jokes)):
        next_joke = input(f"\nEnter 'y' for a joke about {term} or any other key to return to selection: ")
        if next_joke != 'y' or i >= len(list_of_jokes):
            return
        else:
            joke_list = process_joke(list_of_jokes[i])
            print_joke(joke_list, animal)

def main_loop(url,headers):
    while True:
        animal = select_animal()
        if animal == 'done':
            return print("Thank you for using the animal joke simulator!")
        term = search_term()
        list_of_jokes = get_jokes(url, headers, term)
        loop_through_joke_list(list_of_jokes, term, animal)

if __name__ == '__main__':
    url = "https://icanhazdadjoke.com/search"
    headers = {'Accept': 'application/json'}
    main_loop(url, headers)


