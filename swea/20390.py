T = int(input())
direction = [(1, 0), (0, 1)]

def min_sum(tmp = 0, cnt = 0, now = (0, 0)):
    global ans
    if cnt == 2 * n - 2:
        ans = min(ans, tmp)
        return
    for i in range(2):
        nx = now[0] + direction[i][0]
        ny = now[1] + direction[i][1]
        if nx < n and ny < n:
            min_sum(tmp + arr[nx][ny], cnt + 1, (nx, ny))


for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 10**6
    min_sum(arr[0][0])
    print(f'#{tc} {ans}')