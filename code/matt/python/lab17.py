import requests


def main():
    url = 'https://favqs.com/api/qotd'

    response = requests.get(url)

    data = response.json()
    quote = data['quote']
    print(f"{quote['author']} - {quote['body']}")

    def print_quotes(query, page, quotes):
        print(f'25 quotes associated with {query} - page {page}')
        for quote in quotes:
            print('-' * 40)
            print(quote['author'])
            print(quote['body'])

    def get_response(keyword_url, headers, params):
        response = requests.get(keyword_url, headers=headers, params=params)
        data = response.json()
        quotes = data.get('quotes')
        return quotes

    while True:
        page = 1
        keyword_url = 'https://favqs.com/api/quotes'
        headers = {
            'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
        query = input(
            'Input the keyword you want to search for or done to exit: ')
        params = {
            'filter': query,
            'page': page
        }
        if query == 'done':
            break

        quotes = get_response(keyword_url, headers, params)

        print_quotes(query, page, quotes)

        while True:
            print('-' * 40)
            next_page = input(
                "Hit enter for next page or 'done' to check for another keyword: ")

            if next_page == '':
                page += 1
                params = {
                    'filter': query,
                    'page': page
                }
                quotes = get_response(keyword_url, headers, params)

            print_quotes(query, page, quotes)

            if next_page == 'done':
                break


main()
