T = int(input())

for tc in range(1, T + 1):
    n, q = map(int, input(). split())
    box_list = [0]*n
    work_list = [list(map(int, input().split())) for _ in range(q)]
    for i in range(q):
        for j in range(work_list[i][0]-1, work_list[i][1]):
            box_list[j] = i + 1



    print(f'#{tc}',*box_list)
