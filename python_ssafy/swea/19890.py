N = int(input())
Node = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    if Node[0][i] == 1:
        for j in range(N):
            if Node[i][j] == 1:
                print(0,i,j)