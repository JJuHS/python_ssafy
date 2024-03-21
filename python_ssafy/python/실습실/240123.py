# d = {
#     1:'apple',
#     2:'banana',
#     3:'melon'
# }
# d2 = {
#     4:'apple2',
#     5:'banana2',
#     6:'melon2'
# }

# d.update(A = 'ABCD', B = 2)
# print(d)

# d.update(d2)
# print(d)

# d = {3, 2, 1, 9, 100, 4, 87, 39, 10, 52}
# print(d.pop())
# print(d.pop())
# print(d.pop())
# print(d.pop())
# print(d.pop())
# print(d.pop())
# print(d.pop())
# print(d.pop())
# print(d.pop())
# print(d.pop())
# print(d.pop())

# d = {'a','b','c','d','e','f','g','h'}
# print(d.pop())
# print(d.pop())
# print(d.pop())
# print(d.pop())
# print(d.pop())
# print(d.pop())
# print(d.pop())
# print(d.pop())

# print(hash('a'))
# print(int(hash('a')))
# print(hash(int(hash('a'))))
# print(hash('a'))

# my_list = [1, 3, 2, 4]
# print(sorted(my_list), id(sorted(my_list)))
# my_list.sort()
# print(my_list, id(my_list))

# my_list = [1,2,3]
# my_list.append(4)
# my_list.append(5)
# my_list.append(6)
# print(my_list)
# my_list = [1,2,3]
# my_list.append([4,5,6])
# print(my_list)
# my_list.extend([4,5,6])
# print(my_list)

# d = {
#     'plus' : ['더하기', '장점'],
#     'minus' : ['빼기', '적자'],
#     'multiply' : ['곱하기', '다양하게'],
#     'division' : ['나누기', '분열']
# }

# # 실습 1 '빼기' 반환
# print(d['minus'][0])
# print(d.get('minus')[0])
# print(d.setdefault('minus')[0])
# print(d.pop('minus')[0])

# # 실습 2. key 값 순차적으로 출력
# for i in list(d.keys()):
#     print(i)

# # 실습 3. 'square' : ['제곱', '사각형'] 추가
# d['square'] = ['제곱', '사각형']
# d.setdefault('square', ['제곱', '사각형'])
# d.update(square = ['제곱', '사각형'])

# # 실습 4. 'division' 제거
# del d['division']
# d.pop('division','')

# d = {'a', 'b', 'c', 1, 2, 3}

# print(d.pop())
# print(d)

# print(hash(1))
# print(hash(2))
# print(hash('a'))
# print(hash('b'))
