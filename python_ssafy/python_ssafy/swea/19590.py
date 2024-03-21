import time
import datetime
start = time.time()



n = int(input())

monster_map = []
for i in range(n):
    a = list(map(int, input().split()))
    monster_map.append(a)

k = int(input())

x = [1, 1, -1, -1]
y = [1, -1, 1, -1]

ans = 0
for i in range(n):
    for j in range(n):
        ans_tmp = 0
        for m in range(4):
            for _ in range(1,k+1):
                ii = i + _ * x[m]
                jj = j + _ * y[m]
                if 0 <= ii < n and 0 <= jj < n:
                    ans_tmp += monster_map[ii][jj]

        if ans_tmp > ans:
            ans = ans_tmp
print(ans)


sec = time.time()-start
times = str(datetime.timedelta(seconds=sec))
print(f"{times} sec")