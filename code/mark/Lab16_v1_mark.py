import requests
import cowsay
from time import sleep
import re

def get_user_input():
    options = {'cow': cowsay.cow, 'dragon': cowsay.dragon, 'penguin': cowsay.tux, 'kitty': cowsay.kitty, 'cat': cowsay.meow, 'turtle': cowsay.turtle, 'done': 'done'}
    while True:
        selection = input("Select an animal to tell you a joke or 'done' to quit: ").lower()
        if selection in options.keys():
            return options[selection]
        else:
            print("That animal is not available at this time.  Please select: ")
            for key in options.keys():
                print(key)
    
def get_joke(url):
    response =  requests.get(url, headers=headers).json()
    return response.get('joke')

def process_joke(joke_raw):
    joke_list = re.split(r'(?<=[.?!])\s*', joke_raw)
    return joke_list[:-1]

def print_joke(joke_list, animal):
    for joke in joke_list:
        animal(joke)
        sleep(4)

def main_loop():
    while True:
        animal = get_user_input()
        if animal == 'done':
            return print("Thank you for using the animal joke simulator!")
        joke_raw = get_joke(url)
        joke_list = process_joke(joke_raw)
        print_joke(joke_list, animal)

if __name__ == '__main__':
    url = "https://icanhazdadjoke.com"
    headers = {'Accept': 'application/json'}
    main_loop()


