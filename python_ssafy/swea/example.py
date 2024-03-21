T = int(input())

def find_rotate(n, arr):
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    for_bfs = [((0,0), 0, 0)]  # 시작 좌표, 현재 방향, 현재까지 우회전 수

    while for_bfs:
        current, direction_tmp, rotate_num = for_bfs.pop(0)

        for direction in directions:
            next_row, next_col = current[0] + direction[0], current[1] + direction[1]
            next_direction = directions.index(direction)

            if 0 <= next_row < n and 0 <= next_col < n and arr[next_row[next_col]] !=1:
                next_turn = rotate_num + (direction_tmp != next_direction)
                for_bfs.append(((next_row, next_col), next_direction, next_turn))

    return rotate_num

for tc in range(1, T+1):
    N = int(input())
    apple_list = [list(map(int, input().split())) for _ in range(N)]
    result = find_rotate(N, apple_list)
    print(f'{tc} {result}')

