def cal(task):
    global N, task_time, pre_task, task_matrix, cycle
    if cycle:
        return

    if task_matrix[1][task] != -1:
        return

    if pre_task[task] == []:
        for num in range(1, N + 1):
            if num == task:
                task_matrix[num][task] = task_time[task] // 2
                continue
            task_matrix[num][task] = task_time[task]
        return

    used[task] = 1
    for num in range(1, N + 1):
        max_v = 0
        for ptask in pre_task[task]:
            if used[ptask] == 1:
                cycle = True
                return
            cal(ptask)
            if task_matrix[num][ptask] > max_v:
                max_v = task_matrix[num][ptask]
            used[ptask] = 0
        if num == task:
            task_matrix[num][task] = max_v + task_time[task] // 2
            continue
        task_matrix[num][task] = max_v + task_time[task]
    return


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    task_time = [0] * (N + 1)
    pre_task = [[] for _ in range(N + 1)]
    for task in range(1, N + 1):
        temp = list(map(int, input().split()))
        task_time[task] = temp[0]
        if len(temp) > 2:
            pre_task[task] += temp[2:]

    end = range(1, N + 1)
    for num in range(1, N + 1):
        end = [task for task in end if task not in pre_task[num]]
    task_matrix = [[-1] * (N + 1) for _ in range(N + 1)]
    used = [0] * (N + 1)
    cycle = False
    for task in end:
        cal(task)
    if -1 in task_matrix[1][1:]:
        cycle = True
    if cycle:
        print(f'#{t} -1')
    else:
        print(f'#{t} {min([max(row[1:]) for row in task_matrix[1:]])}')