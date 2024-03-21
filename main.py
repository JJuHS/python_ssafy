from collections import deque as dq

def bfs(s, tmp = 0, num_li = [], cnt = 0):
    global ans
    if cnt == 2:
        ans = max(ans, tmp)
        return

    for i in range(s, n - 3):
        for j in range(i + 2, n - 1):
            bfs(j + 2, tmp + ((arr[i] + arr[j]) ** 2), num_li + [i, j], cnt + 1)
    return
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = dq(list(map(int, input().split())))
    ans = 0

    for k in range(n):
        bfs(0)
        arr.append(arr.popleft())

    print(f'#{tc} {ans}')
