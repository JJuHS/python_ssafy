import time
start = time.time()




wld_map = [['_'] * 5 for k in range(4)]
bomb1 = map(int, input().split())
bomb2 = map(int, input().split())

x = [1, 0, -1, 0, 1, 1, -1, -1]
y = [0, 1, 0, -1, 1, -1, 1, -1]

for bomb in [bomb1, bomb2]:
    bomby, bombx = bomb
    for i in range(8):
        bombbx = bombx + x[i]
        bombby = bomby + y[i]
        if 0 <= bombbx < 4 and 0 <= bombby < 5:
            wld_map[bombbx][bombby] = '#'

for i in range(4):
    for j in range(5):
        print(wld_map[i][j], '', end='')
    print()


sec = time.time()-start
print(sec)