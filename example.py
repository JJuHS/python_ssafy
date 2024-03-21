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
def bingo3():
    pass

for i in range(11):
    x, y = bingo_dict[num[i]]
    visit[x][y] = 1
