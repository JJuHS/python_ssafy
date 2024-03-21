### Class

## 실습 1
# class Singer():
#     def __init__(self): # 생성자 메서드
#         self.occ = '가수'   # 멤버변수
#         self.birth = '2000년 00월 00일'   # 멤버변수
#         self.nation = '한국'   # 멤버변수

#     # 인스턴스 메서드 : 객체의 속성에 접근, self 매개변수를 통해 객체에 접근
#     def rap(self):
#         print('랩하기')
#     def dance(self):
#         print('댄스 추기')
#     def sing(self):
#         print('소몰이 부르기')

# # 클래스 인스턴스 생성        
# singer1 = Singer()

# # 인스턴스 속성 출력
# print('직업:',singer1.occ)
# print('생년월일:',singer1.birth)
# print('국적:',singer1.nation)

# # 인스턴스 메서드 호출
# singer1.rap()
# singer1.dance()
# singer1.sing()

## 실습 2
# my_count 메서드 만들기
# 클래스명 : my_str
# 조건 1 생성자 메서드 구조
# 조건 2 클래스 변수와 멤버 변수 생성
# 조건 3 기능은 count()와 동일하게

# class my_str:
#     def __init__(self, string=''):
#         self.string = string
#         # self.cnt = 0

#     def count(self,find_string):
#         self.cnt = self.string.count(finc_string)
#         return self.cnt
        
# my_str1 = my_str('HelloHello')



# class my_str:
#     def __init__(self, string=''):
#         self.string = string
#         

#     def count(self,find_string):
#         cnt = 0
#         for i in self.string:
#             if i == find_string:
#                 cnt += 1
#         return cnt

# print(my_str1.count('H'))
# print(my_str1.count('e'))
# print(my_str1.count('l'))
# print(my_str1.count('o'))
# 클래스 변수의 역할 : 클래스 변수로 데이터를 추적하거나 데이터를 공유
# 멤버 변수의 역할 : 클래스 변수로 데이터를 추적하거나 데이터의 개별화

## 실습 3
# 클래스 메서드는 클래스 레벨에서 동작화며, cls 매개변수를 통해 클래스 자체에 접근하다.

# class Singer():
#     # 클래스 변수
#     occ = '가수' 
#     birth = '2000년 00월 00일'  
#     nation = '한국' 

#     @classmethod    # 데코레이터
#     def rap(cls):
#         print('랩하기')

#     @classmethod    # 데코레이터
#     def dance(cls):
#         print('댄스 추기')

#     @classmethod    # 데코레이터
#     def sing(cls):
#         print('소몰이 부르기')


# # 클래스 인스턴스 생성        
# singer1 = Singer()

# # 인스턴스 속성 출력
# print('직업:',singer1.occ)
# print('생년월일:',singer1.birth)
# print('국적:',singer1.nation)

# # 인스턴스 메서드 호출
# singer1.rap()
# singer1.dance()
# singer1.sing()

# 실습 4
# 스태틱 메서드 : 클래스, 인스턴스와는 무관하게 독립적으로 동작하는 메서드
# 클래스 내부에서 선언되지만 클래스 변수에 접근하지 않음.

# class Singer():
#     # 클래스 변수
#     occ = '가수' 
#     birth = '2000년 00월 00일'  
#     nation = '한국' 

#     @staticmethod    # 데코레이터
#     def rap():
#         print('랩하기')

#     @staticmethod    # 데코레이터
#     def dance():
#         print('댄스 추기')

#     @staticmethod    # 데코레이터
#     def sing():
#         print('소몰이 부르기')


# # 클래스 인스턴스 생성        
# singer1 = Singer()

# # 인스턴스 속성 출력
# print('직업:',singer1.occ)
# print('생년월일:',singer1.birth)
# print('국적:',singer1.nation)

# # 인스턴스 메서드 호출
# singer1.rap()
# singer1.dance()
# singer1.sing()



