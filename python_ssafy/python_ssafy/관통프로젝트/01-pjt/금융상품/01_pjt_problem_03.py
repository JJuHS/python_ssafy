from pprint import pprint
import requests

option_ = []

def get_deposit_products():
  global option_
  Api_key = 'd7053202b81f53dc0211997a134e03e9'
  url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={Api_key}&topFinGrpNo=020000&pageNo=1'
  data = requests.get(url).json()
  result = data['result']['optionList']

  for i in range(len(result)):
    a = dict()
    a['은행지점코드'] = result[i]['fin_co_no']
    a['예금방식'] = result[i]['intr_rate_type_nm']
    a['저축기간'] = str(result[i]['save_trm']) + '개월'
    a['기본 금리'] =str(result[i]['intr_rate']) + '%'
    a['최고 우대 금리'] = str(result[i]['intr_rate2']) + '%'
    a['상품 코드'] = result[i]['fin_prdt_cd']
    option_.append(a)
  return option_

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint(result)