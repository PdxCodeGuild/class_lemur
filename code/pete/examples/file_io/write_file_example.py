# path = 'code/pete/examples/file_io/books/fire-and-ice.txt'
path = 'code/pete/examples/file_io/books/around-the-world-in-80-days.txt'
# improved_path = 'code/pete/examples/file_io/books/fire-and-ice-deluxe-version.txt'
improved_path = 'code/pete/examples/file_io/books/around-the-world-in-80-days-deluxe-version.txt'

with open(path, 'r', encoding='utf-8') as f:
    contents = f.read()

improved_poem = contents.upper()

with open(improved_path, 'w', encoding='utf-8') as f:
    f.write(improved_poem)