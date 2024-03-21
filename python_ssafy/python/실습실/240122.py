'''
# 문자열 메서드 실습
a = " Practice makes perfect "

#1. 문자열 a에서 'e'의 개수 세기 ★★★
print(a.count('e'))

#2. 문자열 a에서 i의 위치 찾기 (2가지 방법) ★★★★★
print(a.find('i'))
print(a.index('i'))
    # print(a.index('z'))  # ValueError 
    # print(a.find('z'))   # -1

#3. 문자열 a의 문자 사이에 . 삽입 ★★
print('.'.join(a))

#4. 문자열 a를 공백 기준으로 분리하기 ★★★★★
print(a.split())

#5. 문자열 a에서 'makes'를 'made'fh qkRnrl
print(a.replace('makes','made'))

#6. 문자열 a를 대문자에서 소문자로 바꾸기, 소문자에서 대문자로 바꾸기
print(a.upper())
print(a.lower())

#7. 문자열 a의 양쪽 공백 삭제하기 ★★★
print(a.strip())

#8. 시간을 입력받아 HH:MM:SS 출력하기 ★★★★★
# b = input().split(':')
# print(b[0])
import time
print(time.strftime('%H:%M:%S').split(':')[0], '시', time.strftime('%H:%M:%S').split(':')[1], '분', time.strftime('%H:%M:%S').split(':')[2], '초')
# 8-1. 890927-1234567 에서 생일만 보여주기
c = '890927-1234567'
print('생일:', (c.split('-'))[0][2:])

if (c.split('-'))[1][0] == '1':
    print('남자입니다')
else:
    print('여자입니다')
'''

'''
# 리스트 메서드 실습
a = ['b', 'a', 'n', 'a', 'n', 'a']

# 1. 리스트 a의 마지막에 'a' 추가하기
a.append('a')
print(a)
    
# 2-1. 리스트 a를 오름차순으로 정렬 : 원본변경
a.sort()
print(a)

# 3. 리스트 a를 내림차순으로 정렬
a.sort(reverse=True)
print(a)

# 4. 리스트 a를 역순으로 뒤집기
a.reverse()
print(a)

# 5. 리스트 a에서 문자 'a' 삭제하기
a.remove('a')
print(a)

# ==================================================
# 2-2. 리스트 a를 오름차순으로 정렬 : 원본유지
print(sorted(a))

# 6. 리스트 a의 마지막 요소를 꺼내어 삭제하고 반환값 출력
print(a.pop())

# 7. 리스트 a에서 문자 'n'의 개수 출력
print(a.count('n'))
'''