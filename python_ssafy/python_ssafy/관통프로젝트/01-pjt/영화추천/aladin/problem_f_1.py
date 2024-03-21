import json
import os

script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)


def best_new_books(books):
    new_book_list = {}
    for book in books:
        book_id = book['id']
        temp_book = json.load(open(f'data/books/{book_id}.json', encoding='utf-8'))
        temp_year = temp_book['pubDate'][:4]
        if temp_year == '2023':
            new_book_list[book['title']] = temp_book['customerReviewRank']
    new_book_list = list(sorted(new_book_list.items(), key=lambda x: x[1], reverse=True))
    new_book_list_result=[]

    for i in range(len(new_book_list)):
        a = new_book_list[i][0]
        b = str(i+1) + '등 : ' + a
        new_book_list_result.append(b)
        
    return new_book_list_result



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_new_books(books_list))
