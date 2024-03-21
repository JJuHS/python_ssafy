x = [1, 0, -1, 0]
y = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    balloon = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            ans_tmp = balloon[i][j]
            for k in range(4):
                xx = x[k] + i
                yy = y[k] + j
                if 0 <= xx < n and 0 <= yy < m:
                    ans_tmp += balloon[xx][yy]
            ans = max(ans, ans_tmp)

    print(f'#{tc} {ans}')