# 아래 함수를 수정하시오.
def even_elements(old_list):
    for i in old_list:
        if (i % 2) == 1:
            old_list.pop(old_list.index(i))
        else:
            pass
    return old_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)

result_01 = []
result_01.extend(result)

print(result_01)


