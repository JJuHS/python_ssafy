import json
from pprint import pprint
import os

script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)

def book_info(book):
    book_info_dict = {}
    book_info_dict['author'] = book['author']
    book_info_dict['categoryId'] = book['categoryId']
    book_info_dict['cover'] = book['cover']
    book_info_dict['description'] = book['description']
    book_info_dict['id'] = book['id']
    book_info_dict['priceSales'] = book['priceSales']
    book_info_dict['title'] = book['title']
    return book_info_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    pprint(book_info(book))
