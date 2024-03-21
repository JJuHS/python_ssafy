import json
from pprint import pprint
import os

script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)

def book_info(book, categories):
    result_dict = {}
    result_dict['author'] = book['author']
    category_ID = book['categoryId']
    category_name = []

    for find_ID in category_ID:
        for kind_of_book in categories:
            if find_ID == kind_of_book['id']:
                category_name.append(kind_of_book['name'])

    result_dict['categoryName'] = category_name
    result_dict['description'] = book['description']
    result_dict['id'] = book['id']
    result_dict['priceSales'] = book['priceSales']
    result_dict['title'] = book['title']
    result_dict['cover'] = book['cover']
    return result_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))

