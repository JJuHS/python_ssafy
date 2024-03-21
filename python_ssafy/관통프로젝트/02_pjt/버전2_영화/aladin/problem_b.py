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

def best_review_books(books_):
    tmp_list = []
    for book in books_:
        if book['customerReviewRank'] >= 9:
            tmp_list.append(book)
    return tmp_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(best_review_books(books))
