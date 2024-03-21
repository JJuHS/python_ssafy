import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_related_artists(name):
    # 여기에 코드를 작성합니다.
    URL = f'https://api.spotify.com/v1/search?q=artist%3A{name}&type=artist&limit=1&offset=0'
    headers = getHeaders()
    response = requests.get(URL, headers=headers).json()
    
    
    if response['artists']['items'] == []:
        return None
    else:
        user_id = response['artists']['items'][0]['id']
        URL2 = f'https://api.spotify.com/v1/artists/{user_id}/related-artists'
        response2 = requests.get(URL2, headers=headers).json()
        return [response2['artists'][i]['name'] for i in range(len(response2['artists']))]


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    아티스트가 존재하면 해당 아티스트의 id를 기반으로 연관 아티스트 목록 구성
    아티스트가 없을 경우 None을 반환
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    print(get_related_artists("NewJeans"))
    # ['STAYC', 'NMIXX', 'LE SSERAFIM', 'IVE', ... 생략 ..., 'CHUNG HA']

    print(get_related_artists("OldShirts"))
    # None
