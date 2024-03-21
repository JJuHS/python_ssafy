T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(n)]
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 터지는 방향

    res = 0
    for i in range(n):
        for j in range(n):  # 모든 곳에 대하여 탐색
            ans_tmp = score[i][j]
            for k in range(1, 3):   # 두 칸 : 1, 2
                for m in range(4):  # 4 방향
                    nx = i + k * direction[m][0]
                    ny = j + k * direction[m][1]
                    if 0 <= nx < n and 0 <= ny < n:  # 범위 내의 값인지 확인
                        ans_tmp += score[nx][ny]

            if ans_tmp > res:   # 최댓값 갱신
                res = ans_tmp

    print(f'#{tc} {res}')
