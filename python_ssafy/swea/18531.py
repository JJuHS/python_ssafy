import math
T = int(input())
for tc in range(1,T+1):
    n = int(input())+1
    Map = [list(map(int, input().split())) for _ in range(n)]
    people = []

    for i in range(n):
        for j in range(n):
            if Map[i][j] == 1:
                people.append([i,j])
            if Map[i][j] == 2:
                immc = [i,j]
    ans = 0
    for k in people:
        ans_tmp = (((immc[0] - k[0]) ** 2) + (immc[1] - k[1]) ** 2) ** 0.5
        if ans < ans_tmp:
            ans = ans_tmp
    ans = math.ceil(ans)














    print(f'#{tc} {ans}')