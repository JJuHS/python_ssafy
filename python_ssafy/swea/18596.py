import copy
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    task_list = [list(map(int, input().split())) for _ in range(n)]
    task_list_tmp = [[idx, tmp] for idx, tmp in enumerate(task_list)]

    i = 0
    stack_tmp = []
    while len(stack_tmp) != n:
        for j in task_list_tmp:
            if j[1][1] == i:
                stack_tmp.append([j[0], j[1]])
        i += 1

    stack = stack_tmp
    # task_order = stack.pop(2)
    # tasked = [j[0] for j in task_order]
    #
    # print(f'#{tc}', task_order)
    # print(tasked)
