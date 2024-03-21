import sys
sys.setrecursionlimit(5000)

n, m = map(int, sys.stdin.readline().split())
p_list = [[] for _ in range(n)]
cnt = 0

def find_friend(x, y):
    global cnt
    
    x_ = [1,0,-1,0]
    y_ = [0,1,0,-1]
    for i in range(4):
        xx = x + x_[i]
        yy = y + y_[i]
        if (xx >= n) or (yy >= m) or (xx < 0) or (yy < 0):
            continue
        elif p_list[xx][yy] == 'X':
            continue
        elif p_list[xx][yy] == 'P':
            cnt += 1
            p_list[xx][yy] = 'X'
            find_friend(xx,yy)
        else:
            p_list[xx][yy] = 'X'
            find_friend(xx,yy)
z=0
for i in range(n):
    tmp_word = sys.stdin.readline().strip()
    p_list[i] = [char for char in tmp_word]
    t = 0
    while (z==0) and (t < m):
        if 'I' in tmp_word:
            x = i
            y = tmp_word.index('I')
            z=1
        t+=1
        

find_friend(x, y)

if cnt == 0:
    print('TT')
else:
    print(cnt)