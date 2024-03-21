T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        tmp_list = []
        for j in range(n):
            if puzzle[i][j] == 0:
                if len(tmp_list) == k:
                    ans += 1
                tmp_list.clear()
            else:
                tmp_list.append(1)
                if j == n-1:
                    if len(tmp_list) == k:
                        ans += 1


    for i in range(n):
        for j in range(i,n):
            puzzle[i][j], puzzle[j][i] = puzzle[j][i], puzzle[i][j]

    for i in range(n):
        tmp_list = []
        for j in range(n):
            if puzzle[i][j] == 0:
                if len(tmp_list) == k:
                    ans += 1
                tmp_list.clear()
            else:
                tmp_list.append(1)
                if j == n - 1:
                    if len(tmp_list) == k:
                        ans += 1
    print(f'#{tc}', ans)
