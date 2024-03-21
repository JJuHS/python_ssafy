import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_popular_tracks():
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1/search?q=artist_genres%3Ak-pop&type=track&limit=20'
    headers = getHeaders()
    response = requests.get(URL, headers=headers).json()
    tmp = []
    for i in range(20):
        if response['tracks']['items'][i]['popularity'] >= 90:
            tmp.append(response['tracks']['items'][i]['album']['artists'][0]['name'])
    return tmp


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(get_popular_tracks())
    """
    ['Cupid - Twin Ver.', 'Take Two', 'Like Crazy', 'MONEY', 'OMG', 'Like Crazy']
    """
