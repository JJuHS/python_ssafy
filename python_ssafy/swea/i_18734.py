T = int(input())
for tc in range(1, T+1):
    first_x1, first_y1, first_x2, first_y2 = map(int, input().split())
    second_x1, second_y1, second_x2, second_y2 = map(int, input().split())
    ans_list = [[0]*1001 for _ in range(1001)]
    ans = 0
    for i in range(first_x1, first_x2+1):
        for j in range(first_y1, first_y2+1):
            ans_list[i][j] += 1
    for i in range(second_x1, second_x2+1):
        for j in range(second_y1, second_y2+1):
            ans_list[i][j] += 1
    count2 = 0
    choose1and2 = []
    for i in ans_list:
        count2 += i.count(2)
        if i.count(2) != 0:
            choose1and2.append(0)
    if count2 == 0:
        print(f'#{tc}', 4)
    elif count2 == 1:
        print(f'#{tc}', 3)
    else:
        if len(choose1and2) == 1:
            print(f'#{tc}', 2)
        else:
            print(f'#{tc}', 1)

