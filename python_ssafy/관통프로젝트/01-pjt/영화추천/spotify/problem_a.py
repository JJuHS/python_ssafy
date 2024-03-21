import json
from pprint import pprint
import os

script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)

def artist_info(artist, genres):
    result_is = {}
    result_is['genres_ids'] = artist['genres_ids']
    result_is['id'] = artist['id']
    result_is["images"] = artist["images"]
    result_is['name'] = artist['name']
    result_is['type'] = artist['type']
    return result_is


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artist_dict, genres_list))
