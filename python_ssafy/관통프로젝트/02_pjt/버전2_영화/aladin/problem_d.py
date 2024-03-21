import requests
from pprint import pprint



def author_other_works(title):
    ttbkey = 'ttbghtjd15511032001'
    Query = title

    query_type = 'Title'
    max_results = 1
    start = 1
    search_target = 'Book'
    output = 'js'
    version = 20131101

    URL = f'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&Query={Query}&QueryType={query_type}&MaxResults={max_results}&start={start}&SearchTarget={search_target}&output={output}&Version={version}'

    def authors_book(author):
        Query = author
        query_type = 'Author'
        max_results = 30
        
        URL2 = f'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&Query={Query}&QueryType={query_type}&MaxResults={max_results}&start={start}&SearchTarget={search_target}&output={output}&Version={version}'

        response = requests.get(URL2)
        response = response.json()
        books = response['item']
        ISBN = []
        ISBN13 = []
        books_5 = []
        
        for book in books:
            if book['isbn'] in ISBN:
                continue
            elif book['isbn13'] in ISBN13:
                continue
            else:
                ISBN.append(book['isbn'])
                ISBN13.append(book['isbn13'])
                books_5.append(book['title'])
        return books_5[:5]
    
    response = requests.get(URL)
    response = response.json()
    books = response['item']
    if len(books) == 0:
        return None
    
    author_is = books[0]['author']
    author_is = author_is.split()
    try:
        num_ = author_is.index('(지은이)')
    except:
        num_ = author_is.index('(지은이),')
    author_is = author_is[:num_]
    author_is = ' '.join(author_is)
    
    return authors_book(author_is)
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(author_other_works('베니스의 상인'))

    pprint(author_other_works('개미'))

    pprint(author_other_works('*'))
