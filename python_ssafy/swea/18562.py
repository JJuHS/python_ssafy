# 순환선
T = int(input())

def numbers(n, numbers):
    if n==0 or n==1 or n==2 or n==3:
        return 0
    if n== 4:
        return max((numbers[0]+numbers[2]), (numbers[1]+numbers[2])) ** 2
    while True:
        for i in range(n):
            for j in range(n):







for tc in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    visited = [False] * n
    result = 0
    print(f'#{tc} {result}')
