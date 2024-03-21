import json
from pprint import pprint
import os

script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)

def artist_info(artists, genres):
    genres_dict = json.load(open('data/genres.json', encoding='utf-8'))
    result_list = []

    for artist in artists:
        temp_dict = {}
        genre_id = artist['genres_ids']
        genre_name = []

        for dict_is in genres_dict:
            if dict_is['id'] in genre_id:
                genre_name.append(dict_is['name'])
        temp_dict['genres_names'] = genre_name
        temp_dict['id'] = artist['id']
        temp_dict['images'] = artist['images']
        temp_dict['name'] = artist['name']
        temp_dict['type'] = artist['type']
        result_list.append(temp_dict)
    return result_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))
