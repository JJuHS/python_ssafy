T = int(input())
for tc in range(1,T + 1):
    n, m = map(int, input().split())
    fly_list = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            ans_tmp = 0
            for k in range(m):
                for l in range(m):
                    ans_tmp += fly_list[i+k][j+l]
            ans = max(ans, ans_tmp)
    print(f'#{tc}',ans)