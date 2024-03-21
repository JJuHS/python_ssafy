import json
import os

script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)

def dec_artists(artists):
    result_list = []

    for artist in artists:
        artist_follow = {}
        Id_number = artist['id']
        artist_profile_temp = json.load(open(f"data/artists/{Id_number}.json", encoding="utf-8"))
        if artist_profile_temp['followers']['total'] >= 10000000:
            
            artist_follow['name'] = artist['name']
            artist_follow['uri-id'] = artist_profile_temp['uri'][15:]
            result_list.append(artist_follow)
    
    return result_list

if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    print(dec_artists(artists_list))
