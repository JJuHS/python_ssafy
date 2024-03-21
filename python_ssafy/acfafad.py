import itertools
import time
asd = time.time()

n, t = map(int, input().split())
table_tmp = [0] * n + [-1] * t
table_list = list(set(itertools.permutations(table_tmp, n + t)))
table_list2 = []

for i in range(len(table_list)):
    table_list[i] = list(table_list[i])

for table in table_list:
    table_list2.append(table)
    table_tmp2 = table + table
    for i in range(len(table)):
        if table_tmp2[i] == table_tmp2[i+1] == -1:
            table_list2.remove(table)
            break

head_ability = list(map(int, input().split()))
for table in table_list2:
    i = 0
    j = 0
    while j < n+t:
        if table[j] == -1:
            j += 1
        if j == n+t:
            break
        table[j] = head_ability[i]
        i += 1
        j += 1

head_sum_max_max = []
for table in table_list2:
    head_sum_max = 0
    slice = table.index(-1)
    table = table[slice:] + table[:slice]
    table = table [1:]
    t_index = []
    i = 0
    li_tmp = []
    while table:
        if len(table) == 1:
            t_index.append(li_tmp+table)
            break
        if table[0] == -1:
            t_index.append(li_tmp)
            li_tmp = []
            table.pop(0)
            continue
        li_tmp.append(table.pop(0))
    for i in range(t):
        head_sum_max = max(head_sum_max, sum(t_index[i]))
    head_sum_max_max.append(head_sum_max)
print(min(head_sum_max_max))
print(time.time()-asd)
