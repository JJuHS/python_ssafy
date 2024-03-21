import json
import os
import copy
from pprint import pprint
script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)

def sorted_cs_books_by_price(books, categories):
    books_list = []
    for i in range(len(books)):
        category_id_temp = books[i]['categoryId']
        if 2721 in category_id_temp:
            books_list.append(books[i])
    new_book_list = {}

    for book in books_list:
        new_book_list[book['title']] = book['priceSales']
    new_book_list = list(sorted(new_book_list.items(), key=lambda x: x[1], reverse=True))

    result_list = [new_book_list[i][0] for i in range(len(new_book_list))]
    return result_list
            


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(sorted_cs_books_by_price(books, categories_list))
