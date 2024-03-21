
n, m = map(int, input().split())
k = int(input())

map_is = []
bomb_list = []

for i in range(n):
    str_tmp = input()

    for j in range(m):
        if str_tmp[j] == '@':
            bomb_list.append([i, j])

    map_is.append([char for char in str_tmp])

x = [1, 0, -1, 0]
y = [0, 1, 0, -1]

for bomb in bomb_list:
    bomby = bomb[0]
    bombx = bomb[1]
    map_is[bomby][bombx] = '%'

    for i in range(4):
        for fire in range(1, k+1):
            bombby = bomby + fire * x[i]
            bombbx = bombx + fire * y[i]
            if 0 <= bombby < n and 0 <= bombbx < m:
                if map_is[bombby][bombbx] == '#':
                    break
                if map_is[bombby][bombbx] == '_':
                    map_is[bombby][bombbx] = '%'

for i in range(n):
    for j in range(m):
        print(map_is[i][j],end='')
    print()