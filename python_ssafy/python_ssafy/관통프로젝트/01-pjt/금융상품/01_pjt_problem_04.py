from pprint import pprint
import requests

def get_deposit_products():
  Api_key = 'd7053202b81f53dc0211997a134e03e9'
  url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={Api_key}&topFinGrpNo=020000&pageNo=1'
  data = requests.get(url).json()
  base_list = data['result']['baseList']
  option_list = data['result']['optionList']

  total_list = []

  for i in range(len(base_list)):
    goods_code =  base_list[i]['fin_prdt_cd']
    temp_dict = {}
    temp_list = []
    for j in range(len(option_list)):
      goods_code_01 = option_list[j]['fin_prdt_cd']
      
      temp_dict_01 = {}
      if goods_code == goods_code_01:
        temp_dict['금융회사명'] = base_list[i]['kor_co_nm']
        temp_dict['금융상품명'] = base_list[i]['fin_prdt_nm']
        temp_dict_01['저축금리유형'] = str(option_list[j]['intr_rate_type']) + ' : ' + str(option_list[j]['intr_rate_type_nm'])
        temp_dict_01['저축기간'] = str(option_list[j]['save_trm']) + '개월'
        temp_dict_01['저축금리'] = str(option_list[j]['intr_rate']) + '%'
        temp_dict_01['최고우대금리'] = str(option_list[j]['intr_rate2']) + '%'
        temp_list.append(temp_dict_01)
      temp_dict['개별금리정보'] = temp_list
    total_list.append(temp_dict)   

  return total_list

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint(result)