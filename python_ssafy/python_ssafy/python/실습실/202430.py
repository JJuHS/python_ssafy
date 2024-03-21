import itertools
import numpy
# numbers = [63, 31, 27, 11, 25]


# def bubble(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]


# bubble(numbers)
# print(numbers)
# list1 = [1, 4, 1, 2, 7, 5, 2]


# def counting(arr):
#     max_v = max(arr)
#     cnt_arr = [0] * (max_v+1)
#     for num in arr:
#         cnt_arr[num] += 1
#     sorted_arr = []
#     for idx, count in enumerate(cnt_arr):
#         sorted_arr.extend([idx] * count)


# arr1 = [1, 2, 3, 4]
# result = list(itertools.permutations(arr1))
# print(result)


# # 탐욕알고리즘, 동전 종류 : 100, 50, 10
# # 거스름돈에 대한 동전 단위별 개수 출력하는 함수
# def return_coin(coin):
#     tmp = {}
#     tmp[100] = coin//100
#     tmp[50] = (coin%100)//50
#     tmp[10] = ((coin%100)%50)//10
#     return tmp

# print(return_coin(420))



# arr = [3,6,7,1,5,4]
# n = len(arr)
# for i in range(1<<n):    # 1<<n : 부분집합의 개수
# 	for j in range(n):     # 원소의 수만큼 비트를 비교
# 		if i & (1<<j):       # i의 j번 비트가 1인경우
# 				print(arr[j], end=',')   # j번 원소 출력
# 	print()
# print()
#
# arr = [-7, -5, 2, 3, 8, -2, 4, 6, 9, 1]
# n = len(arr)
# result = []
#
# for i in range(n):
#     result.append(list(itertools.combinations(arr, i)))
#
# ans = []
#
# for i in result:
#     for j in i:
#          if sum(j) == 0:
#              ans.append(j)
#
# print(ans)
