
from pprint import pprint
import requests

def get_deposit_products():
  Api_key = 'd7053202b81f53dc0211997a134e03e9'
  url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={Api_key}&topFinGrpNo=020000&pageNo=1'
  data = requests.get(url).json()
  result = data['result']
  results = result.keys()
  return results

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint(result)