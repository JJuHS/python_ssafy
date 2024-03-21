import json
import os

script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)

def best_book(books):
    review_winner = ''
    review_num = 0
    for book in books:
        book_id = book['id']
        temp_book = json.load(open(f'data/books/{book_id}.json', encoding='utf-8'))
        review_book = temp_book['customerReviewRank']
        if review_book > review_num:
            review_winner = book['title']
            review_num = review_book
    return review_winner

if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_book(books_list))
