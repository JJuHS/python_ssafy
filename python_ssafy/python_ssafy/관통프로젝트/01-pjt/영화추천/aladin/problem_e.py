import json
import os

script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)

def new_books(books):
    new_book_list = []
    for book in books:
        book_id = book['id']
        temp_book = json.load(open(f'data/books/{book_id}.json', encoding='utf-8'))
        temp_year = temp_book['pubDate'][:4]
        if temp_year == '2023':
            new_book_list.append(book['title'])
    return new_book_list

if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(new_books(books_list))
