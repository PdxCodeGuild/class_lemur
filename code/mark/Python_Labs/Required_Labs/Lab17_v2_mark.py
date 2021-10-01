import json
import requests

def get_search_keyword():
    search_keyword = input("\nEnter a keyword to search for quotes: ")
    main(search_keyword)

def get_quotes_by_page(url, headers, filter, page):
    params = {
        'page': page,
        'filter': filter
    }
    response = requests.get(url, headers=headers, params=params).json()
    last_page = response.get('last_page')
    quotes_dict = {}
    quotes_list = response.get('quotes')
    for quote in quotes_list:
        author = quote.get("author")
        quote_body = quote.get("body")
        quotes_dict[quote_body] = author
    no_quotes_found = check_if_quotes(quotes_dict)
    if no_quotes_found == True:
        return quotes_dict, True
    else:
        return quotes_dict, last_page

def check_if_quotes(quotes_dict, ):
    values_list = list(quotes_dict.values())
    if values_list[0] == None:
        return True
    else:
        return False

def print_page_of_quotes(results_dict):
    for k,v in results_dict.items():
        print(f"\n{k} - {v}")

def main(search_keyword):
    page = 1
    results_dict, last_page = get_quotes_by_page(url, headers, search_keyword, page)
    print_page_of_quotes(results_dict)
    while True:
        if last_page == True:
            return print(f"\n\nThere are no more pages of quotes for {search_keyword}.")
        next_or_done = input("\nEnter 'next page' or 'done': ")
        if next_or_done == 'next page':
            page += 1
            results_dict, last_page = get_quotes_by_page(url, headers, search_keyword, page)
            print_page_of_quotes(results_dict)
        elif next_or_done == 'done':
            return None
        else:
            print("I do not understand your response.  Please try again.")

if __name__ == '__main__':
    url = "https://favqs.com/api/quotes?"
    headers = {
        'Content-type': 'application/json',
        'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
    }
    
    get_search_keyword()
    while True:
        continue_or_quit = input("\nEnter 'y' to continue. ").lower()
        if continue_or_quit == 'y':
            get_search_keyword()
        else:
            break