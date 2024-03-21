import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def recommendation(track, artist, genre):
    # 여기에 코드를 작성합니다.
    URL = f'https://api.spotify.com/v1/search?q=artist%3A{artist}&type=artist&limit=1'
    headers = getHeaders()
    response = requests.get(URL, headers=headers).json()
    user_id = response['artists']['items'][0]['id']

    URL2 = f'https://api.spotify.com/v1/search?q=track%3A{track}&type=track&limit=1'
    response2 = requests.get(URL2, headers=headers).json()

    track_id = response2['tracks']['items'][0]['album']['id']
    URL3 = f'https://api.spotify.com/v1/recommendations?seed_artists={user_id}&seed_genres={genre}&seed_tracks={track_id}'
    response3 = requests.get(URL3, headers=headers).json()

    return [response3['tracks'][i]['album']['name'] for i in range(len(response3['tracks']))]


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    주어진 트랙, 아티스트 이름, 장르로 음악 트랙 추천 목록 출력하기
    (주의) 요청마다 아래 예시 출력과 차이가 있을 수 있음   
    """
    pprint(recommendation('HypeBoy', 'BTS', 'acoustic'))
    # ['Best Of Me', 'A Drop in the Ocean', 'We Are', 'Dear Mr. President', 'Hurt']
