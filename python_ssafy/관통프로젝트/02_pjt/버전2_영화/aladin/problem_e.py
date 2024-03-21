import requests
from pprint import pprint

def ebook_list(title):
    ttbkey = 'ttbghtjd15511032001'
    Query = title
    query_type = 'Title'
    max_results = 1
    start = 1
    search_target = 'Book'
    output = 'js'
    version = 20131101

    URL = f'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&Query={Query}&QueryType={query_type}&MaxResults={max_results}&start={start}&SearchTarget={search_target}&output={output}&Version={version}'

    response = requests.get(URL)
    response = response.json()
    book_price_90 = 0.9 * response['item'][0]['priceSales']

    search_target2 = 'eBook'
    max_results = 20

    URL2 = f'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&Query={Query}&QueryType={query_type}&MaxResults={max_results}&start={start}&SearchTarget={search_target2}&output={output}&Version={version}'
    response = requests.get(URL2)
    response = response.json()
    ebooks = response['item']
    ebooks = sorted(ebooks, key= lambda x:x['priceSales'])
    ebooks_cheap = []
    
    for i in range(len(ebooks)):
        if ebooks[i]['priceSales'] < book_price_90:
            ebooks_cheap_tmp = {}
            ebooks_cheap_tmp['isbn'] = (ebooks[i]['isbn'])
            ebooks_cheap_tmp['itemId'] = (ebooks[i]['itemId'])
            ebooks_cheap_tmp['priceSales'] = (ebooks[i]['priceSales'])
            ebooks_cheap_tmp['link'] = (ebooks[i]['link'])
            ebooks_cheap.append(ebooks_cheap_tmp)
    return ebooks_cheap


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(ebook_list('베니스의 상인'))

    # pprint(ebook_list('*'))
