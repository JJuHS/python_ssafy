# 아래 함수를 수정하시오.
def sort_tuple(old_tuple):
    new_tuple = tuple(sorted(list(old_tuple)))
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)