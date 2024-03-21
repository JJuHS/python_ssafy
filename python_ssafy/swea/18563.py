# 사과먹기게임

T = int(input())

def find_rotate(n, arr, k):
    global current, directions

    for_bfs = [((current[0],current[1]),0,0)] # 시작 좌표, 현재 방향, 현재까지 우회전 수

    while for_bfs:
        current, direction_tmp, rotate_num = for_bfs.pop(0)
        for direction in directions:
            next_row, next_col = current[0] + direction[0], current[1] + direction[1]
            next_direction = directions.index(direction)

            if 0 <= next_row < n and 0 <= next_col < n and arr[next_row][next_col] !=k and arr[next_row][next_col] !=-1:
                next_turn = rotate_num + (direction_tmp != next_direction)
                for_bfs.append(((next_row, next_col), next_direction, next_turn))
            else:
                next_turn = rotate_num + 1
                for_bfs.append(((next_row, next_col), next_direction, next_turn))
            a = next_direction
            current = [current[0] + directions[0][0], current[1] + directions[0][1]]
        directions = directions[a:] + directions[:a]
        current = [next_row, next_col]

    return rotate_num

directions = [(0,1), (1,0), (0,-1), (-1,0)]

for tc in range(1, T+1):
    N = int(input())
    apple_list = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    current = [0,0]
    M = 0
    for i in range(N):
        for j in range(N):
            if 1 <= apple_list[i][j]<= 10:
                M += 1
    for i in range(1, M+1):
        result += find_rotate(N, apple_list, i)

    print(f'#{tc} {result}')

