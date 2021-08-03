import os

books = os.listdir('books')
print(books)
# print(os.path)

for book in books:
    with open('books/' + book, 'r') as f:
        print(f.read())