bingo = [list(map(int, input().split())) for _ in range(5)]

bingo_dict = {}
for i in range(5):
    for j in range(5):
        bingo_dict[bingo[i][j]] = (i, j)

num = [] * 25
for _ in range(5):
    tmp = list(map(int, input().split()))
    num.extend(tmp)

visit = [[0] * 5 for _ in range(5)]
visit1 = [[0] * 5 for _ in range(5)]


def bingo3():
    ans = set()
    for i in range(5):
        if visit[i].count(1) == 5:
            ans.add(('row', i))
    for i in range(5):
        if visit1[i].count(1) == 5:
            ans.add(('col', i))
    tmp = 0
    for i in range(5):
        if visit[i][i] == 1:
            tmp += 1
    if tmp == 5:
        ans.add('diagonal1')
    tmp1 = 0
    for i in range(5):
        if visit[i][4-i] == 1:
            tmp1 += 1
    if tmp1 == 5:
        ans.add('diagonal2')
    return len(ans)

for i in range(11):
    x, y = bingo_dict[num[i]]
    visit[x][y] = 1
    visit1[y][x] = 1

for i in range(11,25):
    x, y = bingo_dict[num[i]]
    visit[x][y] = 1
    visit1[y][x] = 1
    if bingo3() == 3:
        print(num[i])
        break