import time
import datetime

T = int(input())
start = time.time()
for tc in range(1, 1 + T):
    n, p = map(int, input().split())
    village = [list(map(int, input().split())) for _ in range(n)]

    x = [1, 0, -1, 0]
    y = [0, 1, 0, -1]
    ans = []

    for i in range(n):
        for j in range(n):
            ans_tmp = village[i][j]
            for k in range(4):
                for _ in range(1, p + 1):
                    ii = i + _ * x[k]
                    jj = j + _ * y[k]
                    if 0 <= ii < n and 0 <= jj < n:
                        ans_tmp += village[ii][jj]
            ans.append(ans_tmp)
    print(f'#{tc} {max(ans)}')

sec = time.time() - start
times = str(datetime.timedelta(seconds=sec))
print(f"{times} sec")

