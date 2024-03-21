import sys
N,M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
ans = -555
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            a = num_list[i] + num_list[j] + num_list[k]
            if (abs(a-M) < abs(M - ans)) and (a<=M):
                ans = a
            else:
                pass
print(ans)