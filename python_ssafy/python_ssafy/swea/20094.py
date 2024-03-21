from collections import deque
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    numbers = deque(map(int, input().split()))
    for i in range(m):
        numbers.append(numbers.popleft())
    print(f'#{tc} {numbers[0]}')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    numbers = deque(map(int, input().split()))
    print(f'#{tc} {numbers[m%n]}')
