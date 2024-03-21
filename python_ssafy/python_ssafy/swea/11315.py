T = int(input())

direction = [(1, 0), (0, 1), (1, 1), (-1, 1)]
def concave():
    for k in range(4):
        for i in range(n):
            for j in range(n):
                cnt = 0
                if arr[i][j] == 'o':
                    for m in range(5):
                        tmp_x = i + m * direction[k][0]
                        tmp_y = j + m * direction[k][1]
                        if 0 <= tmp_x < n and 0<= tmp_y < n and arr[tmp_x][tmp_y] == 'o':
                            cnt += 1
                    if cnt == 5:
                        return 'YES'
    return 'NO'

for tc in range(1, T + 1):
    n = int(input())
    arr = [input() for _ in range(n)]
    print(f'#{tc} {concave()}')
