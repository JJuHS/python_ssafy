import json
from pprint import pprint
import os

script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)

def artist_info(artist):
    result_is = {}
    genre_id = artist['genres_ids']
    genres_dict = json.load(open('data/genres.json', encoding='utf-8'))
    genre_name = []
    for dict_is in genres_dict:
        if dict_is['id'] in genre_id:
            genre_name.append(dict_is['name'])
    
    result_is['genres'] = genre_name
    result_is['id'] = artist['id']
    result_is["images"] = artist["images"]
    result_is['name'] = artist['name']
    result_is['type'] = artist['type']
    return result_is

if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    pprint(artist_info(artist_dict))
