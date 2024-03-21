import itertools
import time
asd = time.time()

n, t = map(int, input().split())
table_tmp = [0] * n + [1.1] * t
table_list = list(set(itertools.permutations(table_tmp, n+t)))
table_list2 = []

for i in range(len(table_list)):
    table_list[i] = list(table_list[i])

for table in table_list:
    ans = 'y'
    if table[0] == 1.1 and table[-1] == 1.1:
        ans = 'n'

    for i in range(n+t-1):
        if table[i] == 1.1 and table[i+1] == 1.1:
            ans = 'n'
    if ans == 'y':
        table_list2.append(table)

head_ability = list(map(int, input().split()))

for table in table_list2:
    for head in head_ability:
        for i in range(n+t):
            if table[i] == 0:
                table[i] = head
                break

head_sum_max_max = []
for table in table_list2:
    head_sum_max = 0
    slice = table.index(1.1)
    table = table[slice:] + table[:slice]
    table = table [1:]
    t_index = []
    i = 0
    li_tmp = []
    while table:
        if len(table) == 1:
            t_index.append(li_tmp+table)
            break
        if table[0] == 1.1:
            t_index.append(li_tmp)
            li_tmp = []
            table.pop(0)
            continue
        li_tmp.append(table.pop(0))
    for i in range(t):
        head_sum_max = max(head_sum_max, sum(t_index[i]))
    head_sum_max_max.append(head_sum_max)
print(min(head_sum_max_max))
#
#
print(time.time()-asd)