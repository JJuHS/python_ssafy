T = int(input())

for tc in range(1, T+1):
    n = int(input())
    game_board = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    ans_list = []
    for i in range(n):
        for j in range(n):
            for k in range(i, n):
                for m in range(j, n):
                    if game_board[i][j] == game_board[k][m]:
                        ans_list.append((k - i + 1) * (m - j + 1))

    ans = ans_list.count(max(ans_list))
    print(f'#{tc} {ans}')
