# 아래 함수를 수정하시오.
# def intersection_sets(set_A, set_B):
#     return set_A & set_B


# result = intersection_sets({1, 2, 3}, {3, 4, 5})
# print(result)
def intersection_sets(set_A, set_B):
    return set_A.intersection(set_B)


result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result)
