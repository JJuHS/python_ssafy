"""
    장르에 acoustic이 포함된 아티스트 이름 목록 출력하기
"""

import json
from pprint import pprint
import os

script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)

artists = json.load(open('data/artists.json', encoding='utf-8'))
genres_dict = json.load(open('data/genres.json', encoding='utf-8'))
acoustic_id = 0

for genre in genres_dict:
    if genre['name'] == 'acoustic':
        acoustic_id = genre['id']

def acoustic_artists():
    result_list = []

    for artist in artists:
        if acoustic_id in artist['genres_ids']:
            result_list.append(artist['name'])
    return result_list


if __name__ == "__main__":
    pprint(acoustic_artists())
