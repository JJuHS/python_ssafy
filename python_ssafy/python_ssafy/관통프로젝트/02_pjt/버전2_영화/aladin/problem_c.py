import requests
from pprint import pprint
import json

ttbkey = 'ttbghtjd15511032001'
Query = '파울로 코엘료'

query_type = 'Author'
max_results = 20
start = 1
search_target = 'Book'
output = 'js'
version = 20131101

URL = f'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&Query={Query}&QueryType={query_type}&MaxResults={max_results}&start={start}&SearchTarget={search_target}&output={output}&Version={version}'

response = requests.get(URL)
response = response.json()
books = response['item']

sorted_books = sorted(books, key= lambda x:x['salesPoint'], reverse=True)

def bestseller_book(books_):
    return [book['title'] for book in books_[:5]]


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(bestseller_book(sorted_books))
