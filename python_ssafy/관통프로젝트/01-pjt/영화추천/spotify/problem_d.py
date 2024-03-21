import json
import os

script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)

def max_polularity(artists):
    artist_popularity = {}

    for artist in artists:
        Id_number = artist['id']
        artist_profile_temp = json.load(open(f"data/artists/{Id_number}.json", encoding="utf-8"))
        artist_popularity[artist['name']] = artist_profile_temp['popularity']
    sorted_artist_list = sorted(artist_popularity.items(), key=lambda x: x[1])

    return sorted_artist_list[-1][0]

# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    artists_json = open("data/artists.json", encoding="utf-8")
    artists_list = json.load(artists_json)

    print(max_polularity(artists_list))
