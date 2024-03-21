"""
    팔로워가 5,000,000이상, 10,000,000미만인 아티스트들을 
    아티스트 이름과 팔로워를 목록으로 출력하기
"""

import json
from pprint import pprint
import os

script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)


artists = json.load(open('data/artists.json', encoding='utf-8'))

def get_popular():
    result_list = []

    for artist in artists:
        artist_follow = {}
        Id_number = artist['id']
        artist_profile_temp = json.load(open(f"data/artists/{Id_number}.json", encoding="utf-8"))
        if 5000000 <= artist_profile_temp['followers']['total'] < 10000000:
            
            artist_follow['name'] = artist['name']
            artist_follow['followers'] = artist_profile_temp['followers']['total']
            result_list.append(artist_follow)
    
    return result_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    pprint(get_popular())
