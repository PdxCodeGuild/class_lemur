import requests
import webbrowser

base_url = 'https://openlibrary.org'

# # subject search
# subject = input('What subject do you want to read? ')

# response = requests.get(base_url + f'/subjects/{subject}.json')

# # print(response)

# data = response.json()

# # print(data)

# # print(data.keys())

# works = data.get('works')

# # print(works)

# for work in works:
#     print(work['title'])

# general query search

q = input('What are you searching for? ')

params = {
    'q': q
}
response = requests.get(base_url + '/search.json', params=params)

data = response.json()

print(data.keys())

docs = data.get('docs')

# for i in range(len(docs)):
#     doc = docs[i]
#     print()
#     print(i)
#     print(doc.get('title'))
#     print(doc.get('key'))

for i, doc in enumerate(docs):
    print()
    print(i)
    print(doc.get('title'))
    if doc.get('author_name') is not None:
        for author in doc.get('author_name'):
            print(author)
    print(doc.get('key'))

index = int(input("Enter the number of the book you'd like to know more about: "))
doc = docs[index]
# print(doc['key'])

webbrowser.open(base_url + doc['key'])

# webbrowser test

# webbrowser.open('https://pdxcodeguild.com')